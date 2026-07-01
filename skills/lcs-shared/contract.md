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
These are project-level singletons - overwritten on each run. This exception overrides the timestamped folder convention for onboarding output.

## Artifact Files
Create only when relevant:
- explore.md
- debug.md
- prd.md
- prd-enhanced.md
- code-review.md
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

## OKF Frontmatter Schema

All LCS artifacts MUST include standard YAML frontmatter at the top of the file, delimited by `---` lines with no blank lines before it.

### Schema

```yaml
---
type: artifact
artifact_type: prd
status: draft
source: .lcs/work-items/{timestamp}-{slug}/explore.md
timestamp: 2026-07-01T09:27:22+07:00
resource: optional/path/or/url
previous_artifact: optional/path
next_artifact: optional/path
---
```

### Field Constraints

| Field | Type | Required | Allowed Values | Validation Rules |
|---|---|---|---|---|
| `type` | string | required | `artifact` | Must be exactly `artifact` |
| `artifact_type` | string | required | Must match registry | Must be one of the 16 values in the Artifact Type Registry |
| `status` | string | required | `draft`, `review`, `final` | If invalid, use `draft (invalid_frontmatter)` |
| `source` | string | required | Relative path | Must be relative path from repo root; must not escape `.lcs/`; must not be absolute or URL |
| `timestamp` | string | required | ISO 8601 | Format: `YYYY-MM-DDTHH:mm:ss±hh:mm` — regex: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$` |
| `resource` | string | optional | Path, URL, or reference | Validator checks existence if path |
| `previous_artifact` | string | optional | Relative path | Relative path to preceding artifact |
| `next_artifact` | string | optional | Relative path | Relative path to next artifact |

### Validation Rules

- Frontmatter is mandatory for all new artifacts from Phase 1 onward.
- If YAML schema is invalid, report the issue and write with `status: draft (invalid_frontmatter)`.
- Special YAML characters (colons `:`, quotes `"`, newlines) in values MUST be wrapped in double quotes.
- Empty/missing fields are treated as invalid — apply `invalid_frontmatter` marker.
- Timestamp MUST always include timezone offset.

## Artifact Type Registry

| Artifact | `artifact_type` value | Primary Skill | File Location |
|---|---|---|---|
| explore.md | `exploration` | lcs-explore | `.lcs/work-items/{ts}-{slug}/` |
| debug.md | `debug_report` | lcs-debug | `.lcs/work-items/{ts}-{slug}/` |
| prd.md | `prd` | lcs-toprd | `.lcs/work-items/{ts}-{slug}/` |
| prd-enhanced.md | `prd_enhanced` | lcs-prd-reviewer | `.lcs/work-items/{ts}-{slug}/` |
| code-review.md | `code_review` | lcs-code-review | `.lcs/work-items/{ts}-{slug}/` |
| srs.md | `srs` | lcs-tosrs | `.lcs/work-items/{ts}-{slug}/` |
| tests.md | `test_spec` | lcs-tosrs | `.lcs/work-items/{ts}-{slug}/` |
| api.md | `api_spec` | lcs-tosrs | `.lcs/work-items/{ts}-{slug}/` |
| db.md | `db_spec` | lcs-tosrs | `.lcs/work-items/{ts}-{slug}/` |
| traceability.md | `traceability` | lcs-tosrs | `.lcs/work-items/{ts}-{slug}/` |
| task-coverage.md | `task_coverage` | lcs-task-slicer | `.lcs/work-items/{ts}-{slug}/` |
| tasks.md / task-###.md | `task` | lcs-task-slicer | `.lcs/work-items/{ts}-{slug}/task/` |
| state.md | `state` | all skills | `.lcs/` |
| final-doc.md | `final_doc` | lcs-doc-finalizer | `.lcs/docs/{ts}-{slug}/` |
| index.md | `index` | all skills | `.lcs/work-items/{ts}-{slug}/` |
| onboarding.md | `onboarding` | lcs-onboarding | `.lcs/work-items/` |
| onboarding-map.md | `onboarding_map` | lcs-onboarding | `.lcs/work-items/` |

## Artifact Writing Safety

### Content-First / Write-Second

Generate complete artifact content in the planning/thinking stage first. Only after content is finalized, write it to file in a separate step. Never begin writing before content is fully generated.

### File Write Contract

When writing an artifact file, follow this exact 4-step sequence:

1. **Generate**: Produce complete artifact content (including frontmatter) in the current context.
2. **Write**: Write exactly one target file using the write tool.
3. **Verify**: Check the tool result — do not claim success unless the tool confirms success.
4. **Stop on Failure**: If the write tool fails, do not retry in the same step. Move to File Write Fallback.

### File Write Fallback

If the file write tool fails:

1. Output the full artifact content inside a fenced markdown code block.
2. Prefix the block with `(not saved)`.
3. State the target file path clearly above the block.
4. The human operator can manually save the content.

### One Artifact Write Per Step

A single model response MUST NOT generate and write more than one primary artifact file. Primary artifacts are files listed in the Artifact Type Registry. Supporting operations (reading files, updating state) may accompany but not replace the single write rule.

Exception: Skills with multiple output types (e.g., lcs-tosrs with 5 types, lcs-task-slicer with many task files) MUST use one-file-per-step write strategy across sequential steps — never in the same response.

### Model Capability Mode

When using an unstable model (limited or unreliable tool-calling capability):

- Prefer **content-first mode**: generate full content, present for preview, save only on explicit confirmation.
- **Avoid multi-file writes**: The one-artifact-per-step rule is strict for unstable models.
- **Artifact preview**: Before writing, present the artifact content in a code block for human review.
- **Fallback default**: Unstable models should default to File Write Fallback (output as text, mark `(not saved)`) rather than risking failed writes.

### Planner / Reviewer / Executor Role Guidance

Some models (e.g., Nemotron 3 Ultra, routed/free/open-weight models) have unreliable tool-calling. Assign roles based on capability:

| Model Type | Suitable Role | Unsuitable Role |
|---|---|---|
| Stable tool-calling | Executor, Writer | — |
| Unstable tool-calling | Planner, Reviewer | Executor, Writer |

Unstable models SHOULD generate plans and reviews that stable models execute. If an unstable model must write, use content-first mode with fallback.

### Reduce Strictness During Write Steps

Planning and review steps follow the full formatting schema. Write steps use simplified instructions:

- Focus on getting content written correctly.
- Frontmatter validation is relaxed — invalid frontmatter gets `status: draft (invalid_frontmatter)` rather than blocking the write.
- Post-write cleanup and correction can happen in subsequent steps.

### Frontmatter Validation at Write Time

When writing an artifact:

1. Validate YAML frontmatter against the schema (field types, required fields, allowed values).
2. If frontmatter is valid: write with the appropriate `status` value.
3. If frontmatter is invalid: report the validation issue, write the artifact with `status: draft (invalid_frontmatter)`.
4. Never block artifact writing due to frontmatter validation failure — the artifact is still useful with the error marker.
5. Fix invalid frontmatter in a subsequent review/correction step.

## Chain of Truth

### Canonical Level Mapping

| Level | Skills |
|---|---|
| Light | lcs-explore |
| Standard | lcs-toprd, lcs-onboarding, lcs-debug, lcs-self-improvement |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc, lcs-code-review |
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
