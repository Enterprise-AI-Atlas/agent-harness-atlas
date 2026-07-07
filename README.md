# Agent Harness Atlas

Every "agent framework" promises the same thing, but under the hood they make very different choices about memory, orchestration, guardrails, and how humans stay in the loop. This repo is an attempt to cut through the marketing and compare them directly.

The main artifact is [`data/agent-harness-matrix.csv`](data/agent-harness-matrix.csv): a comparison of **72** agent frameworks, coding agents, orchestration layers, and evaluation harnesses. The [`docs/`](docs/) folder explains what most of them have in common and where they genuinely diverge. [`frameworks/`](frameworks/) has a short profile for every harness in the matrix.

## Quick links

- [Comparison matrix (CSV)](data/agent-harness-matrix.csv)
- [Methodology](docs/methodology.md)
- [Common patterns](docs/common-patterns.md)
- [Dissimilarities](docs/dissimilarities.md)
- [Glossary](docs/glossary.md)

## Findings at a glance

- **72 harnesses** across general-purpose frameworks, coding CLIs/IDE agents, enterprise automation platforms, and evaluation harnesses.
- **Turn-based orchestration is the majority**: 32 of 72 harnesses let the LLM drive step-by-step.
- **DAG and state-machine** harnesses (19 combined) are stronger for long-running, auditable workflows.
- **Conversation-only memory dominates**: 40 of 72; persistent state is the key differentiator for multi-session or resumable agents.
- **Multi-agent primitives are still niche**: 49 harnesses have no built-in multi-agent support.
- **Approvals are common, breakpoints are rare**: 21 harnesses support approvals; only 1 lists breakpoints.
- **Guardrails are uneven**: 45 harnesses list no built-in guardrails; sandboxing is concentrated in eval and coding harnesses.
- **Open source leads**: 58 open-source (MIT or Apache-2.0) vs. 13 proprietary, mostly in coding assistants and cloud platforms.

## Repository structure

```
agent-harness-atlas/
├── data/
│   ├── agent-harness-matrix.csv   # Canonical comparison matrix
│   └── confidence.csv             # Per-row confidence and evidence type
├── docs/
│   ├── methodology.md             # Inclusion/exclusion criteria and contribution rules
│   ├── common-patterns.md         # What most harnesses share
│   ├── dissimilarities.md         # Major architectural forks and outliers
│   └── glossary.md                # Controlled vocabulary definitions
├── frameworks/
│   ├── autogen.md                 # One-page profile per harness
│   ├── langchain-langgraph.md
│   └── ...                        # 72 profiles total
└── scripts/
    └── validate.py                # Validate CSV + profile consistency
```

## Validation

```bash
python scripts/validate.py
```

Expected output: `OK: 72 rows, all profiles present, all values valid.`

## Contributing

Every new row in `data/agent-harness-matrix.csv` must be paired with a `frameworks/<name>.md` profile and a `data/confidence.csv` entry. See [`docs/methodology.md`](docs/methodology.md) for inclusion criteria and the controlled vocabulary.
