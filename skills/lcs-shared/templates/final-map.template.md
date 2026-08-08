---
title: "Final Map: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-doc-finalizer"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: final_map
cot_level: strict
version: "1.0"
status: archived
tags: [documentation, final, architecture-map]
summary: "Structural map of implemented {feature-name}"
source: "task-###.md (all done), srs.md"
related: ["doc.md", "map.md"]
---

# Final Map: {feature-name}

## Files Changed
| File | Change Type | Lines | Purpose |
|------|-------------|-------|---------|
| {path} | created/modified | +X -Y | {purpose} |

## New Modules
| Module | Path | Purpose |
|--------|------|---------|
| {name} | {path} | {what it does} |

## Modified Modules
| Module | Path | What Changed |
|--------|------|--------------|
| {name} | {path} | {summary of change} |

## Dependency Graph (New/Changed)
```
{new-module}
├── {existing-module}
└── {new-module-2}
```

## Test Coverage
| Module | Test File | Coverage |
|--------|-----------|----------|
| {module} | {test-path} | {X%} |

## Handoff
→ Reference companion doc: `doc.md`
