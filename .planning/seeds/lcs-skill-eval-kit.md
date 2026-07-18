---
title: Eval kit per skill LCS
planted_date: 2026-07-18
trigger_condition: Saat mau rilis atau update batch skill LCS (terutama code-review, tosrs, toprd).
---

# Seed: Eval kit per skill LCS

## Ide
Saat ini kualitas skill masih diukur dengan intuisi (tidak ada eval). AGENTS.md §6 sudah mewajibkan
20 eval query (10 positif, 10 negatif near-miss) per skill, tapi belum diterapkan ke skill LCS.

## Rencana kecil
- Buat `references/evals/` per skill dengan 20 query (positif + negatif).
- Prioritas: `lcs-code-review`, `lcs-tosrs`, `lcs-toprd` (skill terbesar & paling sering misinterpret).
- Ukur token, durasi, akurasi dengan vs tanpa skill sebelum packaging.

## Mengapa ditunda (seed)
Belum ada baseline pengukuran. Lebih baik selesaikan dulu konsistensi path (todo terkait)
baru eval, supaya eval tidak mengukur sistem yang sudah tahu bermasalah.
