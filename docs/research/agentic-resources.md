# Agentic Resources — Infrastructure Useful to This Project

*Research compiled 2026-08-27. See [README.md](README.md) for method/source caveats.*

Resources for building, identifying, and paying autonomous agents —
relevant both to Technocore participation and to any contribution we build
(whitepaper §3.2).

## 1. Technocore-specific tooling

- **[flop-labs/technocore-chat](https://github.com/flop-labs/technocore-chat)** —
  the service itself (Apache-2.0). Read `docs/design.md`, `PATTERNS.md`
  (E2E, mailboxes, key passing), `INTEROP.md` (ActivityPub / Matrix /
  WebSub / JSON-RPC bridges).
- **`uvx technocore-mcp`** — official MCP server, nine tools; install into
  Claude Code with `claude mcp add technocore -- uvx technocore-mcp`.
- **Agent Skill** — `SKILL.md` in the repo, served at
  `technocore.chat/skill.md`; installable on Claude.
- **Discovery endpoints** — `/openapi.json`, `/.well-known/agent.json`,
  `/.well-known/api-catalog`, manual at `/llms.txt`.
- **[zunmax/technocore-did-starter](https://github.com/zunmax/technocore-did-starter)** —
  community tutorial for encrypted Ed25519 DID + signed messages +
  contribution logging. Read it as reference; generate keys only with code
  you've audited (our issue #6).
- ⚠️ **Avoid custodial helpers** — [Flop Delegate](https://flopdelegate.com/)
  (platform holds your agent's keypair) and browser-based DID generators.
  A DID whose private key someone else generated is not your identity.

## 2. Agent identity standards

- **[did:key method](https://w3c-ccg.github.io/did-key-spec/)** — the
  self-contained DID method Technocore uses: the identifier encodes the
  Ed25519 public key itself; verification needs no registry or resolver.
- **[W3C DID Core](https://www.w3.org/TR/did-core/)** and
  **[W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/)** —
  the broader identity stack if agent credentials become relevant.
- **[/.well-known/agent.json](https://github.com/flop-labs/technocore-chat)** —
  agent-card discovery pattern (as used by A2A-style protocols).

## 3. Agent payments — the rails Flop wants to compete with/complement

- **[x402](https://www.x402.org/)** — open HTTP-402 payment standard for
  machine-to-machine payments; 50M+ M2M transactions processed; foundation
  members include Google, Visa, AWS, Circle, Anthropic, Vercel
  ([Coinbase research](https://www.coinbase.com/institutional/research-insights/research/market-intelligence/picks-and-shovels-of-the-ai-agent-economy),
  [The Agent Report](https://the-agent-report.com/2026/06/coinbase-mcp-agent-integration/)).
  Directly relevant: Technocore is HTTP-GET-native, and x402 is the
  emerging way HTTP services charge agents.
- **[Coinbase AgentKit + Agentic Wallets](https://www.coinbase.com/developer-platform)** —
  wallet infrastructure for non-human actors (launched Feb 11, 2026):
  gasless transactions on Base, programmable skills; plus MCP-compatible
  products (Payments MCP, Base MCP, Coinbase for Agents)
  ([Autheo overview](https://www.autheo.com/signals/coinbase-ai-agents-future-crypto-april-2026)).
- **[The Agent Payments Stack](https://agentpaymentsstack.com/)** — living
  directory of 100+ projects across 6 layers of agent-payment
  infrastructure; good map of the space.

## 4. Agent frameworks (for building a contribution)

- **[Model Context Protocol (MCP)](https://modelcontextprotocol.io)** — the
  tool-interface standard; Technocore already ships an MCP server, and an
  improved/extended one is a plausible upstream contribution.
- **[ElizaOS](https://github.com/elizaOS/eliza)** — dominant open-source
  framework for crypto-native agents ([CoinGape roundup](https://coingape.com/best-web3-ai-agent-frameworks/)).
- **[Olas (Autonolas)](https://olas.network)** — co-owned autonomous
  services/agent economies.
- **[Virtuals Protocol](https://virtuals.io)** — agent launch/ownership
  platform; ~1.78M agent-completed jobs reported by Feb 2026
  ([Coinbase research](https://www.coinbase.com/institutional/research-insights/research/market-intelligence/picks-and-shovels-of-the-ai-agent-economy)).
- **[Fetch.ai uAgents](https://github.com/fetchai/uAgents)**,
  [Swarms](https://github.com/kyegomez/swarms), Daydreams, Pippin — other
  agent-to-agent frameworks in active use
  ([CoinGape](https://coingape.com/best-web3-ai-agent-frameworks/)).

## 5. Concrete contribution openings (feeds issue #10)

1. **`awesome-technocore`** — still doesn't exist (verified 2026-08-27);
   Flop Labs has said they'd link a community-started one.
2. **A hardened, auditable `technocore_identity.py`** (issue #6) —
   published openly, it doubles as the safe alternative to the custodial
   key generators circulating.
3. **x402 ↔ Technocore bridge note or prototype** — how a GET-only
   coordination layer meets the emerging HTTP payment standard.
4. **A technical write-up** comparing Proof-of-Useful-Inference to the
   verifiable-inference approaches in
   [`bitcoin-comparison.md` §3](bitcoin-comparison.md) — timely once the
   whitepaper drops.
