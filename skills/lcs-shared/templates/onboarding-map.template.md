---
title: "Onboarding Map: {repo-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-onboarding"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: onboarding_map
cot_level: standard
version: "1.0"
status: active
tags: [onboarding, architecture-map]
summary: "Structural map of {repo-name} for developer navigation"
source: "repository scan"
related: ["onboarding.md"]
---

# Onboarding Map: {repo-name}

## Module Dependency Graph
```
{entry-point}
├── {module-a} → {module-b}
├── {module-c}
└── {shared-utils}
```

## Module Inventory
| Module | Path | Purpose | Key Exports |
|--------|------|---------|-------------|
| {name} | {path} | {purpose} | {exports} |

## Data Flow
```
{input} → {module-a} → {module-b} → {output}
```

## Configuration Map
| Config | Path | Affects |
|--------|------|---------|
| {name} | {path} | {what it controls} |

## Test Structure
| Test Suite | Path | Covers |
|-----------|------|--------|
| {name} | {path} | {modules/features} |

## Handoff
→ Reference companion doc: `onboarding.md`
