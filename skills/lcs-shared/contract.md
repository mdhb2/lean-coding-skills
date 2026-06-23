# Shared Coding Workflow Contract

This file defines canonical artifact format, folder conventions, Handoff section, and token-optimization rules used by all skills in this pack.

## Folder Convention
All runtime artifacts live under:
```
.lcs/work-items/<timestamp>-<slug-work-item>/
```

### Skill-Specific Exception: `lcs-doc-finalizer`
When active skill is `lcs-doc-finalizer`, documentation outputs use dedicated docs subtree:
```
.lcs/docs/<timestamp>-<slug-work-item>/
```
Index file for this subtree:
```
.lcs/docs/docs-index.md
```
Archive target for finalized source artifacts:
```
.lcs/archive/<timestamp>-<slug-work-item>/
```
This exception overrides generic docs/archive path assumptions in other rules.

### Skill-Specific Exception: `lcs-codebase-doc`
When active skill is `lcs-codebase-doc`, repository documentation outputs use:
```
.lcs/codebase/
```
Project intent documents are read from:
```
.lcs/docs/
```
This exception overrides generic runtime artifact path assumptions for codebase mapping and repository documentation outputs.

### Skill-Specific Exception: `lcs-self-improvement`
When active skill is `lcs-self-improvement`, diagnostic output uses timestamped path:
```
.lcs/docs/self-improvements/<timestamp>-analysis.md
```
Supporting files:
```
.lcs/docs/self-improvements/state.json
.lcs/docs/self-improvements/index.md
```
This report is diagnostic-only and does not apply changes automatically.
This exception overrides generic runtime artifact path assumptions for self-improvement analysis output.

## Artifact Files
Create only when relevant:
- explore.md
- debug.md
- prd.md
- tasks.md
- state.md
- final-doc.md

## Handoff
Must appear at bottom of every artifact:
```markdown
## Handoff

Next recommended skill:
Next file to read:
Current phase:
Current confidence:
Blocking questions:
Risks to carry forward:
Suggested next command:
```

## Chain of Truth

### Canonical Level Mapping

| Level | Skills |
|---|---|
| Light | lcs-explore |
| Standard | lcs-toprd, lcs-onboarding, lcs-debug, lcs-self-improvement |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc |
| Very Strict | lcs-task-executor, lcs-task-executer (legacy), lcs-debug-ext |
| Meta | lcs-chain-of-truth (protocol, not self-applied) |

### Report Placement Rule

Any artifact using the Chain of Truth protocol **must** place the `## Chain of Truth Report` section **before** the `## Handoff` section.

### Verification Rule

Verify where available. For markdown-only repos: check file existence, grep for content, run `git diff --check`. Do not claim verification passed unless it was actually performed.

## Token Optimization Rules
1. Read state.md first when continuing work.
2. Avoid reading all artifacts unless necessary.
3. Use Affected Areas / Files from PRD to narrow code inspection.
4. Executor focuses on one task at a time.
5. Update canonical files rather than create versions.
