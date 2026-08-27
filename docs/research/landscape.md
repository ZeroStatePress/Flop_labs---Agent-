# Landscape — Teams Working on Decentralized AI Compute & Inference

*Research compiled 2026-08-27. See [README.md](README.md) for method/source caveats.*

Flop is not entering an empty field. As of mid-2026 the "crypto × AI
compute" sector has operational networks with real revenue; Bittensor alone
is a ~$2.4B token ([Yellow.com](https://yellow.com/news/decentralized-ai-race-bittensor-rivals)).
Grouped by what they actually sell:

## 1. Incentivized intelligence markets (closest to Flop's design)

- **[Bittensor (TAO)](https://bittensor.com)** — the fair-launch
  predecessor Flop most resembles: no VC round, token emissions rewarded to
  subnets producing useful model outputs, scored by validators via Yuma
  Consensus (subjective, stake-weighted). ~$2.4–2.7B market cap, category
  leader ([Yellow research](https://yellow.com/research/bittensor-decentralized-ai-market-2-7-billion),
  [State of Bittensor](https://emoryblockchain.substack.com/p/state-of-bittensor-in-2025)).
- **[Ritual](https://ritual.net)** — AI-native execution layer; verifies
  inference integrity via TEEs or ZK proofs
  ([Equilibrium Labs](https://equilibrium.co/writing/state-of-verifiable-inference)).
- **[Allora](https://allora.network)** — self-improving decentralized
  inference network with peer-scored forecasts (same subjective-scoring
  family as Bittensor).

## 2. Verifiable / decentralized training & compute protocols

- **[Gensyn](https://gensyn.ai)** — a16z-backed ($43M Series A) trustless
  compute protocol: cryptographic verification that off-chain training jobs
  ran correctly; token launched 2026
  ([Yellow.com](https://yellow.com/news/is-gensyn-next-decentralized-ai-trade)).
- **[Prime Intellect](https://primeintellect.ai)** — decentralized training
  runs across pooled global GPUs (INTELLECT model series); open
  infrastructure for distributed RL/training
  ([KuCoin overview of 2026 training models](https://www.kucoin.com/blog/How-AI-crypto-tokens-power-4-decentralized-training-models-in-2026)).
- **[Nous Research](https://nousresearch.com)** — open-model lab whose
  Psyche network does decentralized training over the internet (DisTrO
  optimizers).
- **[Pluralis Research](https://pluralis.ai)** — "protocol learning":
  collaboratively trained models where no single party holds the full
  weights.

## 3. GPU / compute marketplaces (DePIN — sell raw capacity, not consensus)

- **[Akash Network (AKT)](https://akash.network)** — decentralized cloud
  marketplace; record ~$5M quarterly compute spend, practical overflow
  capacity during GPU crunches ([KuCoin](https://www.kucoin.com/blog/ai-compute-crypto-depin-narrative)).
- **[io.net (IO)](https://io.net)** — aggregates independent data-center
  cards into virtual clusters ("rent ~1,000 H100s as one machine")
  ([HOGE Wire](https://hoge.gg/decentralized-inference-crypto-gpu-networks-2026/)).
- **[Render Network (RNDR/RENDER)](https://rendernetwork.com)** — GPU
  rendering marketplace expanded into AI inference; >$1.5B market cap.
- **[Golem (GLM)](https://golem.network/ai)** — the 2016 original
  off-chain compute market; now runs AI workloads.
- **[Flux / FluxEdge](https://fluxofficial.medium.com/flux-proof-of-useful-work-utility-in-ai-0d115c0cd035)** —
  live Proof-of-Useful-Work pivot; FluxEdge is a decentralized GPU
  marketplace for AI/ML ([DePIN Hub](https://depinhub.io/projects/flux/)).

## 4. Useful survey material

- [Reflexivity Research — Overview of Decentralized Compute](https://www.reflexivityresearch.com/free-reports/overview-of-decentralized-compute)
- [Equilibrium Labs — State of Verifiable Inference](https://equilibrium.co/writing/state-of-verifiable-inference)
- [Yellow — AI Compute Demand vs Crypto GPU Networks (2026)](https://yellow.com/research/ai-compute-demand-crypto-gpu-networks-gap-2026)
- [KuCoin — AI Compute + Crypto: The Next $10B Narrative?](https://www.kucoin.com/blog/ai-compute-crypto-depin-narrative)
- Academic: [Proofs of Useful Work (Ball et al.)](https://eprint.iacr.org/2017/203.pdf) ·
  [Challenges of PoUW](https://www.researchgate.net/publication/363402495_Challenges_of_Proof-of-Useful-Work_PoUW) ·
  [Replacing cryptopuzzles with useful computation](https://arxiv.org/pdf/2404.15735) ·
  [Cost-aware PoQ for decentralized LLM inference](https://arxiv.org/pdf/2512.16317) ·
  [HadAgent: proof-of-inference consensus for agent serving](https://arxiv.org/pdf/2604.18614)

## 5. Where Flop would sit

Flop's differentiators, if delivered: (a) agents as the *native customer*
(vs. human devs renting GPUs), (b) inference fees fused with block rewards
into one consensus mechanism, (c) a Bittensor-style fair launch with a
Hayes-scale distribution reach. Its burden of proof: a verification story
none of the above have fully cracked, against incumbents that already have
years of production history and liquidity.
