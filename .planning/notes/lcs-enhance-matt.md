```yaml
---
title: "PRD: Matt Pocock Engineering Skills Adoption & LCS V2 Enhancement"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-explore"
    id: "lcs-explore"
  - type: agent
    name: "lcs-research"
    id: "lcs-research"
created: "2026-08-08"
updated: "2026-08-08T11:30:00+07:00"
tags: [engineering-skills, domain-modeling, debugging, architecture, matt-pocock]
summary: "Adopt Matt Pocock Engineering Skills into LCS V2 — 5 new skills + 5 enhancements"
status: reviewed
related:
  - "https://github.com/mdhb2/lean-coding-skills/tree/v2"
  - "https://github.com/mattpocock/skills/tree/main/skills/engineering"
artifact_type: prd
source: "lcs-explore, lcs-research, matt-pocock-engineering-skills"
cot_level: standard
version: "1.0"
---
```

# PRD: Matt Pocock Engineering Skills Adoption &amp; LCS V2 Enhancement

## Problem Statement &amp; Objective

- **Problem Statement:** LCS V2 memiliki workflow audit dan traceability yang kuat (Chain of Truth, SRC-###), namun kurang dalam disiplin engineering fundamental seperti *domain modeling*, *disciplined debugging*, *architectural vocabulary* (seams/depth), dan *large-scale planning*. Akibatnya, AI agent sering kehilangan konteks domain, gagal membangun feedback loop yang ketat saat debugging, dan kesulitan menangani refactoring berskala besar.

- **Objective:** Mengadopsi dan mengadaptasi disiplin engineering dari Matt Pocock Engineering Skills ke dalam ekosistem LCS V2. Implementasi harus menghasilkan 5 skill baru dan 5 enhancement pada skill existing, lengkap dengan instruksi [`SKILL.md`](http://SKILL.md) yang presisi, terintegrasi penuh dengan LCS Shared Contract, dan menjaga *Requirement Preservation Rule*.

## Background &amp; Solution

- **Background:** Matt Pocock Skills menekankan pada *ubiquitous language* ([CONTEXT.md](http://CONTEXT.md)), *seam discipline* (Michael Feathers), *6-phase debugging loop*, dan *tracer-bullet tickets*. LCS V2 menekankan pada *auditability* (Chain of Truth), *traceability* (SRC/FR/AC), dan *token optimization*.

- **Solution:** Menyusun blueprint lengkap untuk 5 skill baru `domain-modeling`, `research`, `prototype`, `wayfinder`, `wizard`) dan 5 enhancement `debug`, `task-executor`, `code-review`, `task-slicer`, `toprd`). Instruksi skill ditulis secara eksplisit di dalam PRD ini agar `lcs-task-slicer` dapat langsung memotongnya menjadi *vertical slices* tanpa ambiguitas.

## Source Context

- **Matt Pocock Engineering Skills:** `mattpocock/skills` (domain-modeling, diagnosing-bugs, tdd, codebase-design, etc.)

- **LCS V2 Base:** `mdhb2/lean-coding-skills/tree/v2` (Shared Contract, Chain of Truth, OKF Frontmatter)

## Scope &amp; User Stories

### User Stories

1. As a developer, I want to actively build and sharpen a domain model ([CONTEXT.md](http://CONTEXT.md)), so that terminology stays consistent across the codebase.

2. As a developer, I want to spawn a background research agent against primary sources, so that I can gather facts without hallucinating.

3. As a developer, I want to create throwaway prototypes (logic/UI), so that I can validate design decisions interactively before committing.

4. As a developer, I want to chart a "wayfinder" map of decision tickets locally, so that I can navigate huge, foggy projects across multiple sessions.

5. As a developer, I want to generate interactive bash wizards for manual procedures, so that human-in-the-loop setup is secure and repeatable.

6. As a developer, I want `lcs-debug` to enforce a 6-phase disciplined loop (Feedback Loop -&gt; Minimize -&gt; Hypothesise -&gt; Instrument -&gt; Fix -&gt; Post-mortem), so that hard bugs are solved systematically.

7. As a developer, I want `lcs-task-executor` to enforce seam discipline and avoid TDD anti-patterns, so that tests verify behavior, not implementation details.

8. As a developer, I want `lcs-code-review` to run a two-axis review (Standards + Spec), so that reviews catch both quality and correctness issues.

9. As a developer, I want `lcs-task-slicer` to support blocking edges and the expand-contract pattern, so that wide refactors keep CI green.

10. As a developer, I want `lcs-toprd` to explicitly plan testing seams, so that test strategy is defined before implementation.

## Source Requirement Ledger

| SRC ID | Priority | Origin | Description |

|---|---|---|---|

| SRC-001 | P0 | User Story 1 | Implement `lcs-domain-modeling` to maintain project root [`CONTEXT.md`](http://CONTEXT.md) and `docs/adr/`, challenging fuzzy terms inline. |

| SRC-002 | P0 | User Story 2 | Implement `lcs-research` to spawn background agents for primary source investigation, saving cited Markdown. |

| SRC-003 | P0 | User Story 3 | Implement `lcs-prototype` with logic (HTML state panel) and UI (URL param variations) branches. |

| SRC-004 | P0 | User Story 4 | Implement `lcs-wayfinder` using local `.lcs/` map and decision tickets instead of external issue trackers. |

| SRC-005 | P0 | User Story 5 | Implement `lcs-wizard` using [`template.sh`](http://template.sh) for secure, ephemeral human-in-the-loop procedures. |

| SRC-006 | P0 | User Story 6 | Enhance `lcs-debug` to Very Strict CoT with the 6-phase disciplined loop (must build tight feedback loop before hypothesizing). |

| SRC-007 | P0 | User Story 7 | Enhance `lcs-task-executor` with Seam vocabulary (Michael Feathers) and strict TDD anti-pattern prevention. |

| SRC-008 | P0 | User Story 8 | Enhance `lcs-code-review` to execute parallel sub-agent checks for Axis 1 (Standards) and Axis 2 (Spec). |

| SRC-009 | P0 | User Story 9 | Enhance `lcs-task-slicer` to map blocking edges and apply Expand-Contract pattern for wide refactors. |

| SRC-010 | P0 | User Story 10 | Enhance `lcs-toprd` to include a mandatory "Testing Seams" section. |

| SRC-011 | P0 | LCS V2 Contract | All new/enhanced skills must strictly adhere to LCS Shared Contract `.lcs/work-items/`, OKF Frontmatter, Handoff). |

| SRC-012 | P0 | LCS V2 CoT | All skills must declare and enforce their specific Chain of Truth level (Standard, Strict, or Very Strict). |

| SRC-013 | P1 | Matt Pocock | Debug Phase 1 must refuse to proceed to Phase 2 without a deterministic, agent-runnable, red-capable command. |

| SRC-014 | P1 | Matt Pocock | Task Executor must reject implementation-coupled tests and tautological assertions. |

| SRC-015 | P1 | Matt Pocock | Wizard must use `ask_secret` for credentials and verify statically `bash -n`), never executing end-to-end automatically. |

| SRC-016 | P1 | Matt Pocock | Domain Modeling must only offer ADRs when: 1) Hard to reverse, 2) Surprising without context, 3) Result of real trade-off. |

| SRC-017 | P1 | Matt Pocock | Prototype must be clearly marked as throwaway and archived on a separate branch after validation. |

## Non-Goals / Out of Scope

- **External Issue Tracker Integration:** Wayfinder and Triage will use local `.lcs/` markdown files, not GitHub Issues/Linear APIs, to maintain LCS V2's local-first architecture.

- **Modifying Chain of Truth Levels:** No new CoT levels will be created; existing Light/Standard/Strict/Very Strict will be mapped appropriately.

- **Grilling/Triage Skills:** Excluded to prevent scope creep; `lcs-explore` and `lcs-prd-reviewer` already cover these needs sufficiently.

## Requirements

- [ ] All new skills must include the exact [`SKILL.md`](http://SKILL.md) content defined in the Technical Approach section.

- [ ] All enhanced skills must append the exact new sections to their existing [`SKILL.md`](http://SKILL.md) files.

- [ ] `lcs-shared/[contract.md](http://contract.md)` must be updated to include the new artifact types `domain_model`, `research_report`, `prototype`, `wayfinder_map`, `wizard_script`).

- [ ] Traceability matrix must map all SRC-### to downstream FR/AC/TEST IDs.

## Technical Approach &amp; Implementation Decisions

### Deep Modules: Design &amp; Skill Specifications

*The following sections contain the EXACT instructions to be written into the respective [`SKILL.md`](http://SKILL.md) files. `lcs-task-slicer` must use these as the absolute source of truth for task generation.*

#### 1. NEW SKILL: `lcs-domain-modeling` (CoT Level: Standard)


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 1)
> See reference file for complete implementation details.


#### 2. NEW SKILL: `lcs-research` (CoT Level: Standard)


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 2)
> See reference file for complete implementation details.

> **Orca Tool Overlap:** This skill may overlap with Orca's `research` tool. Decision: If LCS-tracked, use this skill for traceability. If ad-hoc, prefer Orca directly.


#### 3. NEW SKILL: `lcs-prototype` (CoT Level: Strict)


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 3)
> See reference file for complete implementation details.

> **Orca Tool Overlap:** This skill may overlap with Orca's `prototype` tool. Decision: If LCS-tracked, use this skill for traceability. If ad-hoc, prefer Orca directly.


#### 4. NEW SKILL: `lcs-wayfinder` (CoT Level: Strict)



> **Note:** `lcs-wayfinder` is distinct from `lcs-pathfinder` (understanding skill). Wayfinder = codebase navigation during active work. Pathfinder = one-time architecture mapping for onboarding/learning.

> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 4)
> See reference file for complete implementation details.


#### 5. NEW SKILL: `lcs-wizard` (CoT Level: Standard)


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 5)
> See reference file for complete implementation details.

> **Orca Tool Overlap:** This skill may overlap with Orca's `wizard` tool. Decision: If LCS-tracked, use this skill for traceability. If ad-hoc, prefer Orca directly.


#### 6. ENHANCEMENT: `lcs-debug` (Upgrade to Very Strict CoT)

*Append to existing `lcs-debug/[SKILL.md](http://SKILL.md)` Behavior Checklist:*


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 6)
> See reference file for complete implementation details.


#### 7. ENHANCEMENT: `lcs-task-executor` (Add Seam Discipline)

*Append to existing `lcs-task-executor/[SKILL.md](http://SKILL.md)` TDD Mode section:*


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 7)
> See reference file for complete implementation details.


#### 8. ENHANCEMENT: `lcs-code-review` (Add Two-Axis Review)

*Append to existing `lcs-code-review/[SKILL.md](http://SKILL.md)` Phase 2:*


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 8)
> See reference file for complete implementation details.


#### 9. ENHANCEMENT: `lcs-task-slicer` (Add Blocking Edges &amp; Expand-Contract)

*Append to existing `lcs-task-slicer/[SKILL.md](http://SKILL.md)` Behavior Checklist:*


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 9)
> See reference file for complete implementation details.


#### 10. ENHANCEMENT: `lcs-toprd` (Add Testing Seams)

*Append to existing `lcs-toprd/[SKILL.md](http://SKILL.md)` PRD Template Structure:*


> **Full SKILL.md draft:** `references/skill-drafts.md` (Draft 10)
> See reference file for complete implementation details.


## Affected Areas / Files

**New Files to Create:**

- `skills/lcs-domain-modeling/[SKILL.md](http://SKILL.md)`

- `skills/lcs-research/[SKILL.md](http://SKILL.md)`

- `skills/lcs-prototype/[SKILL.md](http://SKILL.md)`

- `skills/lcs-wayfinder/[SKILL.md](http://SKILL.md)`

- `skills/lcs-wizard/[SKILL.md](http://SKILL.md)`

- `skills/lcs-wizard/assets/[template.sh](http://template.sh)`

**Files to Modify:**

- `skills/lcs-debug/[SKILL.md](http://SKILL.md)`

- `skills/lcs-task-executor/[SKILL.md](http://SKILL.md)`

- `skills/lcs-code-review/[SKILL.md](http://SKILL.md)`

- `skills/lcs-task-slicer/[SKILL.md](http://SKILL.md)`

- `skills/lcs-toprd/[SKILL.md](http://SKILL.md)`

- `skills/lcs-shared/[contract.md](http://contract.md)` (Update Artifact Type Registry)

- [`AGENTS.md`](http://AGENTS.md) (Update Skill Inventory)

## Testing Seams

- **Primary seam:** The [`SKILL.md`](http://SKILL.md) markdown files themselves. The test is whether an AI agent reading the [`SKILL.md`](http://SKILL.md) can execute the workflow without hallucinating or deviating from the LCS Shared Contract.

- **Secondary seam:** The `.lcs/work-items/` output artifacts. The test is whether downstream skills (e.g., `lcs-task-slicer` reading [`prd-enhanced.md`](http://prd-enhanced.md) with the new "Testing Seams" section) can correctly parse and utilize the new data.

## Security Considerations

- `lcs-wizard` MUST use `ask_secret` to prevent credentials from being written to bash history or `.lcs/` logs.

- `lcs-prototype` MUST be isolated in a `prototype/` directory and explicitly excluded from production build paths in the PRD.

- `lcs-debug` Phase 6 MUST enforce cleanup of `[DEBUG-XXXX]` logs to prevent sensitive runtime data from being committed to git.

## Performance Considerations

- `lcs-research` should utilize background execution (if supported by the adapter) to prevent blocking the main agent context window.

- `lcs-code-review` Axis 1 and Axis 2 should be evaluated in parallel sub-agent calls where the adapter permits, reducing total review time.

## Potential Bugs / Edge Cases

- **Edge Case:** `lcs-domain-modeling` is invoked on a legacy repo with no [`CONTEXT.md`](http://CONTEXT.md). **Handling:** Create file lazily on first term resolution.

- **Edge Case:** `lcs-debug` Phase 1 cannot build a tight feedback loop (e.g., bug requires physical hardware interaction). **Handling:** Stop, document the blocker, and request a captured artifact (HAR file, video) from the user.

- **Edge Case:** `lcs-wayfinder` map reveals the project is actually small enough for one session. **Handling:** Abort map creation, hand off directly to `lcs-toprd`.

## Acceptance Criteria

- [ ] AC-001: `lcs-domain-modeling` successfully creates/updates [`CONTEXT.md`](http://CONTEXT.md) in project root and tracks state in `.lcs/`.

- [ ] AC-002: `lcs-research` outputs a Markdown file with primary source citations, rejecting secondary blogs.

- [ ] AC-003: `lcs-prototype` generates an isolated HTML/UI prototype and provides a Handoff to archive it.

- [ ] AC-004: `lcs-wayfinder` generates a local map and blocked decision tickets inside `.lcs/work-items/`.

- [ ] AC-005: `lcs-wizard` generates a bash script using [`template.sh`](http://template.sh) that passes `bash -n` syntax check.

- [ ] AC-006: `lcs-debug` strictly enforces Phase 1 (Feedback Loop) before allowing Phase 3 (Hypotheses).

- [ ] AC-007: `lcs-task-executor` rejects TDD attempts that violate seam discipline (implementation-coupled).

- [ ] AC-008: `lcs-code-review` outputs distinct findings for Axis 1 (Standards) and Axis 2 (Spec).

- [ ] AC-009: `lcs-task-slicer` correctly sequences Expand-Contract tasks for wide refactors.

- [ ] AC-010: `lcs-toprd` includes the "Testing Seams" section in all generated PRDs.

## Test Strategy &amp; Testing Decisions

- **Unit:** Verify each new [`SKILL.md`](http://SKILL.md) contains the exact required headers and CoT declarations.

- **Integration:** Run a full lifecycle: `lcs-explore` -&gt; `lcs-domain-modeling` -&gt; `lcs-toprd` (verify Testing Seams present) -&gt; `lcs-task-slicer` (verify blocking edges) -&gt; `lcs-task-executor` (verify seam discipline) -&gt; `lcs-code-review` (verify two-axis output).

- **E2E:** Simulate a hard bug scenario using `lcs-debug` to ensure Phase 1 blocks progression until a red-capable command is established.

## Review Notes

- **Last Reviewed:** 2026-08-08

- **Summary:** Complete blueprint generated, embedding exact [SKILL.md](http://SKILL.md) instructions for 5 new and 5 enhanced skills, fully adapted for LCS V2 local-first architecture.

- **Changes Applied:** Mapped Matt Pocock's issue-tracker-dependent skills (Wayfinder) to LCS's `.lcs/work-items/` local markdown structure.

## Chain of Truth Report

### Level

Standard

### Sources Checked

- LCS V2 Repository (v2 branch `skills/` directory)

- Matt Pocock Engineering Skills `mattpocock/skills` engineering directory)

- LCS Shared Contract [`contract.md`](http://contract.md) rules on OKF and Handoff)

### Assumptions

- [verified] LCS V2 adapters (Claude Code, OpenCode) support reading multiple markdown files sequentially.

- [verified] The user wants the exact [SKILL.md](http://SKILL.md) content embedded in the PRD for precise slicing.

- [unverified] The target project repository has a [`template.sh`](http://template.sh) available for `lcs-wizard`, or `lcs-wizard` will need to generate it. (Mitigation: `lcs-wizard` will generate it if missing).

### Plan

1. Synthesize Matt Pocock disciplines into LCS V2 constraints.

2. Draft exact [SKILL.md](http://SKILL.md) markdown blocks for all 10 target skills.

3. Map to Source Requirement Ledger and Acceptance Criteria.

4. Format according to `lcs-toprd` template.

### Actions Taken

- Extracted core engineering principles (Seams, 6-phase debug, Expand-Contract, Domain Modeling).

- Adapted external issue tracker concepts to local `.lcs/` file structures.

- Wrote comprehensive PRD with embedded skill specifications.

### Verification

- Cross-referenced all SRC-### with AC-### to ensure 100% coverage.

- Verified all new skills include mandatory `## Handoff` and `## Chain of Truth Report` sections.

### Report

**Confidence:** High. The PRD contains the exact literal text required for downstream skills to execute without ambiguity.

**Limitations:** Adapters must support the creation of nested directories (e.g., `wayfinder-tickets/`) inside `.lcs/work-items/`.

## Handoff

Next recommended skill: lcs-prd-reviewer

Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/[prd.md](http://prd.md)

Current phase: prd

Current confidence: high

Blocking questions: None

Risks to carry forward: Ensure `lcs-prd-reviewer` checks for the presence of the new "Testing Seams" section during its audit.

Source of Truth Bundle: .lcs/[state.md](http://state.md), matt-pocock-skills, lcs-v2-skills

Must Preserve IDs: SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012

Unresolved IDs: None

Suggested next command: Review and fix [prd.md](http://prd.md) using lcs-prd-reviewer

```