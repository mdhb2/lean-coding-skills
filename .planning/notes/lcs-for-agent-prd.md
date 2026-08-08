```yaml
---
title: "PRD: Enhance LCS V2 with Writing-for-Agents Principles"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-toprd"
created: "2026-08-08"
updated: "2026-08-08T16:00:00+07:00"
tags: [enhancement, agent-writing, lcs-v2, optimization]
summary: "Integrate Matt Pocock's writing-for-agents principles (completion criteria, progressive disclosure, leading words, pruning) into core LCS V2 skills to eliminate premature completion, reduce token bloat, and improve agent reliability."
status: completed
related: ["lcs-shared/contract.md", "skills/lcs-task-executor/SKILL.md", "skills/lcs-debug/SKILL.md", "skills/lcs-code-review/SKILL.md"]
artifact_type: prd
artifact_id: "SRC-001"
source: "lcs-explore, lcs-research"
cot_level: standard
version: "1.0"
---

# PRD: Enhance LCS V2 with Writing-for-Agents Principles

## Problem Statement & Objective

**Problem Statement:**
LCS V2 memiliki struktur yang solid, namun seiring bertambahnya kompleksitas skill, muncul beberapa kerentanan dalam eksekusi agen:
1. **Premature Completion:** Agen sering mengklaim "Selesai" atau "Test passed" tanpa bukti output terminal yang sebenarnya, karena kriteria penyelesaian di `SKILL.md` terlalu longgar (misal: "Run validation commands").
2. **Token Bloat & Sprawl:** Aturan yang sama (seperti format OKF atau aturan `SRC-###`) diulang di berbagai file, dan template panjang (seperti struktur PRD/SRS) membuat `contract.md` menjadi terlalu berat untuk dimuat setiap saat.
3. **Weak Context Pointers:** Deskripsi skill di `AGENTS.md` atau `SKILL.md` terkadang terlalu umum, menyebabkan agen gagal memicu skill yang tepat secara konsisten.
4. **No-Op Instructions:** Instruksi seperti "Berpikirlah selangkah demi selangkah" atau "Pastikan mengikuti aturan" membebani *context load* tanpa mengubah perilaku model secara nyata.

**Objective:**
Mengintegrasikan prinsip-prinsip dari `writing-for-agents` (Matt Pocock) ke dalam inti LCS V2 untuk menciptakan dokumentasi skill yang **dapat diprediksi, hemat token, dan tahan terhadap halusinasi**. Fokus pada 3 area utama:
1. Menerapkan **Strict Completion Criteria** pada skill eksekusi kritis.
2. Menerapkan **Progressive Disclosure** dan **Co-location** pada `lcs-shared/contract.md`.
3. Mengoptimalkan **Context Pointers** dan **Leading Words** di `AGENTS.md` dan deskripsi skill.

## Background & Solution

**Background:**
Prinsip `writing-for-agents` menekankan bahwa dokumen untuk agen harus dibangun di atas *Information Hierarchy* (In-file steps, In-file reference, Disclosed reference). Setiap langkah harus memiliki *Completion Criterion* yang jelas dan dapat diperiksa (checkable & exhaustive). Penggunaan *Leading Words* (kata-kata yang sudah memiliki makna kuat di pretraining model, seperti "tight", "red", "tracer bullets") lebih efektif daripada mendefinisikan jargon baru.

**Solution:**
1. **Enhance 3 Core Skills:** Menulis ulang bagian behavior checklist di `lcs-task-executor`, `lcs-debug`, dan `lcs-code-review` dengan *Strict Completion Criteria*.
2. **Refactor `contract.md`:** Memindahkan template panjang ke folder `templates/` dan menggunakan *Context Pointers* yang tajam. Mengelompokkan aturan terkait (`Co-location`).
3. **Prune & Sharpen:** Menghapus instruksi *no-op* dan memperbarui deskripsi skill di `AGENTS.md` dengan *Leading Words* untuk pemicu yang lebih andal.

## Source Context

- **Matt Pocock `writing-for-agents`:** https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents
- **LCS V2 Shared Contract:** `skills/lcs-shared/contract.md` (OKF v0.2 compliant)
- **LCS V2 Core Skills:** `lcs-task-executor`, `lcs-debug`, `lcs-code-review`

## Scope & User Stories

### User Stories
1. As a developer, I want `lcs-task-executor` to have strict completion criteria for test execution, so that it cannot claim success without verifiable terminal output.
2. As a developer, I want `lcs-debug` to enforce a hard stop after Phase 1 (Feedback Loop), so that the agent does not hypothesize prematurely without a red-capable command.
3. As a developer, I want `lcs-code-review` to require explicit evidence for every claim, so that reviews are factual and not hallucinated.
4. As a developer, I want large templates (PRD, SRS, Task) moved to `templates/` and referenced via context pointers, so that `contract.md` remains lightweight and focused on rules.
5. As a developer, I want related rules (e.g., all `SRC-###` preservation rules) co-located under a single heading, so that the agent can find them easily without scanning the whole document.
6. As a developer, I want skill descriptions in `AGENTS.md` to use sharp leading words and explicit trigger phrases, so that the router (`lcs-master`) selects the correct skill reliably.
7. As a developer, I want all no-op instructions (e.g., "be thorough", "think step by step") removed from SKILL.md files, so that context load is minimized.
8. As a developer, I want the OKF v0.2 frontmatter validation to be relaxed during the write step (allowing `invalid_frontmatter` status), so that unstable models do not block the entire workflow on minor YAML errors.

## Source Requirement Ledger

| SRC ID | Priority | Origin | Description |
|---|---|---|---|
| SRC-001 | P0 | User Story 1 | Enhance `lcs-task-executor` with strict completion criteria for validation steps (must capture verbatim stdout/stderr, exit code 0). |
| SRC-002 | P0 | User Story 2 | Enhance `lcs-debug` to enforce a hard stop after Phase 1 (Build Tight Feedback Loop) with explicit completion criteria before hypothesizing. |
| SRC-003 | P0 | User Story 3 | Enhance `lcs-code-review` to mandate explicit evidence (file path, line number, or command output) for every finding; forbid unsupported claims. |
| SRC-004 | P0 | User Story 4 | Refactor `lcs-shared/contract.md` to use Progressive Disclosure: move large templates to `lcs-shared/templates/` and reference them via context pointers. |
| SRC-005 | P0 | User Story 5 | Apply Co-location in `contract.md`: group all `SRC-###` preservation rules and OKF validation rules under dedicated, single headings. |
| SRC-006 | P0 | User Story 6 | Update `AGENTS.md` and skill `description` fields to use sharp Leading Words and explicit trigger phrases for reliable routing. |
| SRC-007 | P0 | User Story 7 | Prune no-op instructions from all enhanced SKILL.md files (e.g., remove "think carefully", "be thorough"). |
| SRC-008 | P0 | User Story 8 | Ensure OKF v0.2 write-step relaxation is documented: invalid frontmatter gets `status: completed (invalid_frontmatter)` but does not block the write. |
| SRC-009 | P1 | User Story 1 | Use leading words like "tight loop" and "red-capable" in `lcs-debug` to anchor agent behavior efficiently. |
| SRC-010 | P1 | User Story 3 | `lcs-code-review` must explicitly state "Tests were not run" if validation commands are skipped, rather than assuming success. |
| SRC-011 | P1 | User Story 4 | Context pointers in `contract.md` must follow the format: "For exact structure, read `templates/{template}.md`. Only load when generating this artifact." |
| SRC-012 | P2 | User Story 6 | Add a "Pruning Checklist" to the end of `lcs-shared/contract.md` for future skill creators to validate their documents. |


## Known No-Op Instructions (To Be Removed)

| File | No-Op Instruction | Why It's No-Op |
|---|---|---|
| `lcs-task-executor/SKILL.md` | "Pastikan mengikuti aturan" | Terlalu umum — tidak mengubah perilaku |
| `lcs-debug/SKILL.md` | "Berpikirlah selangkah demi selangkah" | Model sudah melakukan ini secara default |
| `lcs-code-review/SKILL.md` | "Pastikan review menyeluruh" | Tidak ada kriteria spesifik |
| `contract.md` | "Ikuti konvensi yang ada" | Terlalu vague — harus spesifik |

> **Action:** Hapus semua no-op instructions di atas saat implementasi. Ganti dengan kriteria spesifik yang bisa diverifikasi.

## Non-Goals / Out of Scope

- **Tidak membuat skill baru:** Enhancement ini hanya memodifikasi file yang sudah ada (`contract.md`, 3 core skills, `AGENTS.md`).
- **Tidak mengubah OKF v0.2 Schema:** Schema tetap sama, hanya cara penerapan dan validasinya yang di-refine sesuai prinsip *writing-for-agents*.
- **Tidak mengubah Chain of Truth Levels:** Level CoT (Light, Standard, Strict, Very Strict) tetap dipertahankan sesuai registry.

## Requirements

### Functional Requirements
- [ ] `lcs-task-executor` SKILL.md updated with strict completion criteria for test/lint execution.
- [ ] `lcs-debug` SKILL.md updated with hard stop after Phase 1 and explicit criteria for "tight feedback loop".
- [ ] `lcs-code-review` SKILL.md updated to mandate explicit evidence for every claim and forbid unsupported assumptions.
- [ ] `lcs-shared/contract.md` refactored to move templates to `templates/` and use context pointers.
- [ ] `lcs-shared/contract.md` rules reorganized using Co-location principle.
- [ ] `AGENTS.md` skill descriptions updated with leading words and sharp trigger phrases.
- [ ] All no-op instructions removed from the enhanced files.

### Non-Functional Requirements
- **Token Efficiency:** Reduce overall token count of `contract.md` by at least 20% through progressive disclosure.
- **Reliability:** Eliminate "premature completion" hallucinations in the 3 target skills.
- **Maintainability:** Single Source of Truth for all templates and rules.

## Technical Approach & Implementation Decisions

### 1. Progressive Disclosure & Co-location (`lcs-shared/contract.md`)
**Decision:** Move all large artifact templates (PRD, SRS, Task, etc.) from inline markdown in `contract.md` to individual files in `skills/lcs-shared/templates/`.
**Context Pointer Implementation:**
> *"For the exact structure of this artifact, read `templates/{artifact_type}.template.md`. Only load this file when generating a new artifact of this type. Do not load it during review or execution phases."*
**Co-location:** Group all `SRC-###` rules under a single `## Requirement Preservation Rule` heading. Group all OKF rules under `## OKF Frontmatter Schema (v2)`.

### 2. Strict Completion Criteria (`lcs-task-executor`)

> **Dedup Note:** Seam Discipline & TDD Rules sudah ada dari Matt Pocock Enhancement PRD. Enhancement ini MENAMBAHKAN completion criteria spesifik (exit code 0, verbatim stdout/stderr), bukan mengganti yang ada.
**Decision:** Replace vague instructions with checkable, exhaustive criteria.
**Enhancement:**
```markdown
- **Step: Execute Validation.**
  - **Action:** Run `npm run lint` and `npm test` (or project-specific equivalents).
  - **Completion Criterion:** Both commands MUST exit with code 0. The exact stdout/stderr MUST be captured verbatim in the `Verification` section of the Chain of Truth Report. 
  - **Failure Handling:** If either fails, mark task status as `blocked`, record the error, and HALT. Do not attempt to fix without user confirmation or a new task.
```

### 3. Hard Stop & Leading Words (`lcs-debug`)
**Decision:** Enforce Phase 1 completion before any hypothesizing, using leading words like "tight" and "red-capable".
**Enhancement:**
```markdown
- **Phase 1: Build Tight Feedback Loop**
  - **Action:** Construct a deterministic, agent-runnable command that isolates the bug.
  - **Completion Criterion:** You have executed the command at least once, and it reliably goes **red** (fails) on this specific bug. It must be fast (<10s), deterministic, and require no human interaction.
  - **Hard Stop:** DO NOT proceed to Phase 2 (Hypothesise) until this criterion is met and logged. If impossible, state the blocker and request a captured artifact (HAR, log dump) from the user.
```

### 4. Evidence Mandate (`lcs-code-review`)

> **Dedup Note:** Two-Axis Review sudah ada dari Matt Pocock Enhancement PRD. Enhancement ini MENAMBAHKAN explicit evidence requirement per claim, bukan mengganti yang ada.
**Decision:** Forbid unsupported claims. Every finding must have a traceable source.
**Enhancement:**
```markdown
- **Rule: Evidence Mandate.** Every claim in the review MUST cite specific evidence: a file path, line number, or verbatim command output. 
- **Anti-Pattern:** Never write "All tests passed" unless the test output is explicitly captured in the report. If tests were not run, you MUST write: "Tests were not run; validation is incomplete."
```

### 5. Pruning No-Ops & Sharpening Pointers (`AGENTS.md` & Descriptions)
**Decision:** Remove phrases like "think step by step", "be thorough", "please ensure". Replace with leading words.
**Enhancement Example (`lcs-code-review` description):**
- *Before:* "Use this skill to review code implementation after task execution. Be thorough and check everything."
- *After:* "Use for **two-axis** diff review (**Standards** + **Spec**) after `lcs-task-executor`. Triggers: 'review code', 'validate artifacts', 'check results'. Halts on missing evidence."

## Affected Areas / Files

**Files to Modify:**
1. `skills/lcs-shared/contract.md` (Refactor for progressive disclosure, co-location, pruning).
2. `skills/lcs-task-executor/SKILL.md` (Add strict completion criteria).
3. `skills/lcs-debug/SKILL.md` (Add hard stop for Phase 1, leading words).
4. `skills/lcs-code-review/SKILL.md` (Add evidence mandate, anti-patterns).
5. `AGENTS.md` (Sharpen skill descriptions with leading words and explicit triggers).

**Files to Create:**
1. `skills/lcs-shared/templates/prd.template.md`
2. `skills/lcs-shared/templates/srs.template.md`
3. `skills/lcs-shared/templates/task.template.md`
*(Note: Actual template extraction will be done during task execution based on current inline content).*

## Testing Seams

- **Primary Seam:** The `SKILL.md` files themselves. Test: Can an AI agent read the enhanced instructions and execute the workflow without hallucinating "success" or ignoring hard stops?
- **Secondary Seam:** `contract.md` context pointers. Test: Does the agent correctly load `templates/*.template.md` only when generating a new artifact, and skip it during review?
- **Tertiary Seam:** OKF v0.2 frontmatter generation. Test: Does the agent apply `status: completed (invalid_frontmatter)` gracefully when YAML is slightly malformed, rather than crashing the workflow?

## Security Considerations

- **No-Op Pruning:** Ensure that removing "no-op" instructions does not accidentally remove critical security constraints (e.g., "always redact secrets before logging"). Security rules must be explicitly marked as **P0** and retained.
- **Evidence Mandate:** Preventing agents from claiming "tests passed" without output protects against silent deployment of broken code.

## Performance Considerations

- **Token Reduction:** Moving templates to `templates/` and using context pointers will reduce the base token load of `contract.md` by an estimated 20-30%, speeding up every skill invocation that reads it.
- **Fast Failure:** Strict completion criteria in `lcs-task-executor` and `lcs-debug` will cause the agent to fail fast and halt, saving compute cycles that would otherwise be wasted on hallucinated fixes.

## Potential Bugs / Edge Cases

- **Edge Case 1:** Agent fails to find the `templates/` template due to pathing error. 
  - *Handling:* The context pointer must use the exact relative path `../lcs-shared/templates/{name}.template.md`. If missing, the agent must report the missing file and generate a best-effort structure based on OKF schema, marking it `draft (missing_template)`.
- **Edge Case 2:** User explicitly asks the agent to "just write the code, skip the tests".
  - *Handling:* The agent must still update the `task-###.md` status to reflect this deviation, log it in the Chain of Truth Report, and proceed, but must not claim "validation passed".
- **Edge Case 3:** Unstable model struggles with the strict YAML frontmatter validation.
  - *Handling:* The "Reduce Strictness During Write Steps" rule in `contract.md` explicitly allows `status: completed (invalid_frontmatter)` to prevent workflow blockage.

## Acceptance Criteria

- [ ] AC-001: `lcs-task-executor` SKILL.md contains explicit "Completion Criterion" for validation steps requiring verbatim stdout/stderr.
- [ ] AC-002: `lcs-debug` SKILL.md contains a "Hard Stop" directive preventing Phase 2 until a "tight, red-capable" feedback loop is established and logged.
- [ ] AC-003: `lcs-code-review` SKILL.md includes an "Evidence Mandate" rule forbidding unsupported claims and requiring explicit "Tests were not run" statements if applicable.
- [ ] AC-004: `lcs-shared/contract.md` no longer contains inline artifact templates; they are moved to `lcs-shared/templates/` and referenced via clear context pointers.
- [ ] AC-005: `lcs-shared/contract.md` rules are reorganized using the Co-location principle (e.g., all `SRC-###` rules in one section).
- [ ] AC-006: `AGENTS.md` skill descriptions are updated to remove no-ops and include sharp leading words and explicit trigger phrases.
- [ ] AC-007: All enhanced files comply with OKF v0.2 schema requirements, including the relaxed write-step validation rule.
- [ ] AC-008: A "Pruning Checklist" is added to `contract.md` for future skill validation.

## Test Strategy & Testing Decisions

### Testing Decisions
- **What makes a good test:** Tests should verify that the agent *stops* when it should (hard stops) and *demands evidence* when required. We are testing the *constraints* of the prompt, not just the happy path.
- **Seams to test:** The behavior checklist of the 3 enhanced skills, and the context pointer resolution in `contract.md`.

### Unit Tests (Prompt Simulation)
- **Test 1 (Task Executor):** Provide a scenario where `npm test` fails. Verify the agent marks the task as `blocked` and outputs the error, rather than claiming success.
- **Test 2 (Debug):** Provide a vague bug report. Verify the agent asks for repro steps and explicitly states it cannot hypothesize until a red-capable command is built.
- **Test 3 (Code Review):** Provide a code diff without test files. Verify the agent outputs "Tests were not run; validation is incomplete" instead of "All tests passed".
- **Test 4 (Contract):** Ask the agent to generate a PRD. Verify it reads `templates/prd.template.md` and does not hallucinate a custom structure.

### Integration Tests
- Run a full `lcs-toprd` → `lcs-task-slicer` → `lcs-task-executor` flow. Verify that the `SRC-###` IDs are preserved (Co-location test) and that the final execution includes verbatim terminal output (Completion Criterion test).

## Review Notes

- **Last Reviewed:** 2026-08-08
- **Summary:** PRD created to integrate `writing-for-agents` principles into LCS V2, focusing on completion criteria, progressive disclosure, and pruning.
- **Changes Applied:** Defined exact enhancements for 3 core skills and `contract.md`, aligned with OKF v0.2 standards.

## Chain of Truth Report

### Level
Standard

### Sources Checked
- `https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents`
- `https://github.com/mdhb2/lean-coding-skills/tree/v2/skills/lcs-shared/contract.md`
- `https://github.com/mdhb2/lean-coding-skills/tree/v2/skills/lcs-task-executor/SKILL.md`
- `https://github.com/mdhb2/lean-coding-skills/tree/v2/skills/lcs-debug/SKILL.md`
- `https://github.com/mdhb2/lean-coding-skills/tree/v2/skills/lcs-code-review/SKILL.md`

### Assumptions
- [verified] LCS V2 uses OKF v0.2 schema for all artifacts.
- [verified] `lcs-shared/contract.md` currently contains inline templates that can be extracted.
- [unverified] The agent's current model version responds well to "leading words" without additional definition (assumed yes based on Matt Pocock's research).

### Plan
1. Analyze current `contract.md` and core skills for no-ops and weak criteria.
2. Draft enhanced SKILL.md sections with strict completion criteria and hard stops.
3. Design the progressive disclosure structure for `contract.md` (identifying templates to move).
4. Formulate sharp context pointers and leading words for `AGENTS.md`.
5. Compile into PRD format with OKF v0.2 compliance.

### Actions Taken
- Extracted core principles from `writing-for-agents` (Completion Criteria, Progressive Disclosure, Co-location, Leading Words, Pruning).
- Mapped principles to specific LCS V2 vulnerabilities (premature completion, token bloat).
- Drafted exact markdown enhancements for the 3 target skills and `contract.md`.
- Aligned all requirements with OKF v0.2 schema and validation rules.

### Verification
- Checked that all 12 Source Requirements are covered by the 8 Acceptance Criteria.
- Verified that the proposed changes do not violate the existing Chain of Truth levels or folder conventions.
- Confirmed OKF v0.2 frontmatter schema is correctly referenced.

### Report
**Confidence:** High. The enhancements are targeted, directly address known agent failure modes (premature completion, hallucination), and leverage proven prompt engineering principles from `writing-for-agents`.
**Limitations:** The effectiveness of "leading words" depends on the specific LLM provider's pretraining; minor adjustments to word choice may be needed during implementation.

## Handoff

**Next recommended skill:** lcs-prd-reviewer
**Next file to read:** `.lcs/work-items/{timestamp}-{slug-work-item}/prd.md`
**Current phase:** prd
**Current confidence:** high
**Blocking questions:** None
**Risks to carry forward:** Ensure the extraction of templates from `contract.md` to `templates/` does not break existing skills that might be hardcoding inline template expectations (though they should be using the contract).
**Source of Truth Bundle:** `.lcs/state.md`, `lcs-shared/contract.md`, `writing-for-agents/SKILL.md`
**Must Preserve IDs:** SRC-001 through SRC-012
**Unresolved IDs:** None
**Suggested next command:** Review and harden prd.md using lcs-prd-reviewer
```