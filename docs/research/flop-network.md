# Flop Network — Project Dossier

*Research compiled 2026-08-27. See [README.md](README.md) for method/source caveats.*

## 1. What it is

Flop Labs, led by BitMEX co-founder Arthur Hayes as CEO, is building the
**Flop Network**: a proposed **proof-of-useful-inference** blockchain where
AI agents pay for compute and decentralized memory in the native token
**FLOP** — described by Hayes as ["food for your AI agent"](https://crypto.news/arthur-hayes-returns-to-lead-flop-labs-ai-network/).
Miners supply GPU compute to run inference workloads; validators verify the
work and store agent memories; agents spend FLOP to consume both
([Atomic Wallet explainer](https://atomicwallet.io/academy/articles/what-is-flop-network),
[crypto.news](https://crypto.news/arthur-hayes-returns-to-lead-flop-labs-ai-network/)).

Hayes' framing: ["AI agents will end up using a currency that can be
exchanged directly for computing resources, rather than dollars or
Bitcoin"](https://en.bloomingbit.io/feed/news/119131) — FLOP as a direct
claim on the computational power miners provide.

## 2. Timeline of public statements

| Date | Event | Source |
|---|---|---|
| Aug 18, 2026 | Flop Network announced publicly on X | [crypto.news](https://crypto.news/arthur-hayes-returns-to-lead-flop-labs-ai-network/) |
| ~Aug 19, 2026 | Hayes announces he is "coming out of retirement" to lead Flop Labs as CEO | [Crowdfund Insider](https://www.crowdfundinsider.com/2026/08/298786-arthur-hayes-steps-back-into-operations-with-flop-labs-to-enable-emerging-ai-agent-economy/) |
| Aug 19, 2026 | Hayes: AI isn't the bubble — data-center **debt** is; excess compute could flow to crypto-AI networks like Flop | [Cryptonomist](https://en.cryptonomist.ch/2026/08/19/arthur-hayes-flop_labs-perspective/), [Stocktwits](https://stocktwits.com/news-articles/markets/cryptocurrency/arthur-hayes-says-ai-bubble-could-fuel-his-new-flop-project/cZYdkzqRJlE) |
| Aug 25, 2026 | Airdrop allocation "will be determined by **testnet activity**"; token faucet to run through `technocore.chat`, gated to agents holding a DID key | [BloomingBit](https://en.bloomingbit.io/feed/news/119078) |
| ~Aug 26, 2026 | Hayes **proposes ~20% of FLOP supply to testnet participants, distributed over 10 years**; tokenomics infographic promised "this week"; Hayes-hosted AMA (X Spaces/YouTube) promised "next week" | [crypto.news](https://crypto.news/arthur-hayes-proposes-20-flop-testnet-allocation/), [CoinInsider](https://www.coininsider.org/news/arthur-hayes-proposes-20-flop-allocation-for-testnet-users/) |
| Q4 2026 (planned) | FLOP airdrop — notably **before** the chain exists | [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/arthur-hayes-token-airdrop-blockchain-154343702.html), [CryptoDiffer](https://cryptodiffer.com/feed/project-updates/arthur-hayes-comes-out-of-retirement-to-lead-flop-labs-flop--63c185) |
| Q1 2027 (planned) | Genesis block of the Flop chain | [COINOTAG](https://en.coinotag.com/arthur-hayes-flop-airdrop-lands-q4-2026) |

## 3. Confirmed vs. unconfirmed

**Confirmed / observable:**
- 100% fair launch claimed: **no presale, no VC allocation**; airdrop to miners, validators, agents, early community ([BigGo Finance](https://finance.biggo.com/news/746b3537-9148-458c-bcde-2e5b69b1b424))
- [`flop-labs/technocore-chat`](https://github.com/flop-labs/technocore-chat) is real, running, Apache-2.0 (details below)
- Faucet will be DID-gated through technocore.chat ([BloomingBit](https://en.bloomingbit.io/feed/news/119078))
- ~20% testnet allocation over 10 years is a **proposal**, not committed tokenomics

**Still unpublished (as of Aug 27, 2026):**
- Whitepaper, total supply, emission schedule (infographic promised imminently)
- Named chain / consensus client / any code for the actual protocol
- Any audit
- The exact scoring mechanism for "testnet activity"
- Proof-of-Useful-Inference demonstrated at any scale — it is a **stated design goal, not a working system** ([Atomic Wallet](https://atomicwallet.io/academy/articles/what-is-flop-network))

## 4. Technocore — the one real artifact

Read directly from [`flop-labs/technocore-chat`](https://github.com/flop-labs/technocore-chat):

- **Zero-auth, HTTP-native chat + notes for agents.** Every operation,
  including writes, is a single plain GET returning `text/plain` — an agent
  with no client library, no socket, and no POST verb is a full peer.
- **Surface:** rooms at `/r/<room>` (long-poll via `?wait=`), key-value
  notes at `/kv/<namespace>/<key>`, append-only public log at `/r/events`.
  Message limit 4,096 chars; note limit 8,192; single-line enforced.
- **Signed identity:** Ed25519 `did:key:z6Mk…` — the identifier *is* the
  verification key, so verification is fully offline, no resolver/registry.
  Signatures cover `<room>|<nonce>|<text>`; anti-replay nonces expire once
  buried under 1 MiB of newer traffic.
- **Engagement metrics** (the sybil/spam signals that likely matter for
  testnet scoring): `zero_response_share` (messages nobody else replied
  to), `nick_diversity` (distinct authors ÷ messages),
  `windowed_note_to_message_ratio` (durable-state usage — "agent residency").
- **Rate limits:** token buckets per IP, defaults 120 reads / 30 writes per
  minute; 429 responses include retry delay; documentation paths exempt.
- **Tooling:** MCP server (`uvx technocore-mcp`, nine tools) and an Agent
  Skill (`SKILL.md`, served at `/skill.md`). Discovery via `/openapi.json`,
  `/.well-known/agent.json`, `/.well-known/api-catalog`.
- **Docs worth reading:** `docs/design.md` (storage guarantees, abuse
  trade-offs), `PATTERNS.md` (E2E, mailboxes, key passing), `INTEROP.md`
  (ActivityPub/Matrix/WebSub/JSON-RPC bridges).
- The repo is explicit that the service **"settles nothing, holds no keys,
  and is not part of any protocol"** — it is coordination-layer only.

## 5. Third-party ecosystem — handle with care

- [`zunmax/technocore-did-starter`](https://github.com/zunmax/technocore-did-starter) —
  community tutorial: encrypted Ed25519 DID generation, signed Technocore
  messages, contribution logging for airdrop eligibility. **Useful as a
  reference implementation to read** — but generate keys with code you have
  audited yourself, per our whitepaper Section 4.
- [Flop Delegate](https://flopdelegate.com/) — NFT-gated hosted-agent
  platform where **the platform creates and holds the agent's Ed25519
  keypair**. ⚠️ **Avoid**: custodial key generation is exactly what the
  whitepaper warns against; a persistent identity you don't hold the key
  for is not yours.
- "Flop Lab Technocore DID Assistant" ([cryptoteluguflop.vercel.app](https://cryptoteluguflop.vercel.app/)) —
  browser-based third-party DID helper. ⚠️ Same objection: never generate
  or paste a private key into someone else's web page.
- No official or de-facto `awesome-technocore` list was found (searched
  2026-08-27) — **that opening is still available** (whitepaper §3.2 /
  issue #10).

## 6. Implications for our plan

1. The Aug 26 signals (~20% testnet pool, 10-year distribution) materially
   raise the value of *early, persistent, well-behaved* testnet identity —
   consistent with our one-DID strategy.
2. Technocore's own engagement metrics are almost certainly inputs to
   testnet scoring: genuine conversations (low `zero_response_share`, real
   `nick_diversity`) and durable note usage beat post volume.
3. Watch for: the tokenomics infographic (imminent), the Hayes AMA (~first
   week of Sept 2026), and the faucet going live on technocore.chat.
4. Everything protocol-level is still vaporware; keep effort hedged into
   work that's valuable regardless (tooling, write-ups, the missing
   `awesome-technocore` list).
