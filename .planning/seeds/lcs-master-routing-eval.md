---
title: lcs-master Routing Eval Kit
planted_date: 2026-07-18
trigger_condition: When lcs-master is released, or during any batch update of LCS skills.
---

# Seed: lcs-master Routing Eval Kit

## Purpose
Prevent silent routing regressions in the `lcs-master` orchestrator.

## Eval dimensions (when built)
1. **Routing accuracy** — given a user input, does lcs-master pick the correct next skill?
   (positive: "saya mau bikin fitur" → lcs-explore; negative near-miss: "review kode"
   → lcs-code-review, NOT lcs-task-executor).
2. **Contract enforcement** — does it block handoff to a skill with wrong path or
   misnamed folder? (negative: route to `lcs-doc-finalizer` but it uses `.lcs/work-items/docs/`).
3. **SOT decision log** — is every routing recorded in
   `.lcs/work-items/{ts}-lcs-master/session-log.md` with reason?
4. **Autopilot stop** — does autopilot halt & write SOT before Very Strict / mutating
   Strict steps, and on structural-change detection?

## Suggested format
20 queries (10 positive, 10 negative near-miss) using realistic casual Indonesian input,
measured for tokens + accuracy vs a no-skill baseline.
