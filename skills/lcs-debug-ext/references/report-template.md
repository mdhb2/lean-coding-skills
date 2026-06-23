# LCS Debug Ext Report Template

Use this template for `.lcs/work-items/{timestamp}-{slug-work-item}-debug-ext/debug.md`.

```markdown
# LCS Debug Ext Report

## Scope
**Generated from:** [current task / supplied files / supplied folders / logs / combined sources]
**Output directory:** `.lcs/work-items/{timestamp}-{slug-work-item}-debug-ext/`
**Report path:** `.lcs/work-items/{timestamp}-{slug-work-item}-debug-ext/debug.md`
**Changes applied:** None

## Bug Summary
[Short description of the reported bug.]

## Current Status
**Reproduction status:** [Reproduced / Partially reproduced / Not reproduced / Evidence-only]
**Confidence:** [High / Medium / Low]
**Recommended next step:** [TODO]

## Available Evidence
- [Evidence item with path, command, or source]
- [TODO]

## Expected vs Actual
**Expected:** [TODO]
**Actual:** [TODO]

## Feedback Loop
**Loop type:** [test / CLI / curl / harness / manual / HITL / none]
**Command or steps:**

```bash
[TODO]
```

**Signal quality:** [Strong / Moderate / Weak / Missing]

## Ranked Hypotheses

### 1. [Hypothesis Name]
**Confidence:** [High / Medium / Low]
**Reasoning:** [TODO]
**Supporting evidence:** [TODO]
**Would disprove:** [TODO]
**Prediction:** If [X] is the cause, then [Y] should be observed, and [Z] should confirm or disprove it.
**How to verify:** [TODO]

---

## Investigation Notes
- [Confirmed fact]
- [Hypothesis]
- [Limitation]

## Targeted Instrumentation Plan
**Debug prefix:** `[DEBUG-lcs-xxxx]`

| Hypothesis | Probe | Expected signal | Cleanup |
| ---------- | ----- | --------------- | ------- |
| [TODO] | [TODO] | [TODO] | `grep -R "\[DEBUG-lcs-xxxx\]" .` |

## Suspected Root Cause
[Confirmed / Probable / Unknown]

[Explanation.]

## Patch Proposal
**Changes applied:** None

### Summary
[What should be changed.]

### Files likely affected
- `[TODO]`

### Before / After

Before:

```text
[TODO]
```

After:

```text
[TODO]
```

### Proposed diff

```diff
[TODO]
```

### Risk
[Low / Medium / High]

### Validation

```bash
[TODO]
```

### Rollback
[TODO]

## Regression-Test Options

### Recommended Option
[Regression test / smoke test / no good test seam]

**Why:** [TODO]

### Proposed Test
**File:** `[TODO]`
**Test name:** `[TODO]`
**Command:**

```bash
[TODO]
```

## Cleanup Checklist
- [ ] Remove temporary debug logs using prefix `[DEBUG-lcs-xxxx]`.
- [ ] Remove throwaway harnesses or move them to `.lcs/work-items/{timestamp}-{slug-work-item}-debug-ext/`.
- [ ] Confirm no generated debug artifacts are outside `.lcs/work-items/{timestamp}-{slug-work-item}-debug-ext/`.
- [ ] Confirm no source files were modified by this skill.

## Post-Mortem
**What caused the issue?** [TODO]
**What would have prevented it?** [TODO]
**What should be improved?** [TODO]

## Handoff / Follow-Up
[Recommend follow-up skill or workflow if needed.]

Examples:
- If architecture prevents testing, recommend architecture improvement.
- If codebase knowledge is missing, recommend `lcs-codebase-doc`.
- If recurring debugging friction appears, recommend `lcs-self-improvement`.

## Open Questions
1. [ASK USER]

## Limitations
- [TODO]

## Chain of Truth Report
Level: Very Strict

### Sources Checked
- [List all files read, commands run, logs inspected â€” with exact paths]

### Assumptions
- [verified/unverified] [Assumption text]

### Plan Before Action
1. [Step taken before any action]

### Actions Taken
- [Exact commands run with stdout/stderr captured]
- [Files written or read]

### Verification
- [All checks run; results quoted verbatim]
- [If no test seam: document why and mark [unverified]]

### Blocked Items
[None, or list with reasons]

### Confidence
[High / Medium / Low] â€” [justification]

### Risk Notes
[None, or outstanding concerns]

## Handoff
Next recommended skill: <skill-name>
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}-debug-ext/debug.md
Current phase: debug
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <short>
Suggested next command: <command>
```
