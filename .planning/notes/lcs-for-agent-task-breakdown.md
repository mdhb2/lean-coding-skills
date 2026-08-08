# Task Breakdown: Writing-for-Agents Enhancement

**Source PRD:** `.planning/notes/lcs-for-agent-prd.md` (status: reviewed)
**Total Tasks:** 14 tasks across 4 phases
**Estimated Effort:** 2 sessions
**Status:** ✅ COMPLETED (2026-08-08)

---

## Phase 1: Progressive Disclosure — Contract Refactor (SRC-004, SRC-005, SRC-011, SRC-012)

> Reduce `contract.md` token load by moving templates out, co-locating rules, adding context pointers.

| # | Task | File | Change |
|---|---|---|---|
| 1.1 | Add context pointers to `contract.md` — setiap section besar yang punya template di `templates/`, tambah pointer: "For exact structure, read `templates/{type}.template.md`" | `skills/lcs-shared/contract.md` | Tambah ~6 context pointers |
| 1.2 | Co-locate SRC-### rules — grup semua aturan Requirement Preservation di bawah satu heading `## Requirement Preservation Rule` | `skills/lcs-shared/contract.md` | Reorganize section |
| 1.3 | Co-locate OKF rules — grup semua aturan OKF di bawah `## OKF Frontmatter Schema` (sudah ada, pastikan tidak tersebar) | `skills/lcs-shared/contract.md` | Verify + consolidate |
| 1.4 | Tambah Pruning Checklist di akhir `contract.md` — daftar pertanyaan untuk skill creators: "Apakah instruksi ini mengubah perilaku? Jika tidak, hapus." | `skills/lcs-shared/contract.md` | Tambah section baru |

**Acceptance:** `contract.md` lebih ramping, setiap section besar punya context pointer, rules ter-grup rapi.

---

## Phase 2: Strict Completion Criteria — 3 Skills (SRC-001, SRC-002, SRC-003, SRC-009, SRC-010)

> Tambah completion criteria yang bisa diverifikasi ke 3 skill utama.

| # | Task | Skill | Enhancement |
|---|---|---|---|
| 2.1 | Tambah strict completion criteria ke `lcs-task-executor` — setiap validation step harus: run command, capture exit code, capture stdout/stderr verbatim, MUST exit 0 | `skills/lcs-task-executor/SKILL.md` | Merge dengan seam discipline existing |
| 2.2 | Tambah hard stop + leading words ke `lcs-debug` Phase 1 — "tight loop", "red-capable", MUST execute command yang goes RED sebelum hypothesizing | `skills/lcs-debug/SKILL.md` | Merge dengan 6-phase loop existing |
| 2.3 | Tambah evidence mandate ke `lcs-code-review` — setiap claim harus punya file path + line number, "Tests not run" jika validation tidak dijalankan | `skills/lcs-code-review/SKILL.md` | Merge dengan two-axis review existing |
| 2.4 | Tambah leading words ke `lcs-debug` description — "tight loop", "red-capable", "deterministic" | `skills/lcs-debug/SKILL.md` | Update description |

**Acceptance:** Setiap skill punya completion criteria yang bisa di-check secara mekanis (exit code, file path, line number).

---

## Phase 3: Pruning — No-Op Removal (SRC-006, SRC-007)

> Hapus instruksi no-op dan sharpen trigger descriptions.

| # | Task | File | Change |
|---|---|---|---|
| 3.1 | Scan semua SKILL.md — identifikasi no-op instructions (terlalu umum, tidak mengubah perilaku) | Semua `skills/lcs-*/SKILL.md` | Audit + list |
| 3.2 | Hapus no-op dari `lcs-task-executor` — "Pastikan mengikuti aturan", "Berpikirlah langkah demi langkah" | `skills/lcs-task-executor/SKILL.md` | Hapus + ganti spesifik |
| 3.3 | Hapus no-op dari `lcs-debug` — instruksi vague yang tidak menambah perilaku | `skills/lcs-debug/SKILL.md` | Hapus + ganti spesifik |
| 3.4 | Hapus no-op dari `lcs-code-review` — "Pastikan review menyeluruh" | `skills/lcs-code-review/SKILL.md` | Hapus + ganti spesifik |
| 3.5 | Sharpen `AGENTS.md` skill descriptions — ganti deskripsi umum dengan leading words yang tajam | `AGENTS.md` | Update descriptions |

**Acceptance:** Tidak ada instruksi no-op yang tersisa. Setiap instruksi punya kriteria verifikasi.

---

## Phase 4: Integration & Verification (SRC-008)

> OKF write-step relaxation + final validation.

| # | Task | File | Change |
|---|---|---|---|
| 4.1 | Document OKF write-step relaxation — invalid frontmatter → `status: draft (invalid_frontmatter)`, jangan block workflow | `skills/lcs-shared/contract.md` | Sudah ada, verify |
| 4.2 | Cross-check semua perubahan — pastikan tidak ada SKILL.md yang ter-break | Semua file | Manual review |
| 4.3 | Update PRD status → `completed` | `.planning/notes/lcs-for-agent-prd.md` | Status update |

**Acceptance:** Semua 12 SRC items ter-coverage, tidak ada regressi.

---

## Execution Order

```
Phase 1 (Contract Refactor) → Phase 2 (Completion Criteria) → Phase 3 (Pruning) → Phase 4 (Integration)
```

**Parallelization:**
- Phase 1 tasks (1.1-1.4) — sequential (same file)
- Phase 2 tasks (2.1-2.4) — independent, bisa parallel
- Phase 3 tasks (3.1-3.5) — 3.1 harus duluan (audit), lalu 3.2-3.5 parallel
- Phase 4 tasks (4.1-4.3) — sequential

**Critical path:** 1.1-1.4 → 2.1-2.4 → 3.1 → 3.2-3.5 → 4.1-4.3
