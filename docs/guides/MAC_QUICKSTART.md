# Mac Quickstart — Phase 1 in one sitting

The exact commands for the local (Mac) session that establishes the signing
identity. Everything else — repo, tooling, research, roadmap — is already
done; this is the ~10-minute part that must happen on a machine you keep.

Run top to bottom. Stop at any ❌ and fix before continuing.

## 0. Prerequisites (one-time)

```bash
git --version                  # ships with Xcode CLT; install if prompted
python3 --version              # 3.9+ (macOS ships one; brew install python if old)
python3 -m pip install cryptography
```

Optional but recommended (for the agent side, issues #4/#5):

```bash
brew install gh && gh auth login       # GitHub CLI
claude mcp add technocore -- uvx technocore-mcp   # Technocore tools in Claude Code
```

## 1. Clone and enter the repo

```bash
git clone https://github.com/ZeroStatePress/Flop_labs---Agent-.git
cd Flop_labs---Agent-
```

## 2. Generate the identity  → closes half of #7

```bash
python3 technocore_identity.py genkey
python3 technocore_identity.py whoami
```

- Prints your `did:key:z6Mk...` — this is the public identity.
- Writes the **private key** to `~/.technocore/identity.json` (mode 0600).
- If it says an identity already exists: **stop** — do not `--force` unless
  you are certain the old one is disposable. One DID is the whole strategy.

## 3. ⚠️ BACK UP THE KEY — do this before anything else

Copy `~/.technocore/identity.json` into your password manager (1Password:
attach it to a new item) or other encrypted storage. Losing this file loses
the identity permanently; leaking it lets someone impersonate you.

```bash
cat ~/.technocore/identity.json   # copy the JSON into the password manager
```

## 4. Publish the public DID  → closes #7

```bash
python3 technocore_identity.py whoami > identity/did.txt
git add identity/did.txt
git commit -m "Record public DID"
git push
git status   # must NOT mention identity.json or .technocore anywhere
```

(The repo's `.gitignore` already blocks `identity.json`, `.technocore/`,
`*.key`, `*.pem` — the last line is belt-and-braces.)

## 5. Post the signed introduction  → closes #8

Dry-run first (offline, nothing sent):

```bash
python3 technocore_identity.py sign lobby "hello" --nonce 1
```

Then the real post:

```bash
python3 technocore_identity.py post lobby "hello technocore, exploring the network"
```

Expect `status: 200`. Verify your DID is now publicly visible:

```bash
python3 technocore_identity.py read lobby --limit 20
```

(or open `https://technocore.chat/r/lobby?format=json` in a browser).

If you get a `429`: wait the number of seconds in the response and retry
once — do not loop.

## 6. Close the loop on GitHub

- Close [#7](https://github.com/ZeroStatePress/Flop_labs---Agent-/issues/7)
  and [#8](https://github.com/ZeroStatePress/Flop_labs---Agent-/issues/8)
  (and #4/#5 if you did the optional installs) — or just tell Claude and
  it will update the board.

## Done — what "done" means

Your DID is live and verifiable on the network: the first step that
actually counts toward airdrop eligibility is complete. From here the
roadmap is event-driven:

| Watch for | Then |
|---|---|
| Tokenomics infographic (imminent) | read; update research |
| Hayes AMA (~first week Sept) | attend with the prepared questions in [#13](https://github.com/ZeroStatePress/Flop_labs---Agent-/issues/13) |
| Faucet live on technocore.chat | claim with this DID ([#9](https://github.com/ZeroStatePress/Flop_labs---Agent-/issues/9)) |

## Never do

- Post the private key anywhere, including "just temporarily".
- Generate a DID through any website or hosted platform.
- Create a second DID or script bulk posts — the network's own metrics
  flag exactly that, and it risks the identity you just built.
