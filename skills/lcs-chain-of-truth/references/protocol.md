# Chain of Truth Protocol — Full Reference

## Overview

This document defines the behavioral rules for each of the 6 Chain of Truth stages. Every stage has mandatory requirements for agents. No stage may be skipped; if a stage is not applicable, the agent must explicitly state "Not applicable" with a reason.

---

## 1. Source

### Rule
Agent must identify the source of truth before making any claim.

### Acceptable Sources
- User request
- `AGENTS.md`
- `README.md`
- `PRD.md`
- `SRS.md`
- `ARCHITECTURE.md`
- `DATABASE.md`
- `ROADMAP.md`
- Source code (`.py`, `.js`, `.ts`, `.rs`, etc.)
- Test files
- `.lcs/` artifacts (state.md, prd.md, task files, etc.)

### Behavior
- List all sources consulted at the top of the Chain of Truth Report.
- If a source referenced in the report does not exist: say "Source X referenced but not found."
- If two sources disagree on a fact that affects correctness: **halt**, surface the conflict, and ask for resolution before continuing.

### Example
```
Sources Checked:
- AGENTS.md (section 3, line 21)
- PRD.md (acceptance criteria 4)
- .lcs/state.md (active work item)
```

---

## 2. Assumption

### Rule
List every assumption made during execution. Each assumption must carry a status.

### Status Options
| Status | Meaning |
|---|---|
| **Safe** | Confirmed through source check or prior verification |
| **Risky** | Plausible but could cause issues if wrong |
| **Needs confirmation** | Cannot verify with available tools; requires human check |

### Behavior
- Flag unverifiable assumptions explicitly.
- If an assumption later proves false, note it in the Report.

### Example
```
Assumptions:
- Safe: SKILL.md does not exist yet (Test-Path returned False)
- Risky: skill folder naming convention follows pattern
- Needs confirmation: no other config file references this skill
```

---

## 3. Plan

### Rule
Produce a short, enumerable plan (3–7 steps) before editing any files.

### Requirements
- Plan must be **verifiable** — each step should have a clear completion criterion.
- Plan must be produced **before** any Action begins.
- Plan may be iterative (new steps discovered mid-execution), but initial plan must be stated upfront.

### Behavior
- Number each step.
- After execution, mark each step as `done` or `deviated` with explanation.

### Example
```
Plan:
1. Create folder (Test-Path after → True)
2. Write SKILL.md with frontmatter (grep check)
3. Append CoT section (Select-String check)
4. Verify no existing files modified (git diff)
```

---

## 4. Action

### Rule
Surgical edits only. Touch only files explicitly listed in the task scope.

### Behavioral Rules
- Touch only relevant files — no scope creep.
- Preserve existing style, formatting, and conventions.
- Zero cosmetic churn — do not clean up adjacent code.
- Avoid broad rewrites — prefer append or targeted insert.
- No new dependencies without justification in the Report.
- No rename without a compatibility plan.
- Do not remove legacy paths until verification confirms they are unused.

### Behavior
- Record every file created or modified with exact path.
- For each action: state what was done, not why (why belongs in Plan).

### Example
```
Actions Taken:
- Created: .claude/skills/lcs-chain-of-truth/SKILL.md (42 lines)
- Modified: AGENTS.md (appended section 9, lines 158-203)
```

---

## 5. Verification

### Rule
Attempt verification if tools are available. Document the result — never skip.

### Fallback Rules
For **markdown-only repos** (no test runner):

| Check Type | Method |
|---|---|
| File existence | `Test-Path <path>` |
| Content presence | `Select-String -Path <path> -Pattern <pattern>` |
| No unintended changes | `git diff --check` |
| Broken links | Manual README link check |

### Generic Fallback
- Run `git diff --check` to detect whitespace errors.
- If a check cannot be run: explain why in the Report and provide manual verification steps.

### Behavior
- Record the exact command and its stdout/stderr output.
- Do **not** claim "verified" without performing the check.

### Example
```
Verification:
- Test-Path .claude/skills/lcs-chain-of-truth/SKILL.md → True ✓
- Select-String -Pattern "name: lcs-chain-of-truth" → match ✓
- git diff --check → exit 0 ✓
```

---

## 6. Report

### Rule
Produce the Chain of Truth Report before the `## Handoff` section. This is the final stage — no further work after the Report.

### Required Fields
| Field | Description |
|---|---|
| Level | Light, Standard, Strict, or Very Strict |
| Sources Checked | List of all sources consulted |
| Assumptions | List with status (Safe / Risky / Needs confirmation) |
| Plan Followed | Steps executed and their outcomes |
| Actions Taken | Files created or modified |
| Verification | Command(s) run and their results |
| Risks / Notes | Outstanding risks, unverified items, or deferred work |

### Behavior
- Be honest. If something failed, state it. If something is unverifiable, flag it.
- No "assumed passing" — every check outcome must be explicit.
- For Very Strict level: include `Proof of Result` subsection with quoted command outputs.

### Example
```
## Chain of Truth Report

### Level
Very Strict

### Sources Checked
...

### Assumptions
...

### Plan Followed
...

### Actions Taken
...

### Verification
...

### Proof of Result
```
Test-Path ... → True
```

### Risks / Notes
...
```

---

## Source Conflict Behavior

If two sources disagree on a fact that affects correctness:

1. Stop execution.
2. Surface the conflicting facts, citing exact sources and line numbers.
3. Ask for resolution: "Source A says X, Source B says Y. Which is correct?"
4. Do not continue until user resolves the conflict.

### Example
```
CONFLICT DETECTED:
- AGENTS.md section 6 line 52: "The folder name on disk MUST exactly match the name: field"
- TASK-001: says folder should be lcs-chain-of-truth but SKILL.md says name: lcs-chain-of-truth-different

RESOLUTION REQUIRED: Which name is canonical?
```

---

## Verification Fallback (Markdown Repos)

If no test suite exists:

| Fallback | Method |
|---|---|
| File existence | `Test-Path` |
| Content matching | `Select-String` |
| No regression | `git diff --check` |
| Link validity | Manual README link verification |

Never claim "verified" without running the check. If neither automated nor manual check is possible: mark as `[unverified]` with a reason.
