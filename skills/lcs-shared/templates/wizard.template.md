---
title: "Wizard: {procedure-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-wizard"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [wizard, human-in-the-loop, procedure]
summary: "Step-by-step procedure for {procedure-name} with human confirmation"
status: draft
artifact_type: wizard
source: "{source-file}"
cot_level: standard
version: "1.0"
---

# Wizard: {procedure-name}

## Purpose

{procedure-purpose}

## Prerequisites

- [ ] {prerequisite-1}
- [ ] {prerequisite-2}

## Procedure

### Step 1: {step-name}

**Action:** {what-to-do}
**Human Input:** {what-human-needs-to-confirm}
**Expected Result:** {what-should-happen}

### Step 2: {step-name}

**Action:** {what-to-do}
**Human Input:** {what-human-needs-to-confirm}
**Expected Result:** {what-should-happen}

### Step 3: {step-name}

**Action:** {what-to-do}
**Human Input:** {what-human-needs-to-confirm}
**Expected Result:** {what-should-happen}

## Rollback

If step N fails:

1. {rollback-step-1}
2. {rollback-step-2}

## Verification

After completion, verify:
- [ ] {verification-1}
- [ ] {verification-2}

## Audit Trail

| Step | Action | Human Confirmed | Timestamp | Result |
|---|---|---|---|---|
| 1 | {action} | {yes/no} | {timestamp} | {success/fail} |

## Handoff

Next recommended skill: {next-skill}
Next file read: {next-file}
Current phase: wizard
