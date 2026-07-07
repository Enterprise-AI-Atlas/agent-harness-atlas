# LangChain + LangGraph

## What it is
LangChain provides LLM application primitives; LangGraph adds explicit graph-based orchestration with nodes, edges, and conditional state transitions.

## Distinctive traits
- LangGraph state machines are first-class: agents are nodes in a graph.
- Supports persistence, human-in-the-loop breakpoints, and time-travel debugging.
- Large ecosystem of integrations via LangChain packages.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| langchain-langgraph | LangChain | Python+TypeScript | MIT | state-machine | native-tool-calling+mcp | persistent-state | messaging+hierarchy | none | tracing+token-usage | rate-limits | library | production-grade |

## Key links
- Repo: https://github.com/langchain-ai/langgraph
- Docs: https://langchain-ai.github.io/langgraph/
