# Autogen

## What it is
Multi-agent conversation framework from Microsoft Research. Agents are `ConversableAgent` instances that exchange messages; tools are registered callables.

## Distinctive traits
- Conversation-based orchestration: the chat history itself drives control flow.
- `GroupChat` and `GroupChatManager` for multi-agent coordination.
- Built-in `CodeExecutor` for running generated code.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| autogen | Microsoft Research | Python | MIT | conversation-graph | native-tool-calling+mcp | conversation-only | messaging+hierarchy+roles | approvals | tracing+token-usage | rate-limits+turn-caps | library | production-grade |

## Key links
- Repo: https://github.com/microsoft/autogen
- Docs: https://microsoft.github.io/autogen/
