---
title: "Codebase Architecture: {repo-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-codebase-doc"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: codebase_doc
cot_level: strict
version: "1.0"
status: active
tags: [architecture, documentation, codebase]
summary: "Architecture documentation for {repo-name}"
source: "repository scan"
related: ["STRUCTURE.md", "STACK.md", "ARCHITECTURE.md"]
---

# Codebase Architecture: {repo-name}

## Overview
{High-level description of what this codebase does and its primary purpose.}

## Technology Stack
- **Language:** {language + version}
- **Framework:** {framework}
- **Database:** {db if any}
- **Key Dependencies:** {top 5 deps}

## Directory Structure
```
├── src/
│   ├── {module}/    — {purpose}
│   └── {module}/    — {purpose}
├── tests/           — {test structure}
└── config/          — {config files}
```

## Key Entry Points
| Entry Point | Path | Purpose |
|-------------|------|---------|
| Main | {path} | {what it does} |
| API | {path} | {what it does} |

## Architecture Patterns
- {Pattern 1 — where and why}
- {Pattern 2}

## Handoff
→ `lcs-onboarding` — Generate developer onboarding guide.
→ `lcs-toprd` — Use architecture context for PRD.
