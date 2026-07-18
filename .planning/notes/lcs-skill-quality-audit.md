---
title: LCS Skill Quality Audit Findings
date: 2026-07-18
context: Socratic explore session on optimizing LCS skill output quality (intuition-based, no prior measurement). Analysis from direct reading of all 16 SKILL.md files + AGENTS.md sections 6-8.
---

# LCS Skill Quality Audit Findings

Source: explore session "analisa seluruh skill di project ini". Focus: kualitas output artifact (PRD/SRS/task/code-review).

## A. Path inconsistency & artifact loss (kritis untuk Chain of Truth)
- 3 konvensi path berbeda:
  - `work-items/{ts}-{slug}/` — toprd, tosrs, task-slicer, prd-reviewer, code-review
  - `docs/` + `archive/` — doc-finalizer, codebase-doc (path khusus, AGENTS.md §7)
  - `docs/self-improvements/` — self-improvement (path khusus, AGENTS.md §8)
- `lcs-doc-finalizer` step 10 memindah & MENGHAPUS `work-items/{ts}-{slug}/` ke `archive/`.
  Akibat: `code-review.md` (artifact verifikasi) ikut ter-archive → putus dari traceability final.
- `lcs-self-improvement` override path sendiri tanpa cross-link ke finalizer.

## B. Redundansi & duplikasi
- `lcs-task-executer` (119L) = legacy alias `lcs-task-executor` (121L), isi nyaris identik.
  Dua skill trigger sama = risiko salah trigger / drift.
- `lcs-explore` (107L) vs `lcs-debug` (88L): keduanya ringan & interaktif, batas pakai tidak eksplisit.

## C. Kualitas template & determinism
- `lcs-tosrs` kuat (traceability, atomic reqs) tapi `lcs-toprd` mengandalkan "synthesize what you know"
  tanpa wajib baca explore.md/debug.md secara eksplisit di beberapa cabang → risiko halusinasi saat konteks kosong.
- Tidak ada eval/checklist kualitas sama sekali (masih intuisi). Skill besar paling butuh:
  `code-review` (674L), `self-improvement` (417L), `tosrs` (370L).

## D. Trigger & discoverability
- `lcs-codebase-doc` vs `lcs-onboarding` vs `lcs-debug-ext` overlap di "analyze/document repo"
  → bisa salah aktif.

## Rekomendasi (lihat todo & seed terkait)
- Prioritas 1 (konsistensi): standardisasi path archive, hapus/merge task-executer, dokumentasikan 3 path di lcs-shared/contract.md.
- Prioritas 2 (fitur/isi): eval kit per skill, guard baca source di toprd, batas explore vs debug, cross-link self-improvement.
