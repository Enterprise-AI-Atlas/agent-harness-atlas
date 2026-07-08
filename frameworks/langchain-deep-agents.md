# LangChain Deep Agents

## What it is
LangChain Deep Agents is an open-source agent harness built on top of LangChain. It provides a runtime for tool-coding, file-reading, and multi-step agentic tasks, plus a first-class extension point called **agent harness profiles** that lets developers adapt harness behavior to a specific model without fine-tuning.

## Distinctive traits
- Per-model **harness profiles** can change base prompts, apply prompt suffixes, override tool descriptions, exclude tools/middleware, or add custom middleware.
- Designed around an open-source evaluation benchmark so profile changes can be verified against ground-truth correctness.
- The evaluation loop (run benchmark, analyze failures, propose profile changes, verify, re-run full suite) can be automated with an agentic proposer.

## Model-specific profile example: NVIDIA Nemotron 3 Ultra
NVIDIA published a tutorial showing how to tune the LangChain Deep Agents harness for **Nemotron 3 Ultra**.

- **Failing test:** `test_read_file_truncation_recovery_with_pagination` — the agent calls `read_file {'file_path': '/big.txt'}`, receives only the first page, and answers `x` instead of paging forward to find the real last line `opal-fox-91`.
- **Root cause:** The model receives no signal that the file result is paginated, so it treats the first page as the end of the file.
- **Fix:** A small middleware, `ReadFileContinuationNoticeMiddleware`, appends a notice when a `read_file` result contains exactly the per-read limit, telling the model the file likely continues and to call `read_file` again with a larger offset.

```python
class ReadFileContinuationNoticeMiddleware(AgentMiddleware):
    """Tell the model when a read_file result probably continues."""
    name = "ReadFileContinuationNoticeMiddleware"

    def wrap_tool_call(self, request, handler):
        return self._annotate(request, handler(request))

    @staticmethod
    def _annotate(request, result):
        if not isinstance(result, ToolMessage):
            return result
        if request.tool_call.get("name") != "read_file":
            return result
        content = str(result.text)
        args = request.tool_call.get("args", {}) or {}
        offset = int(args.get("offset", 0))
        limit = int(args.get("limit", 100))
        n_lines = sum(
            1
            for row in content.split("\n")
            if "\t" in row and row.split("\t", 1)[0].strip().isdigit()
        )
        if n_lines < limit:
            return result
        notice = (
            f"\n\n[read_file returned {limit} lines starting at offset {offset}, "
            f"the per-read limit. The file likely continues past this window. "
            f"To read further, call read_file again with offset={offset + limit}. "
            f"Do not assume you have seen the end of the file.]"
        )
        return result.model_copy(update={"content": content + notice})
```

Registering the profile:

```python
profile = HarnessProfile(
    extra_middleware=[
        ReadFileContinuationNoticeMiddleware(),
    ]
)
register_harness_profile("nvidia:nemotron-ultra", profile)
```

**Results from the tutorial:** the middleware resolved all three failing `read_file` tests and improved the overall evaluation benchmark from an average of **94/127** to **96/127**.

## Automating the loop
The same run/analyze/propose/verify cycle can be run by an agentic proposer. A reference implementation is available in the NemoClaw community repository and uses a constrained edit scope (only the profile file), repeated verification runs, and full-suite re-runs to avoid overfitting.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| langchain-deep-agents | LangChain | Python | MIT | turn-based | native-tool-calling+mcp | conversation-only | none | none | tracing+token-usage | rate-limits+turn-caps | library | stable |

## Key links
- Docs: https://docs.langchain.com/oss/python/deepagents/overview
- Eval benchmark: https://github.com/langchain-ai/deepagents/tree/main/libs/evals
- Harness profiles reference: https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles
- NVIDIA tutorial: https://developer.nvidia.com/blog/create-a-langchain-deep-agents-harness-profile-for-nvidia-nemotron-3-ultra-to-improve-performance
- Published profile diff: https://github.com/langchain-ai/deepagents/pull/4192/changes/9cde96141156d804bf9d3f468af15466cdb78e64#top
