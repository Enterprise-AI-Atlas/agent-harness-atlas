#!/usr/bin/env python3
"""Validate the agent-harness-atlas data files."""

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "data" / "agent-harness-matrix.csv"
FRAMEWORKS_DIR = REPO_ROOT / "frameworks"
CONFIDENCE_PATH = REPO_ROOT / "data" / "confidence.csv"

CONTROLLED = {
    "orchestration_model": {
        "state-machine",
        "dag",
        "event-driven",
        "turn-based",
        "actor-based",
        "conversation-graph",
        "role-based",
        "hierarchy",
        "eval-harness",
        "other",
        "unknown",
    },
    "tool_integration": {
        "native-tool-calling",
        "mcp",
        "a2a",
        "custom-sdk",
        "plugin-api",
        "none",
        "unknown",
    },
    "memory_model": {
        "conversation-only",
        "persistent-state",
        "shared-memory",
        "vector-db",
        "none",
        "other",
        "unknown",
    },
    "multi_agent_primitives": {
        "messaging",
        "hierarchy",
        "roles",
        "swarm",
        "handoffs",
        "none",
        "unknown",
    },
    "human_in_the_loop": {
        "breakpoints",
        "approvals",
        "feedback",
        "none",
        "unknown",
    },
    "observability": {
        "tracing",
        "cost-tracking",
        "token-usage",
        "logging",
        "none",
        "unknown",
    },
    "guardrails": {
        "sandboxing",
        "output-moderation",
        "rate-limits",
        "turn-caps",
        "none",
        "unknown",
    },
        "deployment_mode": {
        "library",
        "cli",
        "api-server",
        "container",
        "cloud-hosted",
        "embedded",
        "other",
        "unknown",
    },
    "maturity_estimate": {
        "experimental",
        "stable",
        "production-grade",
        "unknown",
    },
}


def validate() -> None:
    errors = []
    rows = list(csv.DictReader(CSV_PATH.open("r", newline="")))
    frameworks = {p.stem for p in FRAMEWORKS_DIR.glob("*.md")}

    for row in rows:
        name = row["name"]
        if name not in frameworks:
            errors.append(f"Missing profile: {name}")
        for col, allowed in CONTROLLED.items():
            for value in row[col].split("+"):
                value = value.strip()
                if value not in allowed:
                    errors.append(f"{name}.{col}: invalid value {value!r}")

    if CONFIDENCE_PATH.exists():
        confidence_names = {r["name"] for r in csv.DictReader(CONFIDENCE_PATH.open("r", newline=""))}
        missing_conf = {r["name"] for r in rows} - confidence_names
        if missing_conf:
            errors.append(f"Missing confidence rows: {sorted(missing_conf)}")
    else:
        errors.append(f"Confidence file not found: {CONFIDENCE_PATH}")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(" -", err)
        raise SystemExit(1)

    print(f"OK: {len(rows)} rows, all profiles present, all values valid.")


if __name__ == "__main__":
    validate()
