# Shared Coding Workflow Contract

This file defines canonical artifact format, folder conventions, Handoff section, and token-optimization rules used by all skills in this pack.

## Folder Convention
All runtime artifacts live under:
```
.lcs/docs/<timestamp>-<slug-work-item>/
```

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
