---
title: "Invalid: bad status value"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-explore"
created: "2026-08-08"
updated: "2026-08-08"
tags: [fixture, regression]
summary: "Regression fixture: status outside lifecycle must FAIL"
status: pending
related: []
artifact_type: explore
source: "state.md"
cot_level: light
version: "1.0"
timestamp: 2026-08-08T10:00:00+07:00
---

# Invalid: bad status value

## Findings

- Regression case: `status: pending` is not in draft|reviewed|active|archived.

## Chain of Truth Report

| Stage | Detail |
|-------|--------|
| Source | fixture file |
| Verification | validate-okf.py must exit non-zero |

## Handoff

Next recommended skill: lcs-toprd
