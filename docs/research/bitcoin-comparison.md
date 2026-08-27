# "Bitcoin, but the work is compute" — Flop vs. Proof-of-Work

*Research compiled 2026-08-27. See [README.md](README.md) for method/source caveats.*

## 1. The core analogy

Flop's pitch is structurally a Bitcoin fork of *ideas*: keep the fair-launch
monetary design and miner incentive loop, but replace the "useless" work
(SHA-256 hashing) with work someone actually wants — AI inference.

| Dimension | Bitcoin | Flop Network (as proposed) |
|---|---|---|
| Work performed | SHA-256 partial-preimage puzzles | AI inference: "a specified number of FLOPs within a set time frame using a particular AI model" ([Blockonomi](https://blockonomi.com/arthur-hayes-proposes-flop-token-plan-for-ai-computing-network)) |
| Usefulness of work | None beyond securing the chain | The work *is* the product — inference an agent requested and paid for |
| Miner revenue | Block rewards + transaction fees | **FLOP block rewards + FLOP inference fees** ([Blockonomi](https://blockonomi.com/arthur-hayes-proposes-flop-token-plan-for-ai-computing-network)) |
| Who consumes the resource | N/A (security is the output) | AI agents, paying FLOP for compute + decentralized memory |
| Validators | Full nodes verify cheap-to-check hashes | Validators "verify the work and store agent memories" — verification is the hard, unsolved part (see §3) |
| Launch model | No premine, no presale — genesis 2009 | Claimed "100% fair launch": no presale, no VC allocation ([BigGo Finance](https://finance.biggo.com/news/746b3537-9148-458c-bcde-2e5b69b1b424)) |
| Distribution to early participants | Early CPU miners earned outsized share | ~20% of supply proposed for testnet participants, over 10 years ([crypto.news](https://crypto.news/arthur-hayes-proposes-20-flop-testnet-allocation/)) |
| Monetary metaphor | "Digital gold" — energy converted to scarcity | "Food for AI agents" — a currency redeemable directly for compute ([bloomingbit](https://en.bloomingbit.io/feed/news/119131)) |
| Status | 17 years of production history | No chain, no whitepaper, no testnet yet — airdrop planned **before** genesis ([Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/arthur-hayes-token-airdrop-blockchain-154343702.html)) |

The key inversion: in Bitcoin, energy is burned to make the ledger
expensive to rewrite. In Flop's design, the same incentive plumbing is
aimed at a *market* — the security budget and the compute marketplace are
supposed to be the same flow of money. That's elegant if it works, and it's
exactly the coupling that has broken every prior attempt (see §3).

## 2. Hayes' macro thesis behind it

- The AI bubble, per Hayes, is not the technology but the **debt financing
  of data centers** — capital-intensive, long-lived assets that are
  economically real estate dressed as tech
  ([Cryptonomist](https://en.cryptonomist.ch/2026/08/19/arthur-hayes-flop_labs-perspective/)).
- When that over-built capacity seeks yield, a permissionless compute
  market denominated in its own token is positioned as the buyer of last
  resort — "excess compute capacity might eventually benefit crypto-AI
  projects, like Flop Labs"
  ([Stocktwits](https://stocktwits.com/news-articles/markets/cryptocurrency/arthur-hayes-says-ai-bubble-could-fuel-his-new-flop-project/cZYdkzqRJlE)).
- Agents, not humans, are the intended economic actors: "AI agents will end
  up using a currency that can be exchanged directly for computing
  resources, rather than dollars or Bitcoin"
  ([bloomingbit](https://en.bloomingbit.io/feed/news/119131)).

## 3. Prior art: proof-of-useful-work has been tried

Flop is entering a lineage with a consistent failure mode — **useful work
is hard to verify cheaply and hard to bind to consensus**:

- **[Primecoin (2013)](https://bitcoinmagazine.com/business/primecoin-the-cryptocurrency-whose-mining-is-actually-useful-1373298534)** —
  miners search for prime-number chains (Cunningham chains). Worked because
  primality is cheap to verify; but the "usefulness" was marginal.
- **Permacoin (2014)** — mining redirected to distributed archival storage.
- **[Ball, Rosen & Sabin — "Proofs of Useful Work" (2017)](https://eprint.iacr.org/2017/203.pdf)** —
  the theoretical formalization (orthogonal-vectors problems); later work
  applied NP-hard optimization (Ofelimos, Chrisimos) and ML training
  (Coin.AI, PoGO with quantized gradients + Merkle proofs) — survey in
  ["Challenges of Proof-of-Useful-Work"](https://www.researchgate.net/publication/363402495_Challenges_of_Proof-of-Useful-Work_PoUW)
  and [arXiv:2404.15735](https://arxiv.org/pdf/2404.15735).
- **[Flux / FluxEdge](https://fluxofficial.medium.com/flux-proof-of-useful-work-utility-in-ai-0d115c0cd035)** —
  a live "PoUW for AI" pivot of an existing GPU DePIN.
- **[Golem](https://golem.network/ai)** — the 2016-era off-chain compute
  marketplace: computation off-chain, only bookkeeping on-chain — the
  pattern most "compute coins" eventually retreat to.

**The open problem Flop must solve — verifiable inference.** How does a
validator know a miner honestly ran *the model it claims* on *the input it
was paid for*?
Current approaches, per [Equilibrium Labs' "State of Verifiable Inference"](https://equilibrium.co/writing/state-of-verifiable-inference):

1. **Subjective/economic scoring** — Bittensor's Yuma Consensus: validators
   score miner outputs, stake-weighted. Works, but consensus is
   fundamentally subjective and gameable.
2. **TEEs** (e.g. Ritual's approach) — cheap, but imports hardware trust
   assumptions (Intel/NVIDIA attestation).
3. **ZK proofs of inference (zkML)** — trustless, but "prohibitively
   expensive" for large models today.
4. **Optimistic/re-execution sampling** (Gensyn-style) — verify a random
   subset, slash cheaters.

Flop has not yet said which of these (or what new mechanism)
Proof-of-Useful-Inference uses. **This is the single most important thing
to look for in the whitepaper/AMA** — it determines whether "Bitcoin for
compute" is an architecture or a slogan.

## 4. Honest differences from Bitcoin to keep in mind

- Bitcoin's work is *permissionless and interchangeable*; inference demand
  is bursty, heterogeneous (models, latency, memory), and requires matching
  — a marketplace problem PoW never had.
- Bitcoin never needed demand for its work product; Flop's security budget
  collapses if agent demand for inference doesn't materialize.
- "Airdrop before the chain exists" (Q4 2026 vs Q1 2027 genesis) has no
  Bitcoin analogue — allocation happens off-chain, on trust in Flop Labs
  ([Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/arthur-hayes-token-airdrop-blockchain-154343702.html)).
- Fair-launch precedent in this niche is **Bittensor (TAO)** — no VC round,
  emissions to useful work — currently ~$2.4B market cap and the category
  leader ([Yellow.com](https://yellow.com/news/decentralized-ai-race-bittensor-rivals)),
  which is both validation of the model and Flop's most direct competitor.
