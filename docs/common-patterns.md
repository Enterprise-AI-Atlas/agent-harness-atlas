# Common patterns across agent harnesses

This analysis is based on the 72 harnesses in [`data/agent-harness-matrix.csv`](../data/agent-harness-matrix.csv). The matrix is a manually-curated snapshot; counts are approximate and meant to surface structural trends rather than exact market share.

## 1. The universal agent loop

Roughly every harness implements the same basic cycle:

1. Receive a user request or goal.
2. Call an LLM with the current context and available tools.
3. Parse the LLM response for tool calls or final output.
4. Execute the requested tool(s) in a controlled environment.
5. Feed the tool result back into context.
6. Repeat until done, a guardrail trips, or a human intervenes.

This loop appears in `turn-based` harnesses (e.g., Pydantic AI, Codex CLI), `state-machine` harnesses (e.g., LangGraph, Temporal), `dag` harnesses (e.g., Prefect Agents, Gumloop), and even `eval-harness` runners such as SWE-bench and Inspect AI. The difference is not whether the loop exists, but who controls the transitions: the LLM, a graph, an event bus, or a workflow engine.

## 2. Tool binding is converging on native tool calling

Of the 72 harnesses, 27 list `native-tool-calling` and 36 list `plugin-api`. Many library/framework harnesses combine native tool calling with a `plugin-api` or MCP layer. Examples:

- **OpenAI Agents SDK** and **Pydantic AI** lean heavily on LLM-native function calling.
- **Autogen**, **LangGraph**, and **Google ADK** add MCP support alongside native tool calling.
- **CLI agents** (Aider, Codex CLI, Claude Code, Goose) expose tools through editor- or shell-specific plugin APIs.

MCP is listed 14 times and appears mostly in newer or explicitly interoperable harnesses. A2A is listed only once (Google ADK), reflecting that cross-agent protocols are still early.

## 3. Conversation-only memory is the default; persistence is the differentiator

40 of 72 harnesses use `conversation-only` memory. This is the cheapest model to implement and works well for short tasks. 19 harnesses support `persistent-state`, including most workflow/state-machine harnesses (LangGraph, Temporal, Camunda, Mastra, n8n, Zapier). 6 use `vector-db` for retrieval-augmented memory (Letta, AutoGPT, GPT Researcher, Cody, MemGPT).

Implication: if an agent must operate across multiple sessions, remember previous decisions, or coordinate with other agents, persistent state is almost mandatory. Many CLI coding agents get away with conversation-only memory because each task is self-contained.

## 4. Human-in-the-loop is dominated by approvals

21 harnesses expose `approvals`, while only 1 exposes `breakpoints` (Devin API). 51 have no built-in human intervention primitive. Approval gating is especially common in:

- Coding CLIs (Aider, Codex CLI, Claude Code, OpenHands, Cody)
- Enterprise automation platforms (n8n, Zapier Central, Relevance AI, VectorShift)
- Remote agent services (Devin API)

Break-before-continue debugging-style breakpoints remain rare outside research-grade and high-autonomy systems.

## 5. Observability = logging + tracing

59 harnesses list `logging` and 30 list `tracing`. `token-usage` tracking appears 12 times, mostly in library/framework harnesses with cost-conscious users (LangGraph, Pydantic AI, Inspect AI, Devin API). Pure CLI and embedded agents often stop at `logging`, while production frameworks add distributed tracing and cost attribution.

## 6. Guardrails are unevenly distributed

45 harnesses list no built-in guardrails in the matrix. The most common guardrail is `rate-limits` (13), followed by `sandboxing` (12). `turn-caps` appear only 3 times. Sandboxing is concentrated in:

- Evaluation harnesses (SWE-bench, Inspect AI, E2B, WebArena, OSWorld)
- Coding agents with remote/containerized execution (Devin API, OpenHands, SWE-agent)
- High-risk automation platforms

General-purpose libraries often leave guardrails to the application layer, which is a meaningful gap for production deployments.

## 7. Most harnesses ship as libraries

38 of 72 are `library`-based. 8 are `cloud-hosted`, 8 are `embedded` in editors, 11 run in `container`s, 4 are CLIs, and 3 are self-hosted `api-server`s. The deployment mode closely correlates with the target user:

- **Developers** get libraries and CLI/embedded tools.
- **Enterprise teams** get cloud-hosted and API-server platforms.
- **Researchers** get containerized evaluation harnesses.

## 8. Open source dominates, but proprietary is prominent

30 harnesses use MIT, 28 use Apache-2.0, and 13 are proprietary. The proprietary entries are concentrated in coding assistants (Claude Code, GitHub Copilot, Cursor, Cody, Amazon Q, Tabnine, Codeium Windsurf), remote agent services (Devin API), and enterprise automation platforms (Zapier, Relevance AI, VectorShift, Wordware).

## Bottom line

The agent harness landscape is more homogeneous at the loop level than the marketing suggests: almost everyone implements the same LLM → tool → context cycle. Differentiation shows up in **orchestration model**, **memory model**, **guardrails**, **deployment mode**, and **target persona**.
