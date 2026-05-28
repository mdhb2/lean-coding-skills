---
name: lcs-prd-reviewer
description: Use this skill whenever the user asks to review, harden, or security-check an existing PRD. Trigger on phrases like "review prd", "audit prd", "harden prd", "security review of prd". This skill aggressively looks for ambiguous acceptance criteria, missing tests, and missing Affected Areas / Files, and writes the hardened/reviewed output to prd-enhanced.md.
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

# LCS PRD Reviewer Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Review `prd.md`, harden acceptance criteria, test strategy, security, performance, and maintainability.
- Write and save the hardened PRD into `prd-enhanced.md` inside the same work-item directory.

Trigger
- Activate when user requests to "review prd", "audit prd", "harden prd", "security review of prd", or when completing the PRD generation phase.

Behavior checklist
- Read `.lcs/state.md` to identify the active work-item directory: `.lcs/work-items/<timestamp>-<slug-work-item>/`. 
- Read `prd.md` inside that active directory.
- Review it for gaps: ambiguous acceptance criteria, missing tests, security, performance, and missing Affected Areas / Files.
- Create or update `prd-enhanced.md` in the same directory with the fully hardened specifications.
- Keep the original `prd.md` intact, but write all improvements and hardenings directly to `prd-enhanced.md`.
- Update `Review Notes` section in `prd-enhanced.md` with:
  - Last Reviewed: <timestamp>
  - Summary: <summary of revisions/gaps found>
  - Changes Applied: <improvements written into prd-enhanced.md>
- End with Handoff section pointing to the next logical step (e.g., `lcs-task-slicer` or task slicing command).

Prompt templates
- Starter: "Review prd.md dan perbaiki menjadi prd-enhanced.md agar siap di-slice"
- Checklist ask: "Apakah acceptance criteria cukup spesifik?"

prd-enhanced.md Structure
Must be exact structure as prd.md:

# PRD: <work-name>

## Objective
<what is the goal>

## Background
<why we are doing this, context>

## Source Context
<links to explore.md, debug.md, or other sources>

## Scope
<what is included>

## Non-Goals
<what is excluded>

## Requirements
<functional requirements checklist>

## Technical Approach
<architecture, libraries, database changes, APIs>

## Affected Areas / Files
<files and modules that need edits>

## Security Considerations
<vulnerabilities, authentication, authz>

## Performance Considerations
<latency, database query limits, caching>

## Potential Bugs / Edge Cases
<what could go wrong, validations>

## Acceptance Criteria
- AC 1: <detail>
- AC 2: <detail>

## Test Strategy
- Unit: <spec>
- Integration: <spec>
- E2E: <spec>

## Review Notes
- Last Reviewed: <date>
- Summary: <summary of revisions>
- Changes Applied: <list of changes>

## Handoff
Next recommended skill: lcs-task-slicer
Next file to read: .lcs/work-items/<timestamp>-<slug-work-item>/prd-enhanced.md
Current phase: prd_review
Current confidence: high
Blocking questions: None
Risks to carry forward: <risks>
Suggested next command: Slice prd-enhanced.md menjadi tasks.md
