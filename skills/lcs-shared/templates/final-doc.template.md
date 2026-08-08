---
title: "Final Documentation: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-doc-finalizer"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: final_doc
cot_level: strict
version: "1.0"
status: archived
tags: [documentation, final, archive]
summary: "Canonical finalized documentation for {feature-name}"
source: "task-###.md (all done), srs.md, code-review.md"
related: ["map.md", "code-review.md"]
---

# Final Documentation: {feature-name}

## Summary
{What was built and why. 2-3 paragraphs.}

## Requirements Implemented
| Source ID | Requirement | Status |
|-----------|-------------|--------|
| SRC-001 | {requirement} | ✅ Done |
| SRC-002 | {requirement} | ✅ Done |

## Architecture Decisions
- {Decision 1 — why this approach}
- {Decision 2}

## Implementation Details
### {Module/Component 1}
{What was implemented, key files changed.}

### {Module/Component 2}
{What was implemented.}

## Test Results
```bash
# Final test run
{output summary}
```

## Known Limitations
- {Limitation 1}
- {Limitation 2}

## Git Commit Recommendation
```
{type}: {description}

{details}
```

## PR Description
```markdown
## What
{what changed}

## Why
{why it changed}

## Testing
{how it was tested}

## Checklist
- [ ] Tests pass
- [ ] Docs updated
- [ ] No breaking changes
```

## Chain of Truth Report
| Stage | Detail |
|-------|--------|
| Source | All task files, srs.md, code-review.md |
| Assumption | All tasks verified done |
| Plan | Consolidate into final docs |
| Action | Generated map.md + doc.md |
| Verification | All SRC-### accounted for |
| Report | {summary} |

## Handoff
→ Archive complete. Source artifacts moved to `.lcs/archive/`.
