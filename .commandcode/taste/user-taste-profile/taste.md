# User Taste Profile
- Prefers Indonesian language in communication, casual/colloquial style (e.g., "cek", "pontensi", "skil2"). Confidence: 0.9
- Prefers bilingual documentation: maintains parallel English and Indonesian versions of project docs (e.g., README.md + README-ID.md), cross-linked. Confidence: 0.75
- Prefers fully removing deprecated/legacy duplicate skills (e.g. `lcs-task-executer`) rather than keeping backward-compatibility aliases; wants ALL references cleaned up across validator, contracts, evals, and docs so no stale traces remain. Confidence: 0.85
- After refactoring, expects verification that no dependent component breaks (runs npm test + grep for leftover references). Confidence: 0.8
- Values systematic, multi-dimensional project reviews: checks component interconnection/consistency, information flow integrity between pipeline stages, and risk/breakage assessment as distinct dimensions. Confidence: 0.8
- Prefers thorough, complete coverage across all components rather than partial or sample-based reviews. Confidence: 0.7
- When documenting skills/tools, includes concrete usage scenarios with example conversation prompts and "when to use" guidance for each. Confidence: 0.85
