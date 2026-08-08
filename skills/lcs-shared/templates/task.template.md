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
status: pending
tags: [task, implementation]
summary: "{Brief description of what this task implements}"
source: "srs.md"
related: ["task-coverage.md"]
blocked_by: <TASK-### or None>
---

# TASK-###: <task-name>

* **Status**: pending
* **Type**: <AFK / HITL>
* **Depends on**: <TASK-### or None>
* **Source coverage**:
  - Sources: SRC-001, SRC-002
  - Requirements: FR-001, BR-001
  - Acceptance Criteria: AC-001, AC-002
  - Tests: TEST-001, TEST-002
* **Priority**: <high/medium/low>
* **Scope**: <vertical slice behavior, avoiding extremely stale specific details unless from verified prototypes>
* **Files likely touched**:
  - <file-path-1>
  - <file-path-2>
* **Implementation notes**:
  - <step-by-step logic, API changes, or structures>
* **Acceptance criteria**:
  - [ ] <AC 1 (falsifiable)>
  - [ ] <AC 2 (falsifiable)>
* **Test plan**:
  - <Unit test spec or manual verification steps>

## Chain of Truth Report

### Level
Very Strict

### Sources Checked
- `.lcs/state.md`
- `.lcs/work-items/{timestamp}-{slug-work-item}/task/task-###.md`

### Assumptions
- [verified] Task dependencies met.
- [verified] Chosen mode (Normal/TDD) confirmed with user.

### Plan Before Action
1. Read state.md and task file.
2. Check dependencies.
3. Implement task.
4. Run validation.

### Actions Taken
- <Exact commands run with stdout/stderr captured>

### Verification
- <All test and lint commands run; results quoted verbatim>

### Proof of Result
```
<Quoted command outputs>
```

### Blocked Items
<None, or list with reasons>

### Confidence
<high/medium/low>

### Risk Notes
<None, or outstanding concerns>

## Handoff

Next recommended skill: lcs-task-executor
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/task/task-###.md
Current phase: execution
Current confidence: high
Blocking questions: None
Risks to carry forward: None
Source of Truth Bundle: target task, prd-enhanced.md if present, prd.md, srs.md if referenced, tests.md if referenced, traceability.md if present, task-coverage.md if present
Must Preserve IDs: <executed SRC/FR/AC/TEST IDs>
Unresolved IDs: <remaining uncovered IDs or None>
Suggested next command: Eksekusi TASK-002
