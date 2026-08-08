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

<!-- Blocked decisions that need human input -->

| Ticket | Question | Context | Status |
|---|---|---|---|
| DEC-001 | {question} | {context} | {open/blocked/resolved} |

## Architecture Notes

### Patterns Used

| Pattern | Location | Purpose |
|---|---|---|
| {pattern} | {location} | {purpose} |

### Dependencies

| Component | Depends On | Type | Notes |
|---|---|---|---|
| {component} | {dependency} | {internal/external} | {notes} |

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

This is distinct from `lcs-pathfinder` (understanding skill).
Wayfinder = codebase navigation during active work.
Pathfinder = one-time architecture mapping for onboarding/learning.
