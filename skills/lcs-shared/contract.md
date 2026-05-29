# Shared Coding Workflow Contract

This file defines canonical artifact format, folder conventions, Handoff section, and token-optimization rules used by all skills in this pack.

## Folder Convention
All runtime artifacts live under:
```
.lcs/work-items/<timestamp>-<slug-work-item>/
```

### Skill-Specific Exception: `lcs-doc-finalizer`
When active skill is `lcs-doc-finalizer`, documentation outputs use dedicated docs subtree:
```
.lcs/docs/<timestamp>-<slug-work-item>/
```
Index file for this subtree:
```
.lcs/docs/docs-index.md
```
Archive target for finalized source artifacts:
```
.lcs/archive/<timestamp>-<slug-work-item>/
```
This exception overrides generic docs/archive path assumptions in other rules.

### Skill-Specific Exception: `lcs-codebase-doc`
When active skill is `lcs-codebase-doc`, repository documentation outputs use:
```
.lcs/codebase/
```
Project intent documents are read from:
```
.lcs/docs/
```
This exception overrides generic runtime artifact path assumptions for codebase mapping and repository documentation outputs.

## Artifact Files
Create only when relevant:
- explore.md
- debug.md
- prd.md
- tasks.md
- state.md
- final-doc.md

## Handoff
Must appear at bottom of every artifact:
```markdown
## Handoff

Next recommended skill:
Next file to read:
Current phase:
Current confidence:
Blocking questions:
Risks to carry forward:
Suggested next command:
```

## Token Optimization Rules
1. Read state.md first when continuing work.
2. Avoid reading all artifacts unless necessary.
3. Use Affected Areas / Files from PRD to narrow code inspection.
4. Executor focuses on one task at a time.
5. Update canonical files rather than create versions.
