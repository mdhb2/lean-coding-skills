# Review: lcs-master-enhance.md terhadap LCS V2

**Reviewer:** AI (automated cross-reference)
**Date:** 2026-08-08
**PRD:** `.planning/notes/lcs-master-enhance.md`

---

## Ringkasan Eksekutif

PRD ini mengusung peningkatan `lcs-master` dari linear router menjadi contextual orchestrator. Ide bagus — menggabungkan strength LCS (audit trail, SOT) dengan approach Matt Pocock (contextual routing, vocabulary foundation). Namun ada beberapa **gaps, inkonsistensi, dan risiko** yang perlu diperbaiki sebelum dieksekusi.

---

## Temuan Kritis (P0)

### 1. Frontmatter Tidak OKF v0.2 Compliant

PRD menggunakan frontmatter lama:
```yaml
type: artifact
artifact_type: prd
timestamp: ...
resource: ...
previous_artifact: ...
next_artifact: ...
```

Harusnya menggunakan OKF v0.2 (yang sudah diadopsi di `contract.md`):
```yaml
title: "PRD: Enhance lcs-master"
format_version: "okf/0.2"
authors: [{type: agent, name: "..."}]
created: "2026-08-08"
updated: "2026-08-08"
status: draft
artifact_type: prd
cot_level: standard
```

**Impact:** Melanggar contract §OKF Frontmatter Schema.

### 2. `lcs-codebase-design` Tidak Ada

PRD mengacu `lcs-codebase-design` sebagai vocabulary foundation layer bersama `lcs-domain-modeling`. Skill ini **belum ada** di `skills/` dan tidak ada dalam task breakdown Matt Pocock enhancement (`matt-pocock-task-breakdown.md`).

**Risiko:** Vocabulary Foundation Layer (§3.1) tidak bisa diimplementasi tanpa skill ini.

**Opsi:**
- A: Buat `lcs-codebase-design` skill baru (sesuai PRD)
- B: Ganti referensi dengan `lcs-codebase-doc` yang sudah ada (beda fungsi)
- C: Defer Vocabulary Foundation Layer sampai skill dibuat

### 3. `lcs-triage` Tidak Ada

PRD menyebut `lcs-triage` di On-ramp 1 (Multiple issues piling up). Skill ini **tidak ada** dan tidak ada plan untuk membuatnya.

**Solusi:** Hapus referensi ke `lcs-triage`, ganti dengan manual prioritization yang sudah dideskripsikan.

---

## Temuan Sedang (P1)

### 4. Enhanced SKILL.md Tidak Lengkap

PRD berisi potongan SKILL.md baru tapi bukan versi lengkap. Beberapa section:
- Frontmatter: Ada tapi lama (bukan OKF)
- On-ramps: Terdefinisi dengan baik
- Branching Logic: Terdefinisi dengan baik
- Vocabulary Foundation: Bergantung pada `lcs-codebase-design` yang tidak ada
- Handoff: Tidak terlihat di potongan SKILL.md

**Rekomendasi:** Buat SKILL.md lengkap setelah PRD di-review, bukan di PRD.

### 5. CoT Level Tidak Dideklarasikan

PRD tidak secara eksplisit menyatakan CoT level untuk `lcs-master` yang enhanced. Current `lcs-master` menggunakan `chain_of_truth_level: Standard`. PRD menambahkan precondition checks dan branching logic yang cukup kompleks.

**Pertanyaan:** Apakah tetap Standard atau perlu upgrade ke Strict?

**Rekomendasi:** Tetap Standard — `lcs-master` adalah router, bukan author artifacts. Precondition check dan branching logic adalah routing logic, bukan filesystem mutation.

### 6. Precondition Check vs Existing `.lcs/` Structure

PRD mengusulkan precondition check yang membuat `.lcs/` directory dan `state.md`. Ini sudah ada di beberapa skills (lcs-explore, lcs-toprd). Perlu klarifikasi:
- Siapa yang membuat `.lcs/` pertama kali?
- Apakah precondition check hanya di `lcs-master` atau juga di skills lain?

**Rekomendasi:** Precondition check hanya di `lcs-master` (router). Skills lain asumsikan `.lcs/` sudah ada.

### 7. Vocabulary Foundation Layer — Architecture Tidak Jelas

PRD mengatakan `lcs-domain-modeling` dan `lcs-codebase-design` "berjalan di bawah semua skills". Tapi tidak menjelaskan:
- Bagaimana cara "berjalan di bawah"? Auto-invoke? Pre-check? Post-check?
- Apakah vocabulary check wajib atau optional?
- Bagaimana integrasi dengan `CONTEXT.md` yang sudah ada?

**Rekomendasi:** Buat section eksplisit yang menjelaskan mechanism:
1. `lcs-master` checks `CONTEXT.md` before routing
2. If new terms detected, auto-invoke `lcs-domain-modeling` before proceeding
3. If architecture question detected, suggest `lcs-codebase-design`

---

## Temuan Rendah (P2)

### 8. Acceptance Criteria Lengkap tapi Beberapa Bergantung pada Missing Skills

AC-002 (Vocabulary Foundation) bergantung pada `lcs-codebase-design` yang tidak ada.
AC-005 (Standalone routing) baik-baik saja — semua standalone skills sudah ada.

### 9. Test Strategy Komprehensif

PRD memiliki test strategy yang baik dengan routing eval queries. Perlu update `routing-eval.json` yang sudah ada (28 queries) untuk menambah test cases baru.

### 10. Stop Matrix Konsisten dengan Existing Contract

Stop matrix yang diusulkan konsisten dengan Chain of Truth levels di `contract.md`. Bagus.

### 11. Standalone Skills Section Bagus

Dokumentasi routing untuk research, wizard, dan merge-conflicts sudah tepat. Tidak perlu perubahan.

---

## Checklist Kesesuaian LCS

| Aspek | Status | Catatan |
|---|---|---|
| OKF v0.2 Frontmatter | ❌ | Gunakan format lama |
| CoT Level Declared | ❌ | Tidak dideklarasikan |
| Handoff Section | ❌ | Tidak terlihat di PRD |
| Negative Triggers | ✅ | "Do NOT activate for..." ada |
| Source Requirement Ledger | ✅ | Ada dengan SRC-### |
| Acceptance Criteria | ✅ | Lengkap dengan AC-### |
| Affected Areas / Files | ✅ | Ada |
| Testing Seams | ✅ | Ada |
| Chain of Truth Report | ✅ | Ada |
| Contract Reference | ✅ | Refer ke `contract.md` |
| Path Convention | ✅ | Follow `.lcs/work-items/` |
| Existing Skills Referenced | ⚠️ | `lcs-codebase-design` tidak ada |

---

## Rekomendasi Aksi

### Sebelum Eksekusi (P0)

1. **Fix frontmatter** — ganti ke OKF v0.2 format
2. **Decide on `lcs-codebase-design`** — buat skill baru atau ganti referensi
3. **Remove `lcs-triage` reference** — ganti dengan manual prioritization

### Saat Eksekusi (P1)

4. **Clarify Vocabulary Foundation mechanism** — bagaimana tepatnya berjalan
5. **Declare CoT level** — Standard (recommendation)
6. **Create complete SKILL.md** — bukan potongan di PRD

### Setelah Eksekusi (P2)

7. **Update routing-eval.json** — tambah test cases untuk on-ramps dan branching
8. **Update AGENTS.md** — tambah `lcs-codebase-design` jika dibuat

---

## Verdict

**PRD: GOOD dengan revisi.** Ide contextual routing solid, integrasi dengan LCS SOT enforcement tepat. Perlu fix frontmatter dan resolve dependency ke `lcs-codebase-design` sebelum implementasi.
