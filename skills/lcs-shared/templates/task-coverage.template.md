---
title: "Task Coverage: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-task-slicer"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: task_coverage
cot_level: strict
version: "1.0"
status: active
tags: [tasks, planning, coverage]
summary: "Task breakdown and coverage matrix for {feature-name}"
source: "srs.md"
related: ["srs.md", "prd-enhanced.md", "task-001.md", "task-002.md"]
---

# Task Coverage: {feature-name}

## Coverage Matrix

| SRS ID | Task(s) | Description |
|--------|---------|-------------|
| FR-001 | task-001 | {what covers this req} |
| BR-001 | task-001, task-002 | {split across tasks} |
| TEST-001 | task-001 | {test implementation} |

## Task Dependency Graph
```
task-001 (foundation)
├── task-002 (depends: 001)
├── task-003 (depends: 001)
└── task-004 (depends: 002, 003)
```

## Task Summary
| Task | Type | Mode | Est. Time | Dependencies |
|------|------|------|-----------|--------------|
| task-001 | AFK | TDD | ~30min | — |
| task-002 | HITL | Normal | ~1hr | task-001 |
| task-003 | AFK | Normal | ~45min | task-001 |
| task-004 | HITL | TDD | ~1hr | task-002, task-003 |

**AFK** = autonomous (agent can run without human)
**HITL** = requires human-in-the-loop (design decision, API choice, etc.)

## Handoff
→ `lcs-task-executor` — Execute tasks in dependency order.
