
## Gotchas & Anti-Patterns

- Do not review code you haven't read. Reading the diff is mandatory.
- Do not skip artifact reading order — missing upstream context leads to false positives.
- Do not assign P0/P1 without clear artifact evidence. Subjective preferences are P3 at most.
- Do not combine review and fix in one step. Review produces report; executor applies fixes.
- Do not claim `All tests passed` unless you actually ran them. State `Tests were not run` if not executed.
- Do not add requirements that don't exist in artifacts. Label suggestions as `Optional Improvement`.
- Do not produce a generic PASS when artifacts are missing. Use BLOCKED or PARTIAL_REVIEW.
- For NEEDS_FIX: always include Fix Request Copy so executor can work independently.
- For blocked reviews: clearly state which artifact is missing and what can't be verified.
- If tests exist but were not run, note this in the report — don't assume they pass.
- Security findings must cite specific code paths, not vague concerns.
- Do not refactor or restructure code in fix instructions. Keep instructions surgical.
- If the same bug appears in multiple files, create one FIX entry per distinct location.
- Separate mandatory fixes (P0/P1) from optional improvements (P2/P3). Mixing them confuses the executor.
- When the task scope is unclear, downgrade to PARTIAL_REVIEW rather than guessing intent.

---
