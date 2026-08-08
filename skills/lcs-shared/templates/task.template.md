---
title: "Task {###}: {task-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-task-slicer"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: task
cot_level: very_strict
version: "1.0"
status: draft
tags: [task, implementation]
summary: "{Brief description of what this task implements}"
source: "srs.md"
related: ["task-coverage.md"]
---

# Task {###}: {task-name}

## Source Coverage

| Source ID | Artifact | Section | Verified |
|-----------|----------|---------|----------|
| FR-001 | srs.md | Functional Requirements | [ ] |
| TEST-001 | tests.md | Test Cases | [ ] |

## Description
{What to build. Be specific enough that an agent can implement without guessing.}

## Dependencies
- [ ] task-{###}: {name} — status: {done/pending}

## Mode
- **Development:** Normal / TDD
- **Type:** AFK / HITL

## Implementation Steps
1. {Step 1 — concrete, verifiable}
2. {Step 2}
3. {Step 3}

## Acceptance Criteria
- [ ] {Criterion 1 — maps to Source Coverage}
- [ ] {Criterion 2}

## Verification Commands
```bash
# Step 1 verification
{command}

# Final verification
{command}
```

## Status
- **Current:** draft → in_progress → done / blocked
- **Blocked Reason:** {if blocked, why}

## Chain of Truth Report
| Stage | Detail |
|-------|--------|
| Source | srs.md FR-001, tests.md TEST-001 |
| Assumption | {any assumptions} |
| Plan | {steps to take} |
| Action | {what was done} |
| Verification | {commands run, results} |
| Report | {pass/fail/block} |

## Handoff
→ `lcs-code-review` — Review implementation against artifacts.
