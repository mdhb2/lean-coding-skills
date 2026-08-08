---
title: "PRD: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-toprd"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: prd
cot_level: standard
version: "1.0"
status: draft
tags: [prd, requirements]
summary: "Product Requirements Document for {feature-name}"
source: "{explore.md or debug.md path}"
related: []
---

# PRD: {feature-name}

## Problem Statement
{What problem does this solve? For whom?}

## Goals & Non-Goals
### Goals
- {Goal 1}

### Non-Goals
- {Explicit non-goal 1}

## Affected Areas / Files
| File/Area | Change Type | Notes |
|-----------|-------------|-------|
| {path} | create/modify/delete | {why} |

## Requirements
### SRC-001: {requirement-name}
- Description: ...
- Priority: high/medium/low

## Acceptance Criteria
- [ ] {Criterion 1}

## Test Strategy
- {How will this be tested?}

## Security Considerations
- {Any security implications?}

## Performance Considerations
- {Any performance implications?}

## Open Questions
- {Question 1}

## Handoff
→ `lcs-prd-reviewer` — Harden and security-check this PRD.
