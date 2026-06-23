# Shared Coding Workflow Contract

This file defines canonical artifact format, folder conventions, Handoff section, and token-optimization rules used by all skills in this pack.

## Folder Convention
All runtime artifacts live under:
```
.lcs/work-items/{timestamp}-{slug-work-item}/
```

### Skill-Specific Exception: `lcs-doc-finalizer`
When active skill is `lcs-doc-finalizer`, documentation outputs use dedicated docs subtree:
```
.lcs/docs/{timestamp}-{slug-work-item}/
```
Index file for this subtree:
```
.lcs/docs/docs-index.md
```
Archive target for finalized source artifacts:
```
.lcs/archive/{timestamp}-{slug-work-item}/
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
.lcs/docs/self-improvements/{timestamp}-analysis.md
```
Supporting files:
```
.lcs/docs/self-improvements/state.json
.lcs/docs/self-improvements/index.md
```
This report is diagnostic-only and does not apply changes automatically.
This exception overrides generic runtime artifact path assumptions for self-improvement analysis output.

### Skill-Specific Exception: `lcs-onboarding`
When active skill is `lcs-onboarding`, outputs use flat singleton paths (no timestamp or slug folder):
```
.lcs/work-items/onboarding.md
.lcs/work-items/onboarding-map.md
```
These are project-level singletons â€” overwritten on each run. This exception overrides the timestamped folder convention for onboarding output.

## Artifact Files
Create only when relevant:
- explore.md
- debug.md
- prd.md
- prd-enhanced.md
- srs.md
- tests.md
- api.md
- db.md
- traceability.md
- task-coverage.md
- tasks.md
- state.md
- final-doc.md

## Requirement Preservation Rule

Every user-provided instruction, explicit constraint, or requirement bullet must receive a stable `SRC-###` identifier in the PRD phase. Once assigned, downstream skills must preserve the `SRC-###` unless the requirement is intentionally removed and documented with a reason.

- Use `P0` for must-not-drop requirements that define correctness, safety, security, compatibility, or explicit user constraints.
- Use `P1` for important requirements that should be implemented unless scope changes.
- Use `P2` for nice-to-have guidance, preferences, or low-risk refinements.
- P0 requirements must not be summarized away. They must appear in downstream traceability either as covered or explicitly unresolved.
- If an artifact has a Source Requirement Ledger, downstream skills must preserve every listed `SRC-###` or block with a clear gap report.

## Source of Truth Bundle

Downstream skills must not ignore enhanced upstream artifacts. Read available artifacts in this order unless a skill-specific rule is stricter:

1. `.lcs/state.md` to locate the active work item.
2. `prd-enhanced.md` if present. This is the authoritative PRD.
3. `prd.md` as baseline fallback and source ledger baseline.
4. `source-ledger.md` if present for legacy/source-only workflows.
5. `srs.md` if present for deterministic requirement decomposition.
6. `tests.md` if present for test coverage mapping.
7. `api.md` and `db.md` if present for implementation contracts.
8. `traceability.md` if present for ID mapping.

If `prd-enhanced.md` exists but was not read, stop and report a source conflict. Do not proceed from `prd.md` alone when enhanced PRD exists.

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
Source of Truth Bundle:
Must Preserve IDs:
Unresolved IDs:
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

## Traceability Validation

Use the bundled validator after SRS generation, task slicing, and execution when artifacts exist.

- On win32: run `powershell -ExecutionPolicy Bypass -File .\skills\lcs-shared\scripts\validate-traceability.ps1 -WorkItemPath <path>`.
- On non-win32: run `python3 ./skills/lcs-shared/scripts/validate-traceability.py --work-item <path>`.
- If Python is not installed on non-win32, stop and ask the user to install Python 3 before validation.

Validation checks:
- all `SRC-###` IDs are preserved from `prd.md` to `prd-enhanced.md` when enhanced PRD exists
- every `AC-###` has a `TEST-###` mapping when `tests.md` exists
- every `AC-###` and `FR-###` has task coverage when task files exist
- every task has Source coverage
- `## Chain of Truth Report` appears before `## Handoff`
