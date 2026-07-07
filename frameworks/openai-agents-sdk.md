# OpenAI Agents SDK

## What it is
OpenAI's official SDK for building agentic applications with handoffs, built-in tracing, and guardrails.

## Distinctive traits
- First-class "handoff" primitive for transferring control between specialized agents.
- Integrated tracing via the OpenAI platform.
- Tight coupling to OpenAI models but clean local runner API.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| openai-agents-sdk | OpenAI | Python | MIT | turn-based | native-tool-calling+mcp | conversation-only | handoffs | none | tracing+token-usage | turn-caps | library | stable |

## Key links
- Repo: https://github.com/openai/openai-agents-python
- Docs: https://platform.openai.com/docs/guides/agents
