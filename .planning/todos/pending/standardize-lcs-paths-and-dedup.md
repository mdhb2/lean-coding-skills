---
title: Standardisasi path archive & hapus duplikat task-executer
date: 2026-07-18
priority: high
status: done
completed: 2026-07-18
---

# Todo: Standardisasi path & hilangkan duplikasi skill

## Konteks
Dari note `lcs-skill-quality-audit.md`. Inkonsistensi path merusak Chain of Truth traceability;
duplikat skill meningkatkan risiko drift & salah trigger.

## Aksi — status setelah eksekusi
1. [x] **Finalizer tidak lagi menghapus code-review.md.**
   `lcs-doc-finalizer` step 10 diubah: COPY (bukan move+delete) ke `archive/`, salin
   `code-review.md` ke `docs/{ts}-{slug}/code-review.md`, baru hapus source setelah kedua copy sukses.
   Template doc.md Chain of Truth Report juga mencantumkan code-review.md di Sources Checked & Bundle.
2. [x] **`lcs-task-executer` sudah legacy alias proper** (deprecation notice + guard di baris 118-119).
   Tidak perlu diubah — sudah memenuhi tujuan hindari drift.
3. [x] **3 path convention sudah didokumentasikan** di `lcs-shared/contract.md` §11-56
   (doc-finalizer, codebase-doc, self-improvement, onboarding). Single source of truth sudah ada.
4. [x] **Batas explore vs debug sudah eksplisit** di description masing-masing
   (explore = sebelum PRD/options; debug = bug investigation, jangan implement sebelum paham).
5. [x] **Cross-link self-improvement → doc-finalizer** ditambah di AGENTS.md §8 + exclusion di finalizer
   guard agar subtree self-improvements tidak tersentuh archive.

## Verifikasi
- [x] Grep finalizer: tidak ada sisa "move and delete" / "delete the source folder".
- [x] Instruksi copy + exclusion + cross-link AGENTS.md muncul di file.
- [ ] (Belum dijalankan) finalize dummy end-to-end untuk konfirmasi code-review.md tetap terbaca di docs/.
