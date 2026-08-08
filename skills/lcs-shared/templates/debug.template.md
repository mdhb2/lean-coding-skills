---
title: "Debug Investigation: {bug-description}"
format_version: "okf/0.2"
authors:
  - type: human
    name: "{reporter}"
  - type: agent
    name: "lcs-debug"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: debug
cot_level: standard
version: "1.0"
status: draft
tags: [debug, investigation]
summary: "Bug investigation and root cause analysis for {bug-description}"
source: "user input, logs, error traces"
related: []
---

# Debug Investigation: {bug-description}

## Bug Report
- **Reporter:** {name}
- **Severity:** critical / high / medium / low
- **Environment:** {dev / staging / prod}

## Reproduction Steps
1. {Step 1}
2. {Step 2}
3. {Step 3}

## Expected Behavior
{What should happen}

## Actual Behavior
{What actually happens}

## Investigation Notes
### Hypothesis 1: {description}
- Evidence: {for / against}
- Verdict: confirmed / rejected / inconclusive

### Hypothesis 2: {description}
- Evidence: {for / against}
- Verdict: confirmed / rejected / inconclusive

## Root Cause
{Confirmed root cause with evidence}

## Proposed Fix Plan
- **File(s):** {affected files}
- **Approach:** {high-level fix description}
- **Risk:** {risk assessment}

## SRC-### (if product/behavior requirement discovered)
### SRC-001: {requirement from bug}
- {description of implied requirement}

## Handoff
→ `lcs-toprd` — Create PRD for fix (if product change needed).
→ Direct fix — Apply proposed fix (if simple bug).
