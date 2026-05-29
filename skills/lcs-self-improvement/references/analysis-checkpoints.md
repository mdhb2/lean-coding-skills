# Analysis Checkpoints

Use these prompts to keep analysis consistent, evidence-based, and privacy-conscious.

## 1) User Goal Discovery

- What outcome was user trying to achieve?
- What acceptance criteria were explicit vs implicit?
- Which constraints were must-have vs preference?
- Did goal shift during conversation?

## 2) Friction Identification

- Where did interaction stall or loop?
- Where did model misunderstand intent?
- Where did user need to repeat corrections?
- Where did output violate known constraints?
- Where did workflow lack clear review/apply separation?

## 3) Repeated Corrections Detection

- Were names, paths, or formats corrected multiple times?
- Did outdated assumptions survive after correction?
- Did model reintroduce already-fixed errors?
- Are same failures visible across supplied logs/files?

## 4) What Worked Well

- Which instruction patterns reduced errors?
- Which output formats improved review speed?
- Which checkpoints prevented rework?
- Which constraints should be preserved as defaults?

## 5) Missing Instructions and Gaps

- Is issue already covered in existing instructions?
- If covered, is wording actionable and operational?
- If not covered, where should new guidance live?
- Is recommendation reusable or session-specific?

## 6) Privacy and Safety Checks

- Does report avoid raw user quotes by default?
- Is evidence summarized without sensitive detail leakage?
- Are secrets, identifiers, or private data excluded?
- Are recommendations phrased without exposing unnecessary transcript detail?

## 7) Evidence Sufficiency

- Is there enough evidence to support each claim?
- Is claim grounded in available sources only?
- Where evidence is thin, did report use `[TODO]`?
- Where policy preference needed, did report use `[ASK USER]`?

If evidence is insufficient overall:

- state limitation explicitly
- produce limited report
- avoid long-term pattern claims

## 8) Confidence Scoring Guidance

Assign confidence per issue/recommendation:

- **High**: Multiple consistent evidence points; low ambiguity.
- **Medium**: Some evidence; moderate ambiguity; likely valid but incomplete.
- **Low**: Sparse/indirect evidence; depends on missing context or assumptions.

Upgrade confidence only when cross-referenced by multiple sources (conversation + files/rules/skills).
