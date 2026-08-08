---
title: "LCS State"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-master"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [state]
summary: "Active work item state"
status: active
related: []
artifact_type: state
source: "runtime"
cot_level: standard
version: "1.0"
type: state
current_phase: idle
current_work: null
last_session_note: "Initial setup"
timestamp: {YYYY-MM-DDTHH:MM:SS+07:00}
---

# LCS State

Runtime control file locating the active work item. Read this first when continuing work.

| Field | Meaning |
|---|---|
| `current_phase` | Current workflow phase (idle, explore, prd, prd_review, srs, tasks, execution, code-review, finalization, complete, ...) |
| `current_work` | Active work-item slug `{timestamp}-{slug-work-item}` or `null` |
| `last_session_note` | One-line summary of the last session action |
| `timestamp` | Last update time (ISO-8601) |

After finalization, `lcs-doc-finalizer` replaces the pointer with `Source Truth Bundle` referencing `.lcs/docs/` outputs.
