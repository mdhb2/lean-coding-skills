---
name: lcs-toprd
description: Use this skill whenever the user asks to produce a lean, implementation-focused PRD from exploration, debug notes, or direct requirements. Trigger on requests to "create PRD", "write PRD", "plan feature", or when user asks for acceptance criteria, test strategy, or technical approach. Prefer concise, developer-ready PRDs that include Affected Areas / Files to limit code reads.
---

LCS ToPRD Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Create or update prd.md. Keep practical for coding. Include security, performance, acceptance criteria, test strategy.

Trigger
- Activate when user requests to "create PRD", "write PRD", "plan feature", or when user asks for acceptance criteria, test strategy, or technical approach.

Behavior checklist
- Read state.md first if continuing. Otherwise locate explore.md or debug.md.
- Ensure PRD uses Affected Areas / Files to limit later code reads.
- Write prd.md under .lcs/docs/<yyyymmdd-HHMMSS>-<slug-work-item>/prd.md. Do not create versioned copies.
- Provide clear Acceptance Criteria and Test Strategy (unit/integration/e2e where applicable).
- Add Review Notes with last reviewed/summary/changes applied.
- End with Handoff recommending lcs-prd-reviewer.

Prompt templates
- Starter: "Create PRD for <work-name> based on explore.md"
- Minimal PRD ask: "Include objective, scope, requirements, acceptance criteria, test strategy"

PRD Template Structure
Use this template when writing prd.md. Keep concise and implementation-focused.

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
Next recommended skill: lcs-prd-reviewer
Next file to read: .lcs/docs/<yyyymmdd-HHMMSS>-<slug-work-item>/prd.md
Current phase: prd
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary>
Suggested next command: Review and fix prd.md
