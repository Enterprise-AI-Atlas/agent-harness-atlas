# Dagger Agents

## What it is
Dagger's approach to running agents inside programmable pipelines. Agents are Dagger functions that can call other functions and LLMs.

## Distinctive traits
- Agents execute as containerized Dagger functions.
- DAG-based execution with caching and reproducibility.
- Strong fit for CI-like and automation use cases.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| dagger-agents | Dagger | Go+Python | Apache-2.0 | dag | native-tool-calling | conversation-only | none | none | tracing+logging | none | library | experimental |

## Key links
- Repo: https://github.com/dagger/dagger
- Docs: https://docs.dagger.io/
