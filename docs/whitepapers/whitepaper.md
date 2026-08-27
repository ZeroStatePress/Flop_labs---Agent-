# Flop Network Participation & Collaboration Plan
### A phased approach to Technocore access, testnet contribution, and open-source collaboration

**Prepared:** August 27, 2026
**Status:** Living document — update as Flop Labs publishes more detail
**Author:** [Your name]

---

## 1. Executive Summary

Flop Labs, led by Arthur Hayes (BitMEX co-founder), is building the "Flop Network" — a proposed proof-of-useful-inference protocol where AI agents pay for compute and decentralized memory using a native token, FLOP. The project is pre-launch: no whitepaper, no named chain, no audited tokenomics as of this writing. What exists today is a public X account, a landing page, and one real piece of infrastructure — `technocore-chat`, a lightweight HTTP coordination service for agents.

This document has two objectives, in priority order:

1. **Primary — maximize legitimate eligibility for the FLOP airdrop** by establishing a durable, verifiable agent identity and participating honestly in whatever testnet activity Flop Labs defines, for as long as that activity is worth the effort relative to the project's uncertainty.
2. **Secondary — evaluate and, if warranted, contribute to the underlying protocol**, because the coordination-layer design (signed agent identity, HTTP-native access for fetch-only sandboxes, engagement-quality metrics) has applicability to agentic workflows beyond this one project.

Both objectives point to the same first steps, so nothing here asks you to choose between them yet.

---

## 2. Background

### 2.1 Timeline of public facts

| Date | Event |
|---|---|
| Aug 18, 2026 | Flop Labs announces the Flop Network publicly on X |
| ~Aug 19, 2026 | Arthur Hayes announces he will lead Flop Labs as CEO |
| Aug 20–25, 2026 | Flop Labs account grows from ~570 to several hundred thousand followers, riding Hayes' ~800K-follower reach; traffic to Technocore reported up 180× in 20 hours |
| Aug 25, 2026 | Hayes states airdrop allocation will be based on **testnet activity**, and that a token faucet will run through `technocore.chat`, gated to agents holding a DID key |
| Q4 2026 (planned) | FLOP airdrop |
| Q1 2027 (planned) | Genesis block — the chain the token is meant to run on does not exist until this point |

### 2.2 What's confirmed vs. unconfirmed

**Confirmed (from the official X account and repo):**
- No presale, no VC allocation — stated as a "100% fair launch"
- Airdrop is intended for miners, validators, agents, and early community
- `technocore-chat` is a real, running, open-source service (Apache-2.0, `flop-labs/technocore-chat` on GitHub)
- Signed identity uses Ed25519 `did:key` — no resolver, no registry, verification is fully offline

**Not yet published:**
- Whitepaper, token supply, distribution formula
- Named chain / consensus client
- Audit of any kind
- Exact scoring mechanism for "testnet activity"

Treat every downstream step in this plan as provisional on that gap closing. The plan is designed so that the effort invested (a real identity, genuine contributions) has value independent of whether FLOP itself is worth anything, which is the honest hedge against the project not panning out.

### 2.3 Why this might matter beyond the airdrop

Independent of the token, the coordination-layer design is a reasonable pattern for agentic workflows generally:

- **Fetch-only compatibility.** Every write is a plain HTTP GET, so an agent whose sandbox only permits `webfetch` (no socket, no POST) is still a full participant. That's a real constraint many agent harnesses have.
- **Offline signature verification.** Because the identifier *is* the Ed25519 public key (`did:key`), there's no registry or resolver to trust or that can go down — verification is self-contained.
- **Engagement-quality metrics.** The service tracks `zero_response_share` and `nick_diversity` specifically to distinguish genuine multi-agent conversation from a bot talking to itself — a lightweight, general-purpose sybil/spam signal that's cheap to compute and worth borrowing for other agent-coordination contexts.
- **Comparable precedent.** The "fair launch, no VC" pitch echoes Bittensor (TAO), the best-known prior attempt at an incentive-driven AI compute network without an investor round. That doesn't guarantee Flop succeeds, but it means the mechanism design isn't unprecedented.

This is a case for **evaluating** the protocol seriously, not a claim that it will succeed — the gaps in Section 2.2 are real and should weigh against over-investing before more is published.

---

## 3. Objectives

### 3.1 Primary: airdrop eligibility, done legitimately

Given that allocation tracks testnet activity, the highest-value actions are:
- One persistent, real DID — not multiple identities. A fresh identity every session looks identical to spam under the service's own engagement metrics and is more likely to get you filtered out than rewarded.
- Genuine, useful contributions over raw volume of posts.
- Early, correct participation in each new mechanism Flop Labs ships (the faucet, testnet nodes, later phases) — being an early, well-behaved user of new infrastructure is usually worth more than high-frequency shallow activity on old infrastructure.

**Explicitly out of scope for this plan:** running multiple sybil identities, scripting high-frequency low-value posts, or otherwise gaming the engagement metrics. Beyond being against the stated "fair launch" spirit, the service's rate limits (30 writes/min per IP) and quality metrics appear designed to catch exactly this pattern.

### 3.2 Secondary: protocol collaboration

If the primary track goes well and the protocol continues to look sound, the natural extensions are:
- Contributing fixes, tooling, or documentation to `flop-labs/technocore-chat`
- Building and open-sourcing your own tooling on top of it (clients, MCP servers, dashboards) — the repo explicitly invites this ("anyone started an awesome-technocore repo yet?")
- Participating in miner/validator roles once the Proof-of-Useful-Inference client is published, if the economics look reasonable at that time

---

## 4. Current State: What You Can Join Today

Only one first-party repository exists as of this writing:

- **`flop-labs/technocore-chat`** (Apache-2.0) — the coordination service itself. Live at `https://technocore.chat`. Ships an MCP server (`uvx technocore-mcp`) and an installable Agent Skill (`SKILL.md`). This is the one to watch, star, and read `docs/design.md` in.

No official `awesome-technocore` list or SDK repo exists yet — Flop Labs has publicly said they'll link one if the community starts it, which is an opening for Objective 3.2.

**Caution on third-party tools.** Several unofficial sites and repos (browser-based DID generators, NFT-gated "agent hosting" platforms) have appeared claiming to help with onboarding. None are run by Flop Labs. Do not generate or store your private key through any of them — key generation should happen locally, using code you can read, exactly as described in Phase 1 below.

---

## 5. Phased Roadmap

### Phase 0 — Research & Environment Setup *(current phase)*
- Track `@flop_labs` and the upcoming AMA for mechanism details
- Set up local tooling: Claude Code + `technocore-mcp`, Python identity/signing script
- Star and read `flop-labs/technocore-chat`, especially `docs/design.md` and `docs/patterns.md`

### Phase 1 — Signed Identity & Network Access
- Create the `flop-collab` repository under your main GitHub account/org (`zerostate`), seeded with this white paper, `README.md`, and the issue templates from Section 6
- Generate one Ed25519 keypair locally; derive `did:key:z6Mk...`
- Back up the private key material offline, outside any repo
- Post one signed introduction message to the `lobby` room
- **Exit criteria:** `github.com/zerostate/flop-collab` exists and is populated; your DID is visible and verifiable in a public Technocore room

### Phase 2 — Testnet Participation & Contribution
- Claim testnet tokens via the faucet once live (DID-gated, per Hayes' Aug 25 statement)
- Publish at least one genuine contribution (tool, write-up, translation, or code fix) referencing your DID, per the format Flop Labs described
- If a miner/validator client is published, evaluate running one against the stated hardware/economics before committing resources
- **Exit criteria:** documented, DID-linked contribution + testnet activity history

### Phase 3 — Genesis & Claim (Q1 2027 target)
- Confirm claim mechanics once published (which are currently undefined)
- Verify any claim contract/site independently before connecting a wallet — scam sites reliably appear around real airdrops
- Execute the claim
- **Exit criteria:** FLOP claimed to a wallet you control, verified through official channels only

### Phase 4 — Post-Launch Collaboration
- Reassess protocol maturity: is there a whitepaper, audit, real economic activity?
- If yes, contribute upstream (PRs, tooling, an `awesome-technocore` list) or continue as a miner/validator
- If no, treat the airdrop as the end state and deprioritize further investment

---

## 6. Repository & Collaboration Plan

Repo: **`github.com/zerostate/flop-collab`** — created under your main GitHub account/org as part of Phase 1, so this work sits alongside your other public projects from day one rather than in an orphaned personal-tracking repo.

Recommended structure for the repo, which tracks this work, holds this document, and stages future contributions back to `flop-labs/technocore-chat`:

```
flop-collab/
├── docs/
│   └── whitepaper.md          # this document
├── identity/
│   └── (DID public key only — never the private key)
├── .github/ISSUE_TEMPLATE/
│   ├── phase-task.md
│   └── contribution-idea.md
└── README.md
```

**Never commit the private key file** (`~/.technocore/identity.json` or equivalent) to this or any repo, public or private. Only the public DID belongs in version control.

Use GitHub Issues on this repo to track phase progress — one issue per Phase-1/2/3/4 milestone above, plus a running backlog of contribution ideas for Section 3.2. When an idea is ready to become a real contribution, open the PR against `flop-labs/technocore-chat` directly rather than this repo.

---

## 7. Risk Register

| Risk | Likelihood | Notes |
|---|---|---|
| Project is discontinued or airdrop terms change materially | Medium | No binding commitments published yet |
| Token has little or no value at claim | Medium–High | No tokenomics, no exchange listing, purely speculative |
| Private key loss or leak | Low if handled per Phase 1 | Entirely your responsibility — the service holds no keys |
| Third-party "helper" tool compromises your key | Medium | Multiple unofficial tools already circulating; avoid them |
| Effort spent on engagement gaming gets you excluded or banned | N/A if avoided | Explicitly out of scope for this plan |
| Genuine contribution has value even if FLOP doesn't | — | This is the hedge: Phase 2 contributions build real, reusable skills/tools regardless of token outcome |

---

## 8. Appendix — Quick Reference

```bash
# Install MCP server for Claude Code
claude mcp add technocore -- uvx technocore-mcp

# Local identity + signing tool
pip install cryptography base58 requests --break-system-packages
python technocore_identity.py genkey
python technocore_identity.py post lobby "hello technocore"
```

Official manual: `https://technocore.chat/llms.txt`
Official repo: `https://github.com/flop-labs/technocore-chat`
