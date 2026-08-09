---
title: "Explore: {short-description}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-explore"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: explore
cot_level: light
version: "1.0"
status: draft
tags: [explore, brainstorm]
summary: "Exploration and trade-off analysis for {feature/problem}"
source: "user input"
related: []
---

# Explore: {short-description}

## Context
{What problem are we solving? Why now?}

## Options Explored
### Option A: {name}
- Description: ...
- Pros: ...
- Cons: ...

### Option B: {name}
- Description: ...
- Pros: ...
- Cons: ...

## Recommendation
{Which option and why. 1-3 lines.}

## Blockers / Open Questions
- {Question 1}
- {Question 2}

## Handoff

Next recommended skill: lcs-toprd
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/explore.md
Current phase: explore
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary or None>
Source of Truth Bundle: .lcs/state.md, explore.md
Must Preserve IDs: SRC-001, SRC-002, ... (from Decision Ledger)
Unresolved IDs: <list or None>
Suggested next command: Create PRD from exploration
