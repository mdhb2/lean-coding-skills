---
name: lcs-code-review
description: Use this skill when the user asks to review code implementation after lcs-task-executor execution. Trigger for prompts like "review code", "lcs-code-review", "review implementation", "check results", "verify task", "code review", "validate against artifacts". Do not trigger for design review, architecture review, brainstorming, or new implementation without existing code.
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

# LCS Code Review

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Review implementation results after `lcs-task-executor`.
- Check whether code matches existing LCS artifacts — Explore, PRD, PRD Enhance, SRS, Task Breakdown, Acceptance Criteria.
- Output a structured review report, not a code patch.

Trigger
- Activate when user asks to review code, check implementation, or verify task completion against artifacts.

Behavior checklist
- Read `.lcs/state.md` to locate active work item.
- Read task artifacts in Required Reading Order.
- Perform review per What to Review sections.
- Write review report to `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md`.
- Update `.lcs/state.md` with current_phase: code-review.

## Output Artifact

- Save review report as: `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md`
- Artifact type: `code_review`
- Use the active work item folder from `.lcs/state.md`

## OKF Frontmatter & Writing Safety

- When creating review reports, include YAML frontmatter following the schema in `../lcs-shared/contract.md`.
- Follow the Artifact Writing Safety rules in contract.md — generate content first, write one file, verify, stop on failure.

## Chain of Truth Level

Level: **Strict**

This skill verifies that implementation matches specifications. Every claim in the review must cite evidence from artifacts or code.

---

## Primary Role

Acts as **reviewer and verifier**, not as a second executor.

Core responsibilities:

1. Check code alignment with LCS artifacts.
2. Find gaps between requirements and implementation.
3. Identify potential bugs, edge cases, regressions, and technical risks.
4. Provide a prioritized fix list executable by `lcs-task-executor`.
5. Determine final status: PASS, PASS_WITH_NOTES, NEEDS_FIX, or BLOCKED.

---

## Mandatory Constraints

### 1. Do not edit code directly

This skill **must not edit code files by default**.

Allowed actions:

- Read artifacts.
- Read code files.
- Read diffs.
- Analyze implementation.
- Write review report.
- Provide patch recommendations.
- Provide handoff for executor.

Forbidden actions:

- Edit code directly.
- Large refactors without instruction.
- Add new features.
- Change task scope.
- Claim fix without successful write/edit tool result.
- Merge review and execution in one step.

If code fixes are needed, produce instructions for `lcs-task-executor`.

### 2. Do not create new requirements

Reviewer must not add requirements not present in artifacts.

Suggestions are allowed, but must be labeled:

```text
Optional Improvement
```

Not:

```text
Required Fix
```

Required Fix may only come from:

- Explore
- PRD
- PRD Enhance
- SRS
- Task Breakdown
- Acceptance Criteria
- Actual bugs / potential bugs blocking main requirements
- Clear security/data risks

### 3. Do not claim PASS without evidence

Every PASS decision must be backed by evidence.

Evidence can be:

- Files checked
- Functions checked
- Diffs checked
- Tests run
- Matching acceptance criteria
- Verified behavior

If tests cannot be run, state clearly:

```text
Tests were not run.
```

Do not write:

```text
All tests passed.
```

unless there is actual test output.

### 4. If artifacts are incomplete, do not force a full review

If critical artifacts are missing, use status:

```text
BLOCKED
```

or:

```text
PARTIAL_REVIEW
```

Then explain which artifacts are missing.

Example:

```text
BLOCKED: SRS not found, behavior compliance review cannot be performed fully.
```

---

## Required Reading Order

Before review, read artifacts in this order:

1. `explore.md`
2. `prd.md`
3. `prd-enhance.md` or PRD reviewer output
4. `srs.md`
5. `task-breakdown.md`
6. Active task being worked on
7. Task acceptance criteria
8. Changed code files
9. Related tests, if any
10. Related documentation, if any

If the repository uses different paths, locate the most relevant LCS artifacts.

---

## What to Review

### 1. Explore Alignment

Check if implementation still matches initial context.

Verify:

- Original problem to solve.
- Technical constraints.
- User goal.
- Scope boundaries.
- Exploration decisions agreed upon.

Review questions:

```text
Does the code solve the same problem identified during exploration?
Is there any implementation that deviates from the initial context?
Are any initial constraints violated?
```

### 2. PRD Alignment

Check if feature matches product requirements.

Verify:

- Feature purpose.
- User story.
- Functional requirements.
- Non-functional requirements.
- Out of scope.
- Success criteria.

Review questions:

```text
Are all main PRD requirements reflected in the code?
Are there any requirements not yet implemented?
Are there any features added that were not requested?
Does the product behavior match user expectations?
```

### 3. PRD Enhance Alignment

Check if PRD reviewer hardening is applied.

Verify:

- Additional edge cases.
- Requirement risks.
- Clarifications.
- Security concerns.
- Data validation.
- Permission rules.
- Failure scenarios.
- UX fallbacks.

Review questions:

```text
Is the PRD hardening output followed?
Are important edge cases handled?
Are previously identified vulnerabilities closed?
```

### 4. SRS Alignment

Check if implementation follows technical specification.

Verify:

- Data model.
- API contract.
- Service behavior.
- State transitions.
- Error handling.
- Validation rules.
- Permission logic.
- Integration points.
- Side effects.
- Dependencies.

Review questions:

```text
Does the code follow the SRS technical design?
Is the data structure correct?
Is the system flow correct?
Is error handling implemented as specified?
Are there any technical behaviors differing from SRS?
```

### 5. Task Breakdown Alignment

Check if completed task matches task breakdown.

Verify:

- Task ID.
- Task scope.
- Acceptance criteria.
- Target files.
- Expected output.
- Work boundaries.
- Task dependencies.

Review questions:

```text
Was the task completed within scope?
Did the task expand into other areas?
Are all acceptance criteria met?
Are there files that should have been touched but were not?
Are there files that should not have been touched?
```

### 6. Potential Bugs

Must check:

- Null / undefined handling.
- Empty state.
- Invalid input.
- Duplicate data.
- Race condition.
- Permission bypass.
- Incorrect validation.
- Incorrect default value.
- Wrong conditional logic.
- Wrong date/time handling.
- Timezone issue.
- Data loss.
- Broken migration.
- Broken relation.
- Broken API response.
- Broken UI state.
- Unhandled errors.
- Regression against existing features.
- Inconsistent naming.
- Inconsistent types.
- Dangerous hardcoded values.

### 7. Security & Data Safety

Must check:

- Auth check.
- Authorization / role permission.
- Input validation.
- SQL injection risk.
- XSS risk.
- CSRF risk.
- Secret/token leakage.
- Sensitive data exposure.
- Unsafe file upload.
- Unsafe external request.
- Missing rate limit if relevant.
- Data ownership rule.

If security is not relevant to the task, write:

```text
No direct security-sensitive surface found for this task.
```

### 8. Error Handling & Failure Mode

Must check:

- Database error.
- API error.
- Network error.
- Empty response.
- Invalid payload.
- Missing config.
- Failed dependency.
- Failed transaction.
- Partial update.
- Retry behavior if relevant.

### 9. Test Coverage

Review:

- Unit test.
- Feature test.
- Integration test.
- Regression test.
- Edge case test.
- Manual test instruction.

If tests are missing, determine whether this is a `Required Fix` or `Recommended Improvement` based on task risk level.

### 10. Maintainability

Check:

- Overly long functions.
- Logic duplication.
- Confusing naming.
- File structure mismatching project patterns.
- Business logic leaking into UI.
- Heavy queries.
- Unclear types.
- Missing comments on complex logic.
- Excessive abstraction.

Maintainability issues are only Required Fix if they risk causing bugs or violating SRS/task.

---

## Severity

| Level | Label | Examples |
|---|---|---|
| P0 | Blocker | Main requirement not met, data corruption risk, security bypass, app crash, wrong task direction |
| P1 | High | Critical edge case fails, missing error handling, important tests missing |
| P2 | Medium | Minor inconsistency, maintainability issue, suboptimal UX fallback |
| P3 | Low | Naming clarity, minor formatting, optional improvement |

---

## Final Review Status

| Status | Requirements |
|---|---|
| PASS | All AC met, no P0/P1, no major bugs found |
| PASS_WITH_NOTES | No P0, no mandatory P1, has P2/P3 or optional improvements |
| NEEDS_FIX | Has P0 or P1, AC not fully met, mismatch with artifacts |
| BLOCKED | Main artifact missing, diff unavailable, active task unclear |

---

## Review Output Format

After review, produce a report saved to `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md` using the template at `../lcs-code-review/assets/code-review-template.md`.

Copy the template, replace each `{{placeholder}}` with actual content, and write the result.

### Template Fields

| Field | Description | Required |
|---|---|---|
| `{{active_work_item_path}}` | Path to current work item folder | yes |
| `{{iso_timestamp}}` | ISO 8601 timestamp with timezone offset | yes |
| `{{task_file_or_diff}}` | Task file or diff path being reviewed | yes |
| `{{task_file}}` | Previous artifact (task file) | yes |
| `{{task_title}}` | Short title of reviewed task | yes |
| `{{review_status}}` | PASS / PASS_WITH_NOTES / NEEDS_FIX / BLOCKED | yes |
| `{{task_id}}` | Task ID or title | yes |
| `{{highest_severity}}` | P0 / P1 / P2 / P3 / NONE | yes |
| `{{next_skill}}` | Next recommended skill | yes |
| `{{code_files}}` | List of code files reviewed | yes |
| `{{test_run}}` | Yes / No | yes |
| `{{test_command}}` | Test command used | if test_run=Yes |
| `{{test_result}}` | Test output summary | if test_run=Yes |
| `{{explore_status}}` to `{{ac_notes}}` | Chain of Truth compliance per source | yes |
| `{{ac_criteria}}` | List of acceptance criteria | yes |
| `{{ac_check_status}}` | PASS / FAIL / PARTIAL per criteria | yes |
| `{{ac_evidence}}` | Evidence per criteria | yes |
| `{{fix_summary_list}}` | Numbered list of fixes (or empty if PASS) | if NEEDS_FIX |
| `{{fix_entries}}` | Full FIX-### blocks (see FIX template below) | if NEEDS_FIX |
| `{{execution_order}}` | YAML ordered fix list | if NEEDS_FIX |
| `{{total_required_fixes}}` | Count of required fixes | yes |
| `{{total_optional_fixes}}` | Count of optional improvements | yes |
| `{{must_rerun}}` | true / false | yes |
| `{{conclusion}}` | Final conclusion text | yes |
| `{{sources_checked}}` | List of artifacts and code read | yes |
| `{{assumptions}}` | Verified/unverified assumptions | yes |
| `{{actions_taken}}` | Summary of review actions | yes |
| `{{verification}}` | Verification result | yes |
| `{{report_summary}}` | 1-3 sentence summary | yes |
| `{{next_file}}` | Next file for executor to read | yes |
| `{{confidence}}` | low / medium / high | yes |
| `{{blocking_questions}}` | List or None | yes |
| `{{risks}}` | Risks to carry forward | yes |
| `{{source_of_truth}}` | Path to main artifact | yes |
| `{{must_preserve_ids}}` | SRC-### list | yes |
| `{{unresolved_ids}}` | SRC-### list | yes |
| `{{suggested_command}}` | Suggested next action | yes |

### FIX Entry Template

Each FIX entry in `{{fix_entries}}` follows this structure:

```markdown
### FIX-{n} — <title>

**Severity:** `P{n}`
**Target skill:** `<target>`
**Issue type:** `<BUG | REQUIREMENT_GAP | SRS_GAP | TASK_GAP | TEST_GAP | DOC_GAP | SECURITY | DATA_SAFETY>`

#### Problem

```text
Describe the issue briefly.
```

#### Location

```text
File: <path/file>
Area/Function: <function name / component / route>
Related artifact: <prd.md / srs.md / task-breakdown.md>
Related requirement: <section / AC / requirement id>
```

#### Expected

```text
Describe the expected behavior based on LCS artifacts.
```

#### Actual

```text
Describe the current implementation behavior.
```

#### Fix Instructions

```text
1. ...
2. ...
```

#### Validation After Fix

```text
- [ ] ...
- [ ] ...
```

#### Fix Request Copy

```markdown
# LCS Fix Request

Target skill: `<target>`

Source review: `FIX-{n}`

## Problem

...

## Location

...
```

---

## Review Procedure

1. Read all available LCS artifacts.
2. Identify the active task being reviewed.
3. Build a list of expected behavior from artifacts.
4. Read diff or changed files.
5. Match implementation against expected behavior.
6. Check acceptance criteria one by one.
7. Find mismatches, missing behavior, and scope creep.
8. Find potential bugs and edge cases.
9. Check security and data safety if relevant.
10. Check test coverage.
11. Determine severity for each issue.
12. Assign final review status.
13. Create fix handoff for `lcs-task-executor` if needed.

---

## Core Principles

- Review based on artifacts, not assumptions.
- Do not add new requirements.
- Do not edit code directly.
- Do not claim success without evidence.
- Do not produce overly generic reports.
- Every issue must have evidence.
- Every fix recommendation must be actionable.
- When in doubt, use PARTIAL or NEEDS_FIX, not PASS.
- Code review must help the executor fix issues clearly and precisely.
