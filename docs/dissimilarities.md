# Dissimilarities: where agent harnesses diverge

This page groups the 72 matrix harnesses by architectural family and highlights the forks that actually matter when choosing or building a harness.

## 1. Orchestration model: who controls the loop?

The matrix shows a clear split:

- **Turn-based (32)**: the LLM drives each step with minimal explicit structure. Examples: Pydantic AI, OpenAI Agents SDK, Aider, Codex CLI, Claude Code, Smolagents, most coding CLIs. These are easy to start with but can become brittle for long-running or conditional workflows.
- **DAG (14)**: execution is a directed acyclic graph of tasks. Examples: Dagger Agents, Prefect Agents, Gumloop, n8n AI Agent, VectorShift, GPT Researcher. DAG harnesses fit automation, ETL, and repeatable processes.
- **State-machine (5)**: explicit states, transitions, and persistence. Examples: LangGraph, Temporal Agents, Camunda AI Agent, Mastra. These excel when a process has guard conditions, retries, human breakpoints, or audit requirements.
- **Role-based (5) and conversation-graph (2)**: agents are organized by role or conversation topology. Examples: CrewAI, MetaGPT, CAMEL, Autogen. These optimize for multi-agent collaboration but introduce coordination complexity.
- **Actor-based / event-driven (3)**: agents react to messages or events. Examples: Dapr Agents, AutoGPT, SuperAGI. These can scale across services but require robust messaging infrastructure.
- **Eval-harness (9)**: not production runtimes, but execution harnesses for benchmarks. Examples: SWE-bench, Inspect AI, E2B, WebArena.

**Why it matters:** the orchestration model determines whether an agent is a script, a workflow, a long-running process, or a multi-agent system. Mixing models inside one project usually requires explicit bridges (MCP, A2A, or shared state).

## 2. Memory model: how much does the agent remember?

- **Conversation-only (40)**: the agent's entire memory is the current prompt context. Cheap, simple, and session-bound. Examples: most CLI coding agents, Pydantic AI, Smolagents.
- **Persistent state (19)**: the harness durably stores execution state across sessions or steps. Examples: LangGraph, Temporal, Camunda, n8n, Mastra, SuperAGI. This is the key enabler for multi-step, resumable workflows.
- **Vector/retrieval memory (6)**: agents query a knowledge store. Examples: Letta, AutoGPT, GPT Researcher, Cody, MemGPT.
- **None (7)**: mostly eval harnesses that run stateless tasks.

**Why it matters:** conversation-only agents forget everything between restarts. If your use case requires learning from prior runs, long-term planning, or cross-agent memory, persistent or vector memory is non-negotiable.

## 3. Multi-agent primitives: alone or in a crowd?

49 harnesses have no multi-agent primitives at all. Among the rest:

- **Messaging (12)**: agents send messages to one another. Autogen, LangGraph, Dapr Agents, CAMEL.
- **Hierarchy (15)**: supervisor/worker or layered control. CrewAI, Camunda, LangGraph, MetaGPT, Temporal.
- **Roles (10)**: role-based task division. CrewAI, CAMEL, MetaGPT, Relevance AI, Griptape.
- **Handoffs (2)**: explicit transfer of control between specialized agents. OpenAI Agents SDK, Google ADK.
- **Swarm (0)**: no harness in the current matrix lists swarm as a primary primitive, though some research projects support it experimentally.

**Why it matters:** multi-agent features are often the headline selling point, but most real-world agents still operate solo. Multi-agent harnesses add complexity (message schemas, conflict resolution, shared state) that pays off only when the problem genuinely decomposes into specialized workers.

## 4. Human-in-the-loop: approvals vs. breakpoints

The matrix is heavily skewed toward `approvals` (21) over `breakpoints` (1). Devin API is the only harness currently tagged with breakpoints. This reflects two design philosophies:

- **Approval gating** is coarse: the agent stops before risky actions and asks permission. Good for safety, but interruptive.
- **Breakpoints** are fine-grained: a human can inspect and steer at arbitrary points. Good for debugging and high-stakes autonomy, but harder to implement well.

**Why it matters:** if you need true human *steering* rather than just veto power, the harness must support breakpoints or equivalent introspection hooks. Most current tools do not.

## 5. Guardrails: sandboxing is not universal

Only 12 harnesses list `sandboxing`. They fall into two groups:

- **Evaluation harnesses** that run arbitrary agent-generated code (SWE-bench, Inspect AI, E2B, AgentBoard, MINT, WebArena, OSWorld, ToolBench).
- **Coding agents** that execute code on behalf of the user (Devin API, OpenHands, SWE-agent).

The remaining 60 harnesses either rely on the host environment's isolation or leave sandboxing to the operator. `rate-limits` (13) and `turn-caps` (3) are the main production guardrails outside sandboxes.

**Why it matters:** an agent that can write and run code without sandboxing is a remote-code-execution risk. This is one of the biggest gaps between experimental demos and production deployment.

## 6. Deployment mode: library vs. service vs. IDE

The deployment split mirrors the go-to-market split:

- **Libraries (38)** target developers who embed the harness in their own code. Examples: LangGraph, Pydantic AI, Autogen, Smolagents.
- **Cloud-hosted services (8)** target teams that want managed agents. Examples: Zapier Central, Relevance AI, VectorShift, Devin API, Arcade AI.
- **Embedded in editors (8)** target individual developers in their IDE. Examples: Continue, Cody, Claude Code, Copilot, Cursor.
- **Containers (11)** target reproducible, isolated execution. Mostly eval harnesses and coding agents.

**Why it matters:** a library gives you control but requires you to build guardrails, observability, and deployment. A cloud service gives you those but limits model/provider choice and raises data-sovereignty questions.

## 7. License: open core vs. proprietary assistants

Proprietary harnesses (13) are almost entirely coding assistants or cloud platforms. Open-source harnesses (58) dominate the general-purpose framework and evaluation spaces. The exception is CLI coding agents: both open-source (Aider, Codex CLI, OpenHands) and proprietary (Claude Code, Cursor, Copilot) are common.

**Why it matters:** if you need to audit, fork, or self-host, the license is a first-order filter. Proprietary coding assistants often win on polish and model integration; open-source frameworks win on extensibility.

## Surprising outliers

- **Google ADK** is the only harness currently tagged with A2A support, making it an early mover in cross-agent protocols.
- **Dapr Agents** is the only `actor-based` harness, reflecting its microservice-native design.
- **Devin API** is the only harness with `breakpoints`, possibly because it is positioned as a supervised remote worker rather than an autonomous tool.
- **E2B** is an eval/sandbox harness that is also used as a building block by other harnesses, blurring the line between harness and infrastructure.

## Bottom line

The meaningful differences are not "does it use an LLM?" or "does it call tools?" — those are table stakes. The real forks are **who owns the execution graph**, **how memory persists**, **how agents coordinate**, **how humans intervene**, **how code is isolated**, and **how the harness is consumed**.
