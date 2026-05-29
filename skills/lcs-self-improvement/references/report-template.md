# LCS Self-Improvement Report Template

Use this template for `.lcs/docs/self-improvements.md`.

```markdown
# LCS Self-Improvement Report

## Scope
**Generated from:** [current conversation / supplied files / supplied folders / combined sources]
**Date:** [current date if available, otherwise TODO]
**Changes applied:** None

## Executive Summary
[Short summary of the most important improvement opportunities.]

## Evidence Limitations
[State what evidence was available and what was not available.]

## Top Friction Patterns

### 1. [Pattern Name]
**Status:** [Already addressed / Partially addressed / Missing / Conflicting / Needs user decision]
**Problem:** [Summarized problem without raw user quotes.]
**Why it matters:** [Practical impact on future sessions.]
**Evidence summary:** [Brief non-quote summary of observed evidence.]
**Suggested target:** [File or location to update, such as AGENTS.md, .lcs/rules/, skills/<skill-name>/SKILL.md, etc.]
**Suggested addition:**
```markdown
[Proposed instruction text]
```
**Confidence:** [High / Medium / Low]

---

## What Worked Well
* [Pattern or workflow that should be preserved]
* [Useful constraint or output format]

## Already Addressed
| Issue | Where addressed | Notes |
| ------ | --------------- | ------ |
| [TODO] | [TODO] | [TODO] |

## Partially Addressed
| Issue | Existing location | Missing piece |
| ------ | ----------------- | ------------- |
| [TODO] | [TODO] | [TODO] |

## Missing Improvements
| Issue | Suggested target | Priority |
| ------ | ---------------- | -------- |
| [TODO] | [TODO] | [High / Medium / Low] |

## Conflicts
| Conflict | Files involved | Recommendation |
| -------- | -------------- | -------------- |
| [TODO] | [TODO] | [TODO] |

## Potential Skill Improvements
| Skill | Suggested improvement | Why |
| ------ | --------------------- | ------ |
| [TODO] | [TODO] | [TODO] |

## Potential New Skills
| Skill idea | Purpose | Trigger |
| ---------- | ------- | ------- |
| [TODO] | [TODO] | [TODO] |

## Open Questions
1. [ASK USER]
2. [ASK USER]

## How To Apply This Report
This report does not change future agent behavior by itself. To make the recommendations effective in future sessions, review the suggested changes and apply accepted items to persistent instruction sources such as:

* `AGENTS.md`
* `CLAUDE.md`
* `GEMINI.md`
* `.lcs/rules/`
* `.lcs/docs/`
* `skills/`

Recommended follow-up command:
```text
Apply the accepted recommendations from .lcs/docs/self-improvements.md
```

Only accepted recommendations should be applied. Preserve rejected or uncertain items as open questions.
```
