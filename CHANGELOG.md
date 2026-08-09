# Changelog

All notable changes to Lean Coding Skills will be documented in this file.


## [v2.4] 2026-08-09

### Code Review Enhancement: Two-Axis Review + Architecture Improvement

**Summary:** Enhanced code review with explicit two-axis process (Spec Compliance & Code Quality), integrated Fowler's code smells baseline, and added new skill for architecture improvement planning.

#### New Features (2)
- **lcs-improve-architecture skill**: Generate visual architecture improvement plans by analyzing features, identifying duplicated concerns, proposing unified architecture with migration task breakdown
- **Two-Axis Review Process**: Explicit separation of spec compliance (PRD/SRS verification) vs code quality (Fowler smells + LCS standards) in lcs-code-review

#### Enhancements (2)
- **Fowler Smell Baseline**: Added 8 core code smells to lcs-code-review (Mysterious Name, Duplicated Code, Long Function, Long Parameter List, Global Data, Mutable Data, Divergent Change, Shotgun Surgery)
- **Concurrent Review Execution**: Two-axis reviews now run in parallel for faster feedback

#### New Artifacts (1)
- **architecture-improvement.template.md**: Template for architecture improvement reports with sections for current state analysis, duplication mapping, unified architecture proposal, and migration breakdown

#### Files Modified (3)
**Skills (2):**
- `skills/lcs-code-review/SKILL.md` - Added two-axis review process and Fowler smell baseline
- `skills/lcs-improve-architecture/SKILL.md` (new) - Architecture improvement planning skill

**Templates (1):**
- `skills/lcs-shared/templates/architecture-improvement.template.md` (new) - Architecture improvement report template

**Documentation (1):**
- `AGENTS.md` - Updated skill inventory count (21 → 22 skills)

#### Impact
- **Code Review Quality**: Reviewers now have explicit framework for checking both requirements alignment and code health
- **Architecture Work**: New workflow from duplication detection to unified refactoring with visual flowcharts
- **Skill Inventory**: 22 total LCS skills

## [v2.3] - 2026-08-09

### Contract.md Alignment - 13 GAP Fixes

**Summary:** Complete alignment of all 21 skills and 8 templates with `skills/lcs-shared/contract.md` specification. Zero contract violations remain.

#### Critical Fixes (4)
- **GAP-001:** Added AFK/HITL enforcement in `lcs-task-executor` — Type field validation now blocks HITL tasks with user confirmation gate
- **GAP-002:** Updated 8 artifact templates with full 10-field Handoff format (explore, prd, prd-enhanced, srs, task, session-log, code-review, debug)
- **GAP-003:** Removed `source-ledger.md` phantom dependency from `lcs-tosrs` — clarified Source Requirement Ledger embedded in prd.md
- **GAP-004:** Added `lcs-tosrs` to `lcs-master` routing chain — workflow now: explore → toprd → prd-reviewer → **tosrs** → task-slicer → executor

#### Medium Priority Fixes (5)
- **GAP-005:** Preserved explore.md Decision Ledger in PRD — added to `lcs-toprd` Source of Truth Bundle
- **GAP-006:** Preserved Testing Seams and User Stories in SRS — added sections to `lcs-tosrs` SRS.md required structure
- **GAP-007:** Added task-coverage.md validation in `lcs-task-executor` completion checklist
- **GAP-008:** Added prototype.md to `lcs-toprd` Source of Truth Bundle
- **GAP-009:** Verified Must Preserve IDs correctly narrowed in `lcs-task-executor` (already correct)

#### Low Priority Fixes (4)
- **GAP-010:** Updated priority notation to P0/P1/P2 in `prd.template.md`
- **GAP-011:** Updated `debug.template.md` with full Source Requirement Ledger format (Description, Priority, Origin)
- **GAP-012:** Added Source Requirement Ledger section to `debug-ext.template.md`
- **GAP-013:** Added explore.md to `lcs-doc-finalizer` Source of Truth Bundle

#### Files Modified (14)
**Skills (5):**
- `skills/lcs-task-executor/SKILL.md`
- `skills/lcs-tosrs/SKILL.md`
- `skills/lcs-master/SKILL.md`
- `skills/lcs-toprd/SKILL.md`
- `skills/lcs-doc-finalizer/SKILL.md`

**Templates (8):**
- `skills/lcs-shared/templates/explore.template.md`
- `skills/lcs-shared/templates/prd.template.md`
- `skills/lcs-shared/templates/prd-enhanced.template.md`
- `skills/lcs-shared/templates/srs.template.md`
- `skills/lcs-shared/templates/task.template.md`
- `skills/lcs-shared/templates/session-log.template.md`
- `skills/lcs-shared/templates/code-review.template.md`
- `skills/lcs-shared/templates/debug.template.md`
- `skills/lcs-shared/templates/debug-ext.template.md`

#### Validation Results
- ✅ All 14 files verified readable
- ✅ All 8 templates validated with complete 10-field Handoff format
- ✅ Source Requirement Ledger format consistent (P0/P1/P2 + Origin)
- ✅ Zero phantom dependencies remain

#### Breaking Changes
None — all changes additive or clarifying.

---

## [v2.2] - 2026-08-08

### OKF Lifecycle Alignment
- Wayfinder DEC tickets now use `status: active/archived` frontmatter
- `artifact_type: index` registered for navigation files (`docs-index.md`, `index.md`)
- Full OKF frontmatter for all index artifacts
- Validator alignment: quoted timestamps, no `type` frontmatter, date-only validation
- PowerShell parity runner: `validate-traceability.ps1`

---

## [v2.1] - 2026-08-07

### Chain of Truth Compliance
- Chain of Truth protocol applied to all 21 skills
- `lcs-task-executer` deprecated in favor of `lcs-task-executor` (typo fix)
- New artifact types and templates added
- `lcs-wizard` helper template `template.sh`
- Extended routing evals
- Indonesian README (`README-ID.md`) added

---

## [v2.0] - 2026-08-06

### Initial Release
- 21 LCS skills implementing complete lean coding workflow
- OKF frontmatter standard (28 artifact types)
- Chain of Truth meta-skill protocol
- Shared contract (`skills/lcs-shared/contract.md`)
- 8 artifact templates
- Validation scripts (bash + PowerShell)
