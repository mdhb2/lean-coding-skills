---
title: "LCS State"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-master"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [state]
summary: "Open work item registry and selected work item state"
status: active
related: []
artifact_type: state
source: "runtime"
cot_level: standard
version: "1.1"
type: state
current_phase: idle
current_work: null
work_items: {}
last_session_note: "Initial setup"
timestamp: {YYYY-MM-DDTHH:MM:SS+07:00}
---

# LCS State

Runtime control file for selecting one active work item while preserving every unfinished work item. Read this first when continuing work.

| Field | Meaning |
|---|---|
| `current_phase` | Mirror of the selected work item's phase, or `idle` when no work item is selected |
| `current_work` | Selected work-item ID `{timestamp}-{slug-work-item}` or `null` |
| `work_items` | Registry of all unfinished work items; finalized items are removed only by `lcs-doc-finalizer` |
| `last_session_note` | One-line summary of the last state-changing action |
| `timestamp` | Last state update time (ISO-8601) |

## Registry

Each `work_items` entry uses:

```yaml
work_items:
  "{timestamp}-{slug-work-item}":
    title: "Human-readable title"
    path: ".lcs/work-items/{timestamp}-{slug-work-item}"
    phase: new
    status: open
    created_at: "{ISO-8601 timestamp}"
    updated_at: "{ISO-8601 timestamp}"
```

## Rules

- `current_work` is only a pointer; switching work must not delete other registry entries.
- When `current_work` is non-null, `current_phase` must match `work_items[current_work].phase`.
- A skill that changes the selected work item's phase must update both fields and `updated_at`.
- After successful finalization/archive, remove only that finalized entry from `work_items`.
- If the finalized item was selected, set `current_work: null` and `current_phase: idle`.

After finalization, `lcs-doc-finalizer` replaces the pointer with `Source Truth Bundle` referencing `.lcs/docs/` outputs.
