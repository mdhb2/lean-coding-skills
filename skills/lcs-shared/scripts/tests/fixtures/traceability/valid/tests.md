---
title: "Tests: user-profile-jwt"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: "2026-08-08"
updated: "2026-08-08"
tags: [tests, fixture, regression]
summary: "Test plan mapping AC-001..003 to TEST-001..003"
status: reviewed
related: ["srs.md"]
artifact_type: tests
source: "srs.md"
cot_level: strict
version: "1.0"
timestamp: 2026-08-08T12:35:00+07:00
---

# Tests: user-profile-jwt

## TEST-001 Profile endpoint returns JSON

- Covers AC-001
- Steps: login, call GET /api/profile, assert 200 + JSON body.

## TEST-002 Passwords stored as bcrypt

- Covers AC-002
- Steps: register user, inspect DB, assert bcrypt hash present.

## TEST-003 Rate limiting triggers 429

- Covers AC-003
- Steps: 5 failed logins, assert 429 on 6th.

## Chain of Truth Report

| Stage | Detail |
|-------|--------|
| Source | srs.md AC-001..003 |
| Verification | each AC mapped to a TEST |

## Handoff

Next recommended skill: lcs-task-slicer
