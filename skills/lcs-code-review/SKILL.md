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

Workflow checklist
- [ ] Read `.lcs/state.md` to locate active work item folder
- [ ] Read task artifacts in Required Reading Order
- [ ] Phase 1: Setup — identify task, read artifacts, read diff
- [ ] Phase 2: Review — check Explore, PRD, PRD Enhance, SRS, Task Breakdown alignment
- [ ] Phase 2: Review — scan for bugs, security, error handling, test coverage, maintainability
- [ ] Phase 3: Report — produce `code-review.md` from template
- [ ] Phase 4: Validate — verify claims, confirm status, update state
- [ ] Write review report to `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md`
- [ ] Update `.lcs/state.md` with current_phase: code-review

## Output Artifact

- Save review report as: `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md`
- Artifact type: `code_review`
- Use the active work item folder from `.lcs/state.md`

## OKF Frontmatter & Writing Safety

- When creating review reports, include YAML frontmatter following the schema in `../lcs-shared/contract.md`.
- Follow the Artifact Writing Safety rules in contract.md — generate content first, write one file, verify, stop on failure.

## Chain of Truth Level

Level: Strict

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

## Phase 1: Setup

1. Read `.lcs/state.md` to locate active work item folder.
2. Read all available LCS artifacts in Required Reading Order.
3. Read diff or changed code files.
4. Build a list of expected behavior from artifacts.

## Phase 2: Review Execution

1. Check alignment with Explore, PRD, PRD Enhance, SRS, and Task Breakdown.
2. Scan for potential bugs (null handling, race conditions, edge cases, etc.).
3. Check security and data safety (auth, injection, exposure, etc.).
4. Check error handling and failure modes.
5. Review test coverage.
6. Review maintainability.
7. Determine severity (P0-P3) for each issue found.

## Phase 3: Report Writing

1. Copy template from `../lcs-code-review/assets/code-review-template.md`.
2. Replace all `{{placeholder}}` with actual review findings.
3. For each issue found, create a FIX-{n} entry with problem, location, expected vs actual, fix instructions, and validation.
4. Include Fix Request Copy block per FIX entry for executor consumption.
5. Add execution order and final status.
6. Write report to `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md`.

## Phase 4: Validation & Handoff

1. Verify all claims in the report are backed by evidence from artifacts or code.
2. Confirm final status (PASS / PASS_WITH_NOTES / NEEDS_FIX / BLOCKED).
3. Update `.lcs/state.md` with `current_phase: code-review`.
4. Present handoff for `lcs-task-executor` with required fixes and execution order.

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

---

## Gotchas & Anti-Patterns

- Do not review code you haven't read. Reading the diff is mandatory.
- Do not skip artifact reading order — missing upstream context leads to false positives.
- Do not assign P0/P1 without clear artifact evidence. Subjective preferences are P3 at most.
- Do not combine review and fix in one step. Review produces report; executor applies fixes.
- Do not claim `All tests passed` unless you actually ran them. State `Tests were not run` if not executed.
- Do not add requirements that don't exist in artifacts. Label suggestions as `Optional Improvement`.
- Do not produce a generic PASS when artifacts are missing. Use BLOCKED or PARTIAL_REVIEW.
- For NEEDS_FIX: always include Fix Request Copy so executor can work independently.
- For blocked reviews: clearly state which artifact is missing and what can't be verified.
- If tests exist but were not run, note this in the report — don't assume they pass.
- Security findings must cite specific code paths, not vague concerns.
- Do not refactor or restructure code in fix instructions. Keep instructions surgical.
- If the same bug appears in multiple files, create one FIX entry per distinct location.
- Separate mandatory fixes (P0/P1) from optional improvements (P2/P3). Mixing them confuses the executor.
- When the task scope is unclear, downgrade to PARTIAL_REVIEW rather than guessing intent.

---

## Chain of Truth Report

### Level
Strict

### Sources Checked
- Project source files, configs, and manifests
- LCS artifacts: explore.md, prd.md, prd-enhanced.md, srs.md, task-breakdown.md, task-###.md
- Task acceptance criteria
- Diff or changed code files
- `.lcs/state.md`

### Assumptions
- User has completed one or more tasks via lcs-task-executor before review
- Active work item is correctly set in `.lcs/state.md`
- Artifacts are in the canonical `.lcs/work-items/{timestamp}-{slug}/` path

### Plan
1. Phase 1: Setup — identify task, read artifacts, read diff
2. Phase 2: Review — check alignment, bugs, security, error handling, test coverage, maintainability
3. Phase 3: Report — populate template from `assets/code-review-template.md`
4. Phase 4: Validate — verify claims, confirm status, update state

### Actions Taken
- Read artifacts in Required Reading Order
- Reviewed implementation against each artifact
- Scanned for bugs, security issues, error handling gaps
- Checked test coverage and maintainability
- Assigned severity (P0-P3) per finding
- Produced `code-review.md` with FIX entries and execution order

### Verification
- Each finding cites artifact or code evidence
- Every non-trivial claim has a source reference
- Missing artifacts trigger BLOCKED or PARTIAL_REVIEW status
- Review status assigned per Final Review Status table

### Report
**Confidence**: Medium (varies by artifact completeness and code access)
**Limitations**: Claims without artifact confirmation marked accordingly; BLOCKED status when critical artifacts are missing

## Handoff

Next recommended skill: lcs-task-executor

Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/code-review.md

Current phase: code-review

Current confidence: medium

Blocking questions: None

Risks to carry forward: Unresolved fixes marked as FIX entries; executor must follow execution order

Source of Truth Bundle: .lcs/state.md, .lcs/work-items/{timestamp}-{slug-work-item}/explore.md, prd.md, srs.md, code-review.md

Must Preserve IDs: <SRC-### list from artifacts>

Unresolved IDs: <SRC-### list from artifacts>

Suggested next command: Execute fixes from code-review.md
