# SWE-bench Harness

## What it is
The execution harness behind SWE-bench, the industry-standard benchmark for evaluating coding agents on real GitHub issues.

## Distinctive traits
- Containerized sandbox execution for safety and reproducibility.
- Compares agent patches against real test suites.
- Not a framework, but a runtime that drives agent execution.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| swe-bench-harness | SWE-bench | Python | MIT | eval-harness | plugin-api | none | none | none | logging | sandboxing | container | stable |

## Key links
- Repo: https://github.com/swe-bench/SWE-bench
- Docs: https://www.swebench.com/
