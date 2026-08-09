---
title: "SRS: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: srs
cot_level: strict
version: "1.0"
status: draft
tags: [srs, specification, deterministic]
summary: "Software Requirements Specification for {feature-name}"
source: "prd-enhanced.md"
related: ["prd-enhanced.md", "tests.md", "api.md", "db.md", "traceability.md"]
---

# SRS: {feature-name}

## Traceability Matrix

| SRS ID | Source | Description | Test ID |
|--------|--------|-------------|---------|
| FR-001 | SRC-001 | {functional req} | TEST-001 |
| BR-001 | SRC-002 | {business rule} | TEST-002 |
| VR-001 | — | {validation rule} | TEST-003 |
| EC-001 | — | {edge case} | TEST-004 |

## Functional Requirements

### FR-001: {requirement-name}
- **Description:** {precise, testable, deterministic}
- **Source:** SRC-001
- **Priority:** high/medium/low
- **Acceptance Criteria:** AC-001, AC-002
- **Dependencies:** none

## Business Rules

### BR-001: {rule-name}
- **Description:** ...
- **Source:** SRC-002

## Validation Rules

### VR-001: {rule-name}
- **Input:** ...
- **Validation:** ...
- **Error:** ...

## Edge Cases

### EC-001: {case-name}
- **Scenario:** ...
- **Expected:** ...

## Constraints
- {Technical or business constraints}

## Assumptions
- {What we assume to be true}

## Handoff

Next recommended skill: lcs-task-slicer
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/srs.md
Current phase: srs
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary or None>
Source of Truth Bundle: .lcs/state.md, prd-enhanced.md if present, prd.md, srs.md, tests.md, traceability.md
Must Preserve IDs: SRC-001, SRC-002, FR-001, AC-001, TEST-001, ...
Unresolved IDs: <list or None>
Suggested next command: Slice SRS into tasks
