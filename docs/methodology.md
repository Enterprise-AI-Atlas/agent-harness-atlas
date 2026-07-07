# Methodology

## Inclusion criteria

A harness is included if it directly runs agents: manages their lifecycle, dispatches tool calls, handles state, and returns results. The strict core includes general-purpose agent frameworks, coding-agent runtimes, and evaluation/standards harnesses that act as runtimes.

## Exclusion criteria

- Pure model providers (no agent orchestration)
- Pure vector databases or embedding stores
- Static chat UI apps without a programmable harness
- Benchmarks without an execution harness

## Dimensions

Each column in `data/agent-harness-matrix.csv` is defined in [`glossary.md`](glossary.md). Values are chosen from a controlled vocabulary; multiple values are joined with `+`. `unknown` is used when evidence is missing.

## Evidence and confidence

Confidence levels are tracked in `data/confidence.csv` keyed by `name`:

- `high`: docs and code were inspected directly
- `medium`: docs or public demos reviewed, no code inspected
- `low`: secondary sources only (blog posts, conference talks, release notes)

## Contribution rules

1. Add a row to `data/agent-harness-matrix.csv`.
2. Add a matching `frameworks/<name>.md` profile.
3. If confidence is not `high`, add or update `data/confidence.csv`.
