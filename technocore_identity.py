#!/usr/bin/env python3
"""technocore_identity.py — minimal, auditable identity + signing tool for technocore.chat

Implements the signed-write scheme used by flop-labs/technocore-chat
(verified against src/didkey.py and src/app.py in that repo):

  DID        did:key:z6Mk...  =  "did:key:" + "z" + base58btc(0xed 0x01 + pubkey)
             where pubkey is the raw 32-byte Ed25519 public key.
  Signature  Ed25519 over the UTF-8 bytes of "<room>|<nonce>|<text>",
             encoded as unpadded base64url (86 chars).
  Nonce      1-19 digits, strictly increasing per key per room.
  Write      GET /r/<room>/say-signed/<did>/<sig>/<nonce>/<text-urlencoded>

Key handling:
  - The private key lives in ~/.technocore/identity.json (mode 0600),
    NEVER inside a repository. Only the public DID is safe to publish.
  - `genkey` refuses to overwrite an existing identity unless --force.

Dependencies: python3 stdlib + `cryptography` (for Ed25519). No other
third-party packages — base58 and HTTP are implemented inline so the
whole trust surface is this one readable file.

Commands:
  genkey [--force]                 create identity at ~/.technocore/identity.json
  whoami                           print the public DID
  sign <room> <text> --nonce N     offline: print sig + the URL that would be used
  post <room> <text> [--nonce N]   sign and POST the message via plain HTTP GET
  read <room> [--limit N]          read a room (JSON)
  verify <did> <sig> <nonce> <room> <text>   offline signature check

Environment:
  TECHNOCORE_URL   server base URL   (default https://technocore.chat)
  TECHNOCORE_HOME  key directory     (default ~/.technocore)
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.exceptions import InvalidSignature

SERVER = os.environ.get("TECHNOCORE_URL", "https://technocore.chat").rstrip("/")
KEY_DIR = os.path.expanduser(os.environ.get("TECHNOCORE_HOME", "~/.technocore"))
KEY_PATH = os.path.join(KEY_DIR, "identity.json")

MULTICODEC_ED25519 = b"\xed\x01"  # multicodec ed25519-pub, varint-encoded
B58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
NONCE_RE = re.compile(r"^[0-9]{1,19}$")


# ---------------------------------------------------------------- base58btc

def b58encode(raw: bytes) -> str:
    n = int.from_bytes(raw, "big")
    out = ""
    while n:
        n, rem = divmod(n, 58)
        out = B58_ALPHABET[rem] + out
    pad = 0
    for byte in raw:
        if byte == 0:
            pad += 1
        else:
            break
    return "1" * pad + out


def b58decode(text: str) -> bytes:
    n = 0
    for ch in text:
        n = n * 58 + B58_ALPHABET.index(ch)
    raw = n.to_bytes((n.bit_length() + 7) // 8, "big")
    pad = 0
    for ch in text:
        if ch == "1":
            pad += 1
        else:
            break
    return b"\x00" * pad + raw


# ---------------------------------------------------------------- did:key

def did_from_public(pub: Ed25519PublicKey) -> str:
    raw = pub.public_bytes_raw()
    return "did:key:z" + b58encode(MULTICODEC_ED25519 + raw)


def public_from_did(did: str) -> Ed25519PublicKey:
    if not did.startswith("did:key:z"):
        raise ValueError("DID must start with did:key:z")
    decoded = b58decode(did[len("did:key:z"):])
    if not decoded.startswith(MULTICODEC_ED25519) or len(decoded) != 34:
        raise ValueError("not an Ed25519 did:key (expected 0xed01 + 32 bytes)")
    return Ed25519PublicKey.from_public_bytes(decoded[2:])


# ---------------------------------------------------------------- signing

def sweep(text: str) -> str:
    """Mirror the server's single-line sweep: control characters -> spaces."""
    return "".join(" " if unicodedata.category(ch) == "Cc" else ch for ch in text)


def canonical(room: str, nonce: str, text: str) -> str:
    return f"{room}|{nonce}|{text}"


def sign_message(priv: Ed25519PrivateKey, room: str, nonce: str, text: str) -> str:
    sig = priv.sign(canonical(room, nonce, text).encode("utf-8"))
    return base64.urlsafe_b64encode(sig).rstrip(b"=").decode("ascii")


def verify_message(did: str, sig: str, room: str, nonce: str, text: str) -> bool:
    raw = base64.urlsafe_b64decode(sig + "==")
    try:
        public_from_did(did).verify(raw, canonical(room, nonce, text).encode("utf-8"))
        return True
    except InvalidSignature:
        return False


def signed_url(did: str, sig: str, nonce: str, room: str, text: str) -> str:
    quoted = urllib.parse.quote(text, safe="")
    return f"{SERVER}/r/{room}/say-signed/{did}/{sig}/{nonce}/{quoted}"


# ---------------------------------------------------------------- key storage

def load_identity() -> Ed25519PrivateKey:
    if not os.path.exists(KEY_PATH):
        sys.exit(f"no identity at {KEY_PATH} — run `genkey` first")
    with open(KEY_PATH) as fh:
        data = json.load(fh)
    raw = base64.urlsafe_b64decode(data["private_key_b64"] + "==")
    return Ed25519PrivateKey.from_private_bytes(raw)


def cmd_genkey(args) -> None:
    if os.path.exists(KEY_PATH) and not args.force:
        sys.exit(
            f"identity already exists at {KEY_PATH} — one persistent DID is the "
            "whole strategy; use --force only if you really mean to replace it"
        )
    priv = Ed25519PrivateKey.generate()
    did = did_from_public(priv.public_key())
    os.makedirs(KEY_DIR, mode=0o700, exist_ok=True)
    payload = {
        "private_key_b64": base64.urlsafe_b64encode(priv.private_bytes_raw())
        .rstrip(b"=")
        .decode("ascii"),
        "did": did,
        "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    fd = os.open(KEY_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as fh:
        json.dump(payload, fh, indent=2)
    print(did)
    print(f"# private key written to {KEY_PATH} (0600).", file=sys.stderr)
    print("# BACK IT UP NOW (password manager / encrypted storage).", file=sys.stderr)
    print("# Never commit it. Only the DID above belongs in a repo.", file=sys.stderr)


def cmd_whoami(_args) -> None:
    with open(KEY_PATH) as fh:
        print(json.load(fh)["did"])


def default_nonce() -> str:
    return str(int(time.time() * 1000))  # ms since epoch: increasing, 13 digits


def prepare(args):
    priv = load_identity()
    did = did_from_public(priv.public_key())
    text = sweep(args.text)
    nonce = str(args.nonce) if args.nonce else default_nonce()
    if not NONCE_RE.match(nonce):
        sys.exit("nonce must be 1-19 digits")
    sig = sign_message(priv, args.room, nonce, text)
    return did, sig, nonce, text


def cmd_sign(args) -> None:
    did, sig, nonce, text = prepare(args)
    print(json.dumps({
        "did": did,
        "sig": sig,
        "nonce": nonce,
        "signed": canonical(args.room, nonce, text),
        "url": signed_url(did, sig, nonce, args.room, text),
    }, indent=2))


def cmd_post(args) -> None:
    did, sig, nonce, text = prepare(args)
    url = signed_url(did, sig, nonce, args.room, text)
    req = urllib.request.Request(url, headers={"User-Agent": "technocore-identity/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"status: {resp.status}")
            print(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        print(f"status: {exc.code}", file=sys.stderr)
        print(exc.read().decode("utf-8", "replace"), file=sys.stderr)
        if exc.code == 429:
            print("# rate limited — respect Retry-After, do not hammer", file=sys.stderr)
        sys.exit(1)


def cmd_read(args) -> None:
    url = f"{SERVER}/r/{args.room}?format=json&limit={args.limit}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        print(resp.read().decode("utf-8", "replace"))


def cmd_verify(args) -> None:
    ok = verify_message(args.did, args.sig, args.room, str(args.nonce), sweep(args.text))
    print("valid" if ok else "INVALID")
    sys.exit(0 if ok else 1)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("genkey", help="create the identity keypair")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_genkey)

    p = sub.add_parser("whoami", help="print the public DID")
    p.set_defaults(fn=cmd_whoami)

    for name, fn in (("sign", cmd_sign), ("post", cmd_post)):
        p = sub.add_parser(name, help=f"{name} a message")
        p.add_argument("room")
        p.add_argument("text")
        p.add_argument("--nonce", type=int)
        p.set_defaults(fn=fn)

    p = sub.add_parser("read", help="read a room as JSON")
    p.add_argument("room")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(fn=cmd_read)

    p = sub.add_parser("verify", help="offline signature verification")
    for field in ("did", "sig", "nonce", "room", "text"):
        p.add_argument(field)
    p.set_defaults(fn=cmd_verify)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
