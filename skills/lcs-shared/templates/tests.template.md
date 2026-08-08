---
title: "Test Plan: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: tests
cot_level: strict
version: "1.0"
status: draft
tags: [tests, test-plan]
summary: "Test specifications for {feature-name}"
source: "srs.md"
related: ["srs.md", "prd-enhanced.md"]
---

# Test Plan: {feature-name}

## Test Coverage Matrix

| Test ID | SRS ID | Type | Description | Status |
|---------|--------|------|-------------|--------|
| TEST-001 | FR-001 | unit | {test desc} | pending |
| TEST-002 | BR-001 | integration | {test desc} | pending |
| TEST-003 | VR-001 | unit | {test desc} | pending |
| TEST-004 | EC-001 | edge | {test desc} | pending |

## Test Cases

### TEST-001: {test-name}
- **SRS Source:** FR-001
- **Type:** unit / integration / e2e
- **Preconditions:** ...
- **Steps:**
  1. ...
  2. ...
- **Expected Result:** ...
- **Edge Cases:** ...

## Handoff
→ `lcs-task-slicer` — Tasks reference these test IDs.
→ `lcs-task-executor` — Implement tests alongside code.
