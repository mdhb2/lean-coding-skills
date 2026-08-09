---
title: "Code Review: {task-id} — {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-code-review"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: code_review
cot_level: strict
version: "1.0"
status: reviewed
tags: [review, verification, quality]
summary: "Implementation review for {task-id} against LCS artifacts"
source: "task-###.md, srs.md, tests.md, prd-enhanced.md"
related: ["task-###.md", "srs.md", "code-review.md"]
---

# Code Review: {task-id} — {feature-name}

## Review Summary
- **Task:** task-{###}
- **SRS Coverage:** {X of Y requirements verified}
- **Test Coverage:** {X of Y tests passing}
- **Verdict:** PASS / PASS WITH NOTES / FAIL

## Artifact Cross-Check

| SRS ID | Task Step | Implementation | Verified |
|--------|-----------|----------------|----------|
| FR-001 | Step 2 | {file:line} | ✅ / ❌ |
| BR-001 | Step 3 | {file:line} | ✅ / ❌ |

## Findings

### Critical (must fix)
- {Finding 1 — file:line, what's wrong, suggested fix}

### Major (should fix)
- {Finding 2}

### Minor (nice to have)
- {Finding 3}

## Security Check
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Auth checks in place
- [ ] No SQL injection vectors

## Test Verification
```bash
# Test run output
{command and output}
```

## Chain of Truth Report
| Stage | Detail |
|-------|--------|
| Source | task-###.md, srs.md, code changes |
| Assumption | {any assumptions} |
| Plan | {review approach} |
| Action | {files reviewed, tests run} |
| Verification | {test results, lint output} |
| Report | {verdict} |

## Handoff

Next recommended skill: lcs-doc-finalizer
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/code-review.md
Current phase: code_review
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <unresolved FIX items or None>
Source of Truth Bundle: .lcs/state.md, prd-enhanced.md if present, prd.md, srs.md, tests.md if present, traceability.md if present, task-coverage.md if present
Must Preserve IDs: <SRC/FR/AC/TEST IDs from artifacts>
Unresolved IDs: <list or None>
Suggested next command: Finalize documentation
