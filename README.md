# Agent Harness Atlas

A vendor-neutral atlas that decomposes how 50–100 agent harnesses work.

The core artifact is [`data/agent-harness-matrix.csv`](data/agent-harness-matrix.csv), a comparison matrix of agent frameworks, coding runtimes, and related harnesses. Supporting prose in [`docs/`](docs/) explains what they share and where they diverge. [`frameworks/`](frameworks/) holds a one-page profile for each included harness.

## Quick links

- [Comparison matrix (CSV)](data/agent-harness-matrix.csv)
- [Methodology](docs/methodology.md)
- [Common patterns](docs/common-patterns.md)
- [Dissimilarities](docs/dissimilarities.md)
- [Glossary](docs/glossary.md)

## Initial findings (work in progress)

1. Most harnesses share the same core loop: receive input → call LLM → parse tool intent → execute tool → feed result back into context.
2. The biggest architectural forks are orchestration model (state machine vs. DAG vs. event-driven) and memory model (conversation-only vs. persistent shared state).
3. Tool binding is converging on native tool calling + MCP, but A2A support is still rare.
4. Production-grade guardrails and human-in-the-loop primitives remain unevenly distributed.

## Contributing

Every new row in `data/agent-harness-matrix.csv` must be paired with a `frameworks/<name>.md` profile. See [`docs/methodology.md`](docs/methodology.md) for inclusion criteria.
