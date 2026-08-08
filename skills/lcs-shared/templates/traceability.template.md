---
title: "Traceability Matrix: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: traceability
cot_level: strict
version: "1.0"
status: active
tags: [traceability, compliance]
summary: "Full traceability from requirements to tests for {feature-name}"
source: "srs.md"
related: ["prd-enhanced.md", "srs.md", "tests.md", "task-coverage.md"]
---

# Traceability Matrix: {feature-name}

## Forward Traceability (Requirements → Implementation)

| Source (PRD) | SRS | Test | Task | Status |
|-------------|-----|------|------|--------|
| SRC-001 | FR-001 | TEST-001 | task-001 | ✅ / ⏳ / ❌ |
| SRC-002 | BR-001 | TEST-002 | task-002 | ✅ / ⏳ / ❌ |

## Backward Traceability (Implementation → Requirements)

| Task | SRS | Test | Source (PRD) | Status |
|------|-----|------|-------------|--------|
| task-001 | FR-001 | TEST-001 | SRC-001 | ✅ / ⏳ / ❌ |

## Coverage Gaps
{List any SRS requirements without task coverage, or tasks without test coverage.}

## Handoff
→ `lcs-doc-finalizer` — Include in final documentation.
