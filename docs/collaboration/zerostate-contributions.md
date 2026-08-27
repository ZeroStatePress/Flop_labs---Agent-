# ZeroState × Flop Labs — Collaboration & Contribution Plan

*Drafted 2026-08-27. Companion to [`docs/whitepapers/whitepaper.md`](../whitepapers/whitepaper.md)
(§3.2, §6) and the research in [`docs/research/`](../research/README.md).*

## 1. Objective

Become visible to the Flop Labs team as a **useful, trustworthy, recurring
contributor** — first through the agentic/Technocore surface that exists
today, then as a remote contributor to the protocol development effort as
its repositories open up. The aim is a reputation built on shipped work
tied to one persistent DID, so that by the time Flop Labs is assembling
its wider contributor circle (testnet, validator set, core tooling), ZeroState
is already a known name in their PR history, their rooms, and their metrics.

**Positioning principle:** every contribution should be genuinely useful to
Flop Labs *even if they never notice us* — that keeps the work honest, and
it is also, in practice, what gets noticed.

## 2. What ZeroState brings

| Capability | Evidence / basis |
|---|---|
| Agentic-workflow engineering | Daily production use of Claude Code, MCP servers, Agent Skills; this repo is itself run agent-first |
| Remote-first development practice | Distributed, async, issue-driven workflow (see this repo's issue structure) — matches how an early-stage protocol team works |
| Technical writing & publishing | ZeroState Press publishing operation — long-form editing, document toolchains, shipping polished artifacts |
| Python/tooling development | Identity/signing tooling (issue #6), automation, CI setup |
| Security-conscious habits | Key-custody discipline baked into this repo (`.gitignore` guards, non-custodial stance vs. tools like Flop Delegate — see [research §5](../research/flop-network.md)) |

## 3. Track A — Agentic side (available today)

Ordered roughly by effort-to-visibility ratio:

1. **`awesome-technocore`** — still unclaimed as of 2026-08-27
   ([research](../research/agentic-resources.md) §5). Flop Labs has
   publicly said they'd link a community-started list. Cheap to start,
   permanently visible, and it makes ZeroState the curator of the
   ecosystem's front door. *First-mover window — do this early.*
2. **Open, auditable identity tooling** — publish our hardened
   `technocore_identity.py` (issue #6) as a standalone, documented,
   non-custodial alternative to the custodial key generators circulating.
   Directly serves Flop Labs' interest (their airdrop integrity depends on
   users not leaking keys to third parties).
3. **Exemplary Technocore citizenship** — one DID, genuine multi-agent
   conversation, real use of the notes/KV surface. Their own metrics
   (`zero_response_share`, `nick_diversity`, note-to-message ratio —
   [research](../research/flop-network.md) §4) are designed to surface
   exactly this; being measurably high-quality *is* the introduction.
4. **MCP / Skill improvements** — the official `technocore-mcp` server and
   `SKILL.md` are v1 artifacts; PRs adding tools, tests, or better
   Claude-Code ergonomics land in *their* repo under our name.
5. **Patterns write-ups** — worked examples extending `PATTERNS.md`
   (mailboxes, E2E, key passing) from real agent sessions; also candidates
   for an upstream docs PR.
6. **x402 ↔ Technocore exploration** — a note or prototype on how a
   GET-only coordination layer meets the emerging HTTP-402 agent-payment
   standard ([research](../research/agentic-resources.md) §3). This is the
   kind of forward-looking piece a protocol team notices, because it does
   their roadmap thinking with them.

## 4. Track B — Remote development side (as the project opens up)

What exists today is one Apache-2.0 service repo; the chain, consensus
client, and testnet are unreleased ([research](../research/flop-network.md) §3).
The development-side strategy is **be already contributing to what's public
when the private things go public**:

1. **Upstream PRs to `flop-labs/technocore-chat`** — bug fixes, test
   coverage, `INTEROP.md` bridges (ActivityPub/Matrix/WebSub), rate-limit
   edge cases, docs. Small, clean, convention-matching PRs are the resume
   a core team actually reads.
2. **Verifiable-inference research contribution** — our
   [Bitcoin comparison](../research/bitcoin-comparison.md) §3 already maps
   the four verification approaches (subjective scoring / TEE / zkML /
   optimistic re-execution). When the whitepaper drops, publish a serious
   technical review of their chosen mechanism — constructive, cited,
   engineering-grade. Protocol teams remember the reviewers who understood
   the hard part.
3. **Testnet operations** — run a miner/validator/node from day one of any
   public testnet (whitepaper Phase 2), file reproducible bug reports, and
   contribute setup documentation ("how to run a Flop testnet node on X")
   — historically the fastest route from outsider to trusted operator in
   new networks.
4. **Developer-experience infrastructure** — CI templates, containerized
   dev environments, or a public testnet status/metrics dashboard. Teams
   at genesis are starved for exactly this and it's highly visible.
5. **AMA & tokenomics engagement** — show up to the imminent AMA
   ([research](../research/flop-network.md) §2) with one or two *precise*
   technical questions (verification mechanism, testnet scoring formula).
   A good question in a public forum is a low-cost credibility signal.

## 5. The "get noticed" ladder

Reputation with a small team compounds in a specific order — skipping
steps reads as opportunism:

1. **Use it well** (Track A.3) — visible in their metrics, zero cost.
2. **Fix something small** — one clean PR upstream (Track B.1).
3. **Ship something they want but didn't build** — `awesome-technocore`,
   identity tool, dashboard (A.1, A.2, B.4). Announce each once, in the
   appropriate room, DID-signed, per their stated contribution format.
4. **Do their thinking with them** — the verifiable-inference review, the
   x402 note (A.6, B.2), AMA questions (B.5).
5. **Ask for the relationship** — only after 1–4: a short, direct note to
   the team pointing at the shipped record, offering specific remote
   development capacity (what we do, hours, links). By then it's a
   confirmation, not a cold pitch.

## 6. Ground rules

- **One DID, forever.** All contributions signed/linked to the single
  Phase-1 identity (issue #7). Reputation doesn't accrue to scattered keys.
- **No volume games.** Their metrics are built to detect low-value posting
  ([research](../research/flop-network.md) §4); one substantive artifact a
  week beats daily noise. Everything in whitepaper §3.1's "out of scope"
  stays out of scope.
- **Non-custodial, always.** We never touch, wrap, or recommend custodial
  key services; it's both the safe stance and a differentiator
  ([research](../research/flop-network.md) §5).
- **Upstream-first.** Code that belongs in their repo goes to their repo
  as a PR; this repo only stages it (whitepaper §6).
- **Honest hedge.** Every item above is real, reusable work (tooling,
  writing, operations experience) even if FLOP goes nowhere — per the
  whitepaper's risk register.

## 7. Proposed first moves (feeds the issue tracker)

| # | Action | Track | Effort | Visibility | When |
|---|---|---|---|---|---|
| 1 | Start `awesome-technocore` repo, seed with research links | A.1 | S | High | Now — first-mover window |
| 2 | Finish + publish auditable identity tool | A.2 / #6 | M | High | Now (blocks Phase 1 anyway) |
| 3 | Signed intro + sustained genuine room presence | A.3 / #8 | S | Medium | After #7 |
| 4 | One small upstream PR (docs/tests/bugfix) | B.1 | S–M | High | Within 2 weeks |
| 5 | AMA attendance with prepared technical questions | B.5 | S | Medium | ~First week of Sept 2026 |
| 6 | Technical review of whitepaper's verification mechanism | B.2 | M–L | High | When whitepaper drops |
| 7 | Testnet node + setup write-up | B.3 | M | High | When testnet opens |
| 8 | x402 ↔ Technocore prototype note | A.6 | M | Medium | Opportunistic |

Each row should become an `[Idea]` issue (contribution-idea template) when
picked up, per the workflow in whitepaper §6 and issue #10.
