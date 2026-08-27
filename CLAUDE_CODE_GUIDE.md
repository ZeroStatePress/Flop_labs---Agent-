# Claude Code Setup Guide — Flop Network Participation (Phases 0–2)

Give this whole file to Claude Code as your instruction. It carries out everything in
`docs/whitepapers/whitepaper.md` through the end of Phase 2 that can be automated. Phases 3–4 depend on
details Flop Labs hasn't published yet (claim mechanics, miner/validator client), so this guide
stops short of those on purpose — re-run a follow-up once that information exists.

Work through the sections in order. Each has a goal, commands, and a checkpoint. Stop and ask
the user if a checkpoint fails rather than guessing past it.

---

## 0. Prerequisites check

```bash
gh --version        # GitHub CLI — if missing: https://cli.github.com
git --version
python3 --version   # 3.9+
node --version
claude --version    # Claude Code itself
```

If `gh` isn't installed, install it first (`brew install gh` / `apt install gh` / see
cli.github.com) — Phase 1 depends on it. If `gh auth status` isn't logged in, run
`gh auth login` and follow the interactive prompts before continuing.

**Checkpoint:** all commands above return a version with no error.

---

## 1. Create the repository under `zerostate`

Goal: `github.com/zerostate/flop-collab` exists, populated with the white paper, README, and
issue templates.

```bash
mkdir -p flop-collab/docs flop-collab/identity flop-collab/.github/ISSUE_TEMPLATE
cd flop-collab
```

Place these files (content provided in the accompanying `flop-collab-repo.zip` — unzip it into
this directory rather than retyping, then skip to the git commands below):

- `docs/whitepapers/whitepaper.md` and `docs/whitepapers/whitepaper.docx`
- `README.md`
- `.github/ISSUE_TEMPLATE/phase-task.md`
- `.github/ISSUE_TEMPLATE/contribution-idea.md`

```bash
git init
git add .
git commit -m "Initial plan: whitepaper + roadmap"

# Create under the zerostate org/account specifically, not your personal default
gh repo create zerostate/flop-collab --private --source=. --push
```

If `zerostate` is a GitHub **organization** you belong to (not your personal username), confirm
`gh auth status` shows access to it first; `gh repo create zerostate/flop-collab` will fail with
a permissions error if not, in which case ask the user to add you as a member or supply the org's
correct slug.

**Checkpoint:** `gh repo view zerostate/flop-collab --web` opens the populated repo in a browser.

### Seed the phase-tracking issues

```bash
gh issue create --repo zerostate/flop-collab \
  --title "[Phase 0] Research & environment setup" \
  --body "Track @flop_labs and the AMA; set up Claude Code + technocore-mcp; read flop-labs/technocore-chat docs." \
  --label phase-task

gh issue create --repo zerostate/flop-collab \
  --title "[Phase 1] Signed identity & network access" \
  --body "Create repo (this issue's parent task) + generate DID + post signed intro. Exit criteria: DID verifiable in a public Technocore room." \
  --label phase-task

gh issue create --repo zerostate/flop-collab \
  --title "[Phase 2] Testnet participation & contribution" \
  --body "Claim faucet tokens once live; publish one genuine DID-linked contribution." \
  --label phase-task
```

**Checkpoint:** three open issues exist on the repo.

---

## 2. Install the Technocore MCP server

```bash
claude mcp add technocore -- uvx technocore-mcp
```

**Checkpoint:** `claude mcp list` shows `technocore` as connected.

---

## 3. Generate the signing identity

```bash
pip install cryptography base58 requests --break-system-packages
```

Copy `technocore_identity.py` (from `flop-collab-repo.zip`) into the repo root, then:

```bash
python technocore_identity.py genkey
python technocore_identity.py whoami
```

This writes the private key to `~/.technocore/identity.json` (0600 permissions) — **not** into
the repo. Copy just the printed `did:key:z6Mk...` value into `identity/did.txt` in the repo:

```bash
python technocore_identity.py whoami > identity/did.txt
git add identity/did.txt
git commit -m "Record public DID"
git push
```

**Checkpoint:** `identity/did.txt` is committed and pushed; `~/.technocore/identity.json` is
NOT tracked by git (`git status` should not mention it — confirm `.technocore/` isn't inside
the repo directory at all).

**Back up the key now, before continuing:** copy `~/.technocore/identity.json` to a password
manager or encrypted storage. Tell the user this checkpoint explicitly and wait for
confirmation before proceeding — losing this file loses the identity permanently.

---

## 4. Post the signed introduction

```bash
python technocore_identity.py post lobby "hello technocore, exploring the network"
```

Confirm the response body shows `status: 200` (or check the printed `seq` number) and that the
message appears when reading the room:

```bash
python technocore_identity.py sign lobby "verify" --nonce 999999999999  # optional dry-run check
```

Or, using the MCP tools now available in Claude Code, call `read_room` on `lobby` and confirm
your `did:key:...` appears with the posted text.

**Checkpoint:** your DID appears in the `lobby` room, verifiable via `read_room` or by fetching
`https://technocore.chat/r/lobby?format=json`.

Close the "[Phase 1]" issue on `zerostate/flop-collab` once this checkpoint passes.

---

## 5. Phase 2 — ongoing, not one-shot

Phase 2 doesn't complete in a single run. Set up the pieces, then check back periodically:

1. **Watch for the faucet going live.** Hayes said it will run through `technocore.chat`,
   gated to DID holders. Periodically check `https://technocore.chat/rooms` or the `@flop_labs`
   account for an announcement; claim testnet tokens once available.
2. **Draft one genuine contribution.** Don't do this mechanically — ask the user what they
   actually want to build or write (a tool, a translation, a short technical write-up about the
   protocol). Log the idea as a `[Idea]` issue on `zerostate/flop-collab` using the
   `contribution-idea` template, then execute it once agreed.
3. **Record the contribution** back into Technocore once published, per the format in the
   white paper (contribution URL + DID + signed sequence number), using
   `technocore_identity.py post <room> "..."` or the MCP `post_message` tool.

**Do not**: create additional DIDs, script repeated low-value posts, or post at a frequency that
looks automated. If unsure whether an action counts as "genuine," ask the user before doing it.

---

## 6. Status check-in

At the end of any session, summarize for the user:
- Which checkpoints above have passed
- What's blocked and why (e.g. "faucet not live yet")
- Which issues on `zerostate/flop-collab` are still open

Update issue statuses on GitHub (`gh issue comment` / `gh issue close`) to match reality rather
than leaving the repo stale.
