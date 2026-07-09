# Albion

## What it is

A configuration and plugin layer that runs Claude Code against Z.ai's GLM-5.2 instead of Anthropic's Claude models. It injects an always-on operating charter (`ALBION.md`) that forces a plain-file working board (`task.md` + `verification.md`) for every non-trivial task, plus deterministic enforcement hooks, delegate-agent skills, accurate cost telemetry, and a vision helper.

## Distinctive traits

- **Model swap without migration**: points Claude Code at a Z.ai Anthropic-compatible endpoint; no fork or patch of Claude Code.
- **Always-on charter**: compiled from `manifest/` source fragments with a byte-exact drift gate; not a trigger phrase or mode.
- **Workbench discipline**: every non-trivial task must leave `task.md` and `verification.md` with content; `bench/report` measures evidence-complete rates.
- **Deterministic hooks**: destructive-command guard, stop gate that blocks "done" until verification passes, strike counter, secrets scrubber for working notes, and post-compaction state re-injection.
- **Real-cost telemetry**: recomputes cost from raw token usage because Claude Code's built-in display is wrong against non-Anthropic endpoints; supports both prompt-metered Coding Plan and token-metered API lanes.
- **Runs alongside stock Claude Code**: launcher sets everything per-invocation; stock `claude` sessions are unaffected.

## Matrix row

| name | org | primary_language | license | orchestration_model | tool_integration | memory_model | multi_agent_primitives | human_in_the_loop | observability | guardrails | deployment_mode | maturity_estimate |
|------|-----|------------------|---------|---------------------|------------------|--------------|------------------------|-------------------|---------------|------------|-----------------|-------------------|
| albion | AmbitiousRealism2025 | bash+python | MIT | turn-based | plugin-api | persistent-state | none | approvals | cost-tracking+logging | none | cli | experimental |

## Key links

- Repo: https://github.com/AmbitiousRealism2025/Albion
- Notes: The "guardrails" column is `none` under the atlas controlled vocabulary, but Albion ships hook-based enforcement (destructive-command guard, stop gate, strike counter, secrets scrubber) that does not map directly to sandboxing/output-moderation/rate-limits/turn-caps.
