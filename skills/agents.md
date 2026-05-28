# Aturan Penamaan: folder & file (agents)

Ringkas, wajib diikuti oleh semua skill dan agent.

1) Struktur folder runtime
- .lcs/work-items/<timestamp>-<slug-work-item>/
  - timestamp format: YYYYMMDD-HHMMSS (contoh: 20260519-203300)
  - slug-work-item: lowercase, a-z0-9, kata dipisah tanda minus (`-`), max 5 segment

2) Direktori output final
- .lcs/work-items/docs/<timestamp>-<slug-work-item>/
  - untuk dokumen akhir (map.md, doc.md) dan arsip
  - indeks: .lcs/work-items/docs/docs-index.md

3) Nama file artefak (kewajiban)
- explore.md                -> hasil eksplorasi (sketsa, Q&A)
- debug.md                  -> hasil investigasi bug
- prd.md                    -> PRD utama (tidak versioned)
- prd-enhanced.md           -> PRD yang sudah di-hardening/review
- task/task-###.md          -> tugas terpisah (nomor 3-digit, mulai 001)
- state.md                  -> file state canonical (lihat bagian 6)
- map.md, doc.md            -> file final output per work-item

4) Penamaan task
- Format: task-001.md, task-002.md, ...
- Isi harus mengikuti template TASK-### yang ada di SKILL.md
- Nomor tidak boleh lompat; gunakan berurutan untuk satu work-item

5) Slug dan timestamp rules
- Timestamp: selalu 14 digit tanpa separator selain `-` antara tanggal/waktu
- Slug: hanya `a-z0-9-`, tidak diawali/diakhiri `-`, tidak gunakan spasi, panjang maks 64
- Contoh folder valid: .lcs/work-items/20260519-203300-shopping-cart/

6) state.md canonical fields (oleh agent)
- current_phase: onboarding|explore|prd|tasks|execution|finalization
- current_work: <timestamp>-<slug-work-item>
- last_session_note: <singkat>
- timestamp: <ISO>

7) Handoff wajib di tiap artefak
- Footer artefak harus berisi Handoff yang konsisten:
  ## Handoff
  Next recommended skill: <skill-name>
  Next file to read: <path>
  Current phase: <phase>
  Current confidence: <low/medium/high>
  Blocking questions: <list or None>
  Risks to carry forward: <short>
  Suggested next command: <command>

8) Referensi dalam SKILL.md
- Semua SKILL.md harus merujuk ke path absolut contoh di atas, misal:
  Next file to read: .lcs/work-items/<timestamp>-<slug-work-item>/explore.md
- Jangan merujuk ke .lcs/docs/ atau .lcs/reff/ — gunakan .lcs/work-items/ dan .lcs/work-items/docs/

8.1) Pengecualian khusus lcs-doc-finalizer
- Untuk skill `lcs-doc-finalizer`, path final wajib:
  - output docs: .lcs/work-items/docs/<timestamp>-<slug-work-item>/
  - archive source: .lcs/work-items/docs/archive/<timestamp>-<slug-work-item>/
  - index: .lcs/work-items/docs/docs-index.md
- Aturan ini override asumsi path generik lain terkait docs/archive.

9) Migrasi dan backward-compat
- Jika menemukan .lcs/docs/ atau .lcs/docs/reff/ di SKILL.md atau rule, ganti menjadi:
  - .lcs/docs/           -> .lcs/work-items/
  - .lcs/docs/reff/      -> .lcs/work-items/docs/
- Jangan ubah isi artefak yang sudah diproduksi tanpa konfirmasi.

10) Contoh lengkap
- Work item sementara: .lcs/work-items/20260519-203300-shopping-cart/
  - explore.md
  - prd.md
  - prd-enhanced.md
  - task/task-001.md
  - task/task-002.md
- Dokumen final: .lcs/work-items/docs/20260519-203300-shopping-cart/
  - map.md
  - doc.md

11) Aturan commit/manual
- Perubahan pada SKILL.md yang mengubah path wajib disertai catatan commit menjelaskan migrasi path.
- Jangan commit binary besar atau secrets.

12) Penerapan
- Semua maintainers: periksa SKILL.md, contract.md, agents.md, dan rules; samakan path ke format di atas.

---
Lokasi file ini: skills/agents.md
