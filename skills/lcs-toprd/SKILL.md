---
name: lcs-toprd
description: Use this skill whenever the user asks to produce a lean, implementation-focused PRD from exploration, debug notes, or direct requirements. Trigger on requests to "create PRD", "write PRD", "plan feature", or when user asks for acceptance criteria, test strategy, or technical approach. Prefer concise, developer-ready PRDs that include Affected Areas / Files to limit code reads.
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

LCS ToPRD Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Create or update prd.md. Keep practical for coding. Include security, performance, acceptance criteria, test strategy. Do NOT interview the user — just synthesize what you already know.

Trigger
- Activate when user requests to "create PRD", "write PRD", "plan feature", or when user asks for acceptance criteria, test strategy, or technical approach.

Behavior checklist
- Read state.md first if continuing. Otherwise locate explore.md or debug.md.
- Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the PRD, and respect any ADRs in the area you're touching.
- Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation. A deep module encapsulates a lot of functionality in a simple, testable interface which rarely changes.
- Ensure PRD uses Affected Areas / Files to limit later code reads.
- Write prd.md under .lcs/work-items/<yyyymmdd-HHMMSS>-<slug-work-item>/prd.md. Do not create versioned copies.
- Provide clear Acceptance Criteria and Test Strategy (unit/integration/e2e where applicable).
- Add Review Notes with last reviewed/summary/changes applied.
- End with Handoff recommending lcs-prd-reviewer.

Prompt templates
- Starter: "Create PRD for <work-name> based on explore.md"
- Minimal PRD ask: "Include objective, scope, requirements, acceptance criteria, test strategy"

PRD Template Structure
Use this template when writing prd.md. Keep concise and implementation-focused.

# PRD: <work-name>

## Problem Statement & Objective
- Problem Statement: <what is the problem from user perspective>
- Objective: <what is the goal, how to solve it>

## Background & Solution
- Background: <why we are doing this, context>
- Solution: <the proposed solution from user perspective>

## Source Context
<links to explore.md, debug.md, or other sources>

## Scope & User Stories
<what is included in this scope>

### User Stories
Provide a detailed, numbered list of user stories in this format:
1. As an <actor>, I want a <feature>, so that <benefit>
2. As an <actor>, I want a <feature>, so that <benefit>

## Non-Goals / Out of Scope
<what is excluded / out of scope>

## Requirements
<functional requirements checklist>

## Technical Approach & Implementation Decisions
- Deep Modules Design: <major modules to build/modify, interfaces to introduce, how they isolate logic>
- Technical decisions: <architecture, libraries, database changes, APIs, specific interactions, schema changes>

*Note: Do NOT include specific file paths or code snippets in this section to prevent them from becoming outdated quickly. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it here and note briefly that it came from a prototype. Trim to decision-rich parts only.*

## Affected Areas / Files
<files and modules that need edits. CRITICAL for LCS token-optimization flow!>

## Security Considerations
<vulnerabilities, authentication, authz>

## Performance Considerations
<latency, database query limits, caching>

## Potential Bugs / Edge Cases
<what could go wrong, validations>

## Acceptance Criteria
- AC 1: <detail>
- AC 2: <detail>

## Test Strategy & Testing Decisions
- Testing decisions: <what makes a good test (only test external behavior, not implementation details), modules to test, prior art in the codebase>
- Unit: <spec>
- Integration: <spec>
- E2E: <spec>

## Review Notes
- Last Reviewed: <date>
- Summary: <summary of revisions>
- Changes Applied: <list of changes>

## Chain of Truth Report
### Level
Standard

### Sources Checked
- `.lcs/state.md`
- `<explore.md or debug.md path>`
- <additional files read>

### Assumptions
- <label each [verified] or [unverified]>

### Plan
1. <Step one>
2. <Step two>

### Actions Taken
<Per-step record of what was done>

### Verification
<Command output or manual review result>

### Report
<Structured summary with confidence rating>

## Handoff
Next recommended skill: lcs-prd-reviewer
Next file to read: .lcs/work-items/<yyyymmdd-HHMMSS>-<slug-work-item>/prd.md
Current phase: prd
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary>
Suggested next command: Review and fix prd.md

## Chain of Truth Level

Level: Standard

This skill follows the LCS Chain of Truth protocol at the declared level.
