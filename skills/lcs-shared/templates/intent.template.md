---
title: "Intent: {short-description}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-explore"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: intent
cot_level: light
version: "1.0"
status: refining
tags: [intent]
summary: "Refined user intent for {feature/problem}"
source: "explore.md"
related: ["explore.md"]
---

# Intent: {short-description}

## Problem

{The actual problem being solved, not the user's proposed solution.}

## Proposed Outcome

{The change or result the user wants, described without implementation detail.}

## Affected Users and Systems

- Users: {who is affected}
- Systems: {systems/data involved}

## Constraints

- {constraint that must be respected}

## Out of Scope

- {explicitly excluded item}

## Open Questions

- {unresolved question, or None}

## Intent Status

- Status: {refining|confirmed|blocked|superseded}
- Reason: {why this status applies}

## Handoff

Next recommended skill: lcs-toprd
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/intent.md
Current phase: explore
Current confidence: {low|medium|high}
Blocking questions: {list or None}
Risks to carry forward: {summary or None}
Source of Truth Bundle: .lcs/state.md, explore.md, intent.md
Must Preserve IDs: {list or None}
Unresolved IDs: {list or None}
Suggested next command: Create PRD from exploration and intent
