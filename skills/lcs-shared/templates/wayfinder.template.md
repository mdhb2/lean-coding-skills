---
title: "Wayfinder: {codebase-area}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-wayfinder"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [navigation, codebase-map, decisions]
summary: "Codebase navigation map for {codebase-area}"
status: draft
artifact_type: wayfinder
source: "{source-file}"
cot_level: strict
version: "1.0"
---

# Wayfinder: {codebase-area}

## Navigation Map

### Entry Points

| Entry Point | File | Purpose |
|---|---|---|
| {entry} | {file} | {purpose} |

### Key Paths

| From | To | Purpose | Notes |
|---|---|---|---|
| {source} | {destination} | {purpose} | {notes} |

### Decision Points

| Location | Decision | Options | Recommendation |
|---|---|---|---|
| {file:line} | {question} | {options} | {recommendation} |

## Decision Tickets

<!-- Blocked decisions that need human input.
     Status column uses the OKF lifecycle: active = open, archived = resolved.
     Never use open/blocked/resolved in frontmatter — keep that vocabulary in the body only. -->

| Ticket | Question | Context | Status |
|---|---|---|---|
| DEC-001 | {question} | {context} | {active/archived} |

## Architecture Notes

### Patterns Used

| Pattern | Location | Purpose |
|---|---|---|
| {pattern} | {location} | {purpose} |

### Dependencies

| Component | Depends On | Type | Notes |
|---|---|---|---|
| {component} | {dependency} | {internal/external} | {notes} |

## Decision Ticket Frontmatter Template

Each ticket is a child file `.lcs/work-items/{ts}-{slug}/wayfinder-tickets/DEC-###.md`:

```yaml
---
title: "DEC-001: {question}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-wayfinder"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [wayfinder-ticket]
summary: "{one-line question}"
status: active        # active = open; set to archived when resolved
related: ["wayfinder-map.md"]
artifact_type: wayfinder
source: "wayfinder-map.md"
cot_level: strict
version: "1.0"
blocked_by: "{DEC-###}"   # optional: ticket this one depends on (empty if none)
---
```

## Files Touched

| File | Lines | Change Type | Reason |
|---|---|---|---|
| {file} | {lines} | {read/modified} | {reason} |

## Navigation Summary

{brief-summary-of-codebase-area}

## Handoff

Next recommended skill: {next-skill}
Next file read: {next-file}
Current phase: wayfinder

## Note

Wayfinder plans and navigates work during active development. It is not a one-time architecture mapping tool — use `lcs-codebase-doc` for onboarding/learning-oriented codebase mapping.
