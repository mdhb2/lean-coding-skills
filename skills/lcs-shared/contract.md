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

> **Templates:** For exact structure of each artifact type, read `templates/{artifact_type}.template.md`. Only load when generating new artifact — not during review or execution.

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
- tasks.md (deprecated; lcs-task-slicer now emits task-coverage.md + task/task-###.md)
- state.md
- final-doc.md (deprecated; lcs-doc-finalizer now emits doc.md + map.md)

## Requirement Preservation Rule

> **SRC-### ID Convention:** All source requirements use `SRC-###` prefix. Acceptance criteria use `AC-###`. All IDs must be preserved through the entire chain (explore → PRD → SRS → task → code-review). See `templates/traceability.template.md` for matrix format.

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

## OKF Frontmatter Schema (v2 — OKF v0.2 Compliant)

> **Full schema + all templates:** `templates/okf-schema.md` and `templates/*.template.md`

All LCS artifacts MUST include YAML frontmatter per [OKF v0.2 spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).
Full schema + templates: `lcs-shared/templates/okf-schema.md`

### Schema (merged OKF + LCS)

```yaml
---
# OKF Required
title: "PRD: feature-name"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-toprd"
created: "2026-07-01"
updated: "2026-07-01"

# OKF Recommended
tags: [prd, requirements]
summary: "One-sentence summary"
status: draft
related: ["explore.md"]

# LCS Extensions
artifact_type: prd
artifact_id: "SRC-001"
source: "explore.md"
cot_level: standard
version: "1.0"
---
```

### OKF Required Fields

| Field | Type | Description |
|---|---|---|
| `title` | string | Descriptive title |
| `format_version` | string | Always `"okf/0.2"` |
| `authors` | list | `[{type: "human"\|"agent", name: "...", id: "..."?}]` |
| `created` | ISO-8601 | `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SSZ` |
| `updated` | ISO-8601 | Last updated |

### OKF Recommended Fields

| Field | Type | Description |
|---|---|---|
| `tags` | list[string] | Topics/categories |
| `summary` | string | One-sentence summary |
| `status` | enum | `draft` → `reviewed` → `active` → `archived` |
| `related` | list[string] | Paths to related artifacts |

### LCS Extension Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `artifact_type` | enum | yes | Must match registry below |
| `artifact_id` | string | no | Traceability ID (`SRC-###`, `FR-###`, etc.) |
| `source` | string | yes | Relative path to source artifact |
| `cot_level` | enum | yes | `light` / `standard` / `strict` / `very_strict` |
| `version` | string | no | Default `"1.0"` |

### Status Lifecycle

```
draft → reviewed → active → archived
```

| Status | Meaning | Set by |
|---|---|---|
| `draft` | Work in progress | Creating skill |
| `reviewed` | Reviewed, may have notes | lcs-prd-reviewer, lcs-code-review |
| `active` | Approved, ready for execution | User approval |
| `archived` | Finalized, immutable | lcs-doc-finalizer |

### Validation Rules

Frontmatter mandatory for all artifacts. Invalid YAML → report issue, write `status: draft (invalid_frontmatter)`.
Special YAML characters (colons, quotes, newlines) MUST be wrapped in double quotes.
Empty/missing required fields → apply `invalid_frontmatter` marker.

### Templates

All 18 artifact templates available in `lcs-shared/templates/{artifact_type}.template.md`.
Copy template → rename → fill frontmatter → write content.

## Artifact Type Registry (Quick Reference)

Full definitions + templates: `lcs-shared/templates/okf-schema.md`

| `artifact_type` | File(s) | Primary Skill | CoT Level |
|---|---|---|---|
| `explore` | explore.md | lcs-explore | light |
| `prd` | prd.md | lcs-toprd | standard |
| `prd_enhanced` | prd-enhanced.md | lcs-prd-reviewer | strict |
| `srs` | srs.md | lcs-tosrs | strict |
| `tests` | tests.md | lcs-tosrs | strict |
| `api` | api.md | lcs-tosrs | strict |
| `db` | db.md | lcs-tosrs | strict |
| `traceability` | traceability.md | lcs-tosrs | strict |
| `task_coverage` | task-coverage.md | lcs-task-slicer | strict |
| `task` | task-###.md | lcs-task-slicer/executor | very_strict |
| `debug` | debug.md | lcs-debug | standard |
| `debug_ext` | debug.md | lcs-debug-ext | very_strict |
| `code_review` | code-review.md | lcs-code-review | strict |
| `codebase_doc` | *.md (7 files) | lcs-codebase-doc | strict |
| `onboarding` | onboarding.md | lcs-onboarding | standard |
| `onboarding_map` | onboarding-map.md | lcs-onboarding | standard |
| `final_doc` | doc.md | lcs-doc-finalizer | strict |
| `final_map` | map.md | lcs-doc-finalizer | strict |
| `analysis` | {ts}-analysis.md | lcs-self-improvement | standard |
| `session_log` | session-log.md | lcs-master | standard |
| `domain_model` | CONTEXT.md | lcs-domain-modeling | standard |
| `research` | research.md | lcs-research | standard |
| `prototype` | prototype.md | lcs-prototype | strict |
| `wayfinder` | wayfinder.md | lcs-wayfinder | strict |
| `wizard` | wizard.md | lcs-wizard | standard |
| `execution_log` | session-log.md | lcs-master | standard |

### Artifact ID Prefixes

| Prefix | Used In | Example |
|---|---|---|
| `SRC-###` | prd.md, prd-enhanced.md | `SRC-001: User authentication` |
| `FR-###` | srs.md | `FR-001: Login endpoint` |
| `BR-###` | srs.md | `BR-001: Password policy` |
| `VR-###` | srs.md | `VR-001: Email format` |
| `EC-###` | srs.md | `EC-001: Concurrent login` |
| `TEST-###` | tests.md | `TEST-001: Login success` |
| `API-###` | api.md | `API-001: POST /auth/login` |
| `DB-###` | db.md | `DB-001: users table` |
| `task-###` | task-###.md | `task-001: Implement login` |
| `DBG-###` | debug.md | `DBG-001: Login timeout` |

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
| Very Strict | lcs-task-executor, lcs-debug-ext |
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


---

## Pruning Checklist (For Skill Creators)

Before adding any instruction to a SKILL.md, ask:

1. **Does this change agent behavior?** If the instruction is "think carefully" or "follow the rules" — it's a no-op. Delete it.
2. **Can this be verified mechanically?** If not, make it specific: replace "run tests" with "run `npm test` and capture exit code 0".
3. **Is this already stated elsewhere?** Don't repeat rules from `contract.md` or `AGENTS.md`. Use context pointers instead.
4. **Is this a leading word or a vague directive?** "tight loop" anchors behavior. "do your best" does not. Use leading words.
5. **Would a senior developer approve this instruction?** If it reads like a placeholder or wishful thinking, rewrite or remove.
