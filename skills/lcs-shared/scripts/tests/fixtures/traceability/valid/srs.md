---
title: "SRS: user-profile-jwt"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: "2026-08-08"
updated: "2026-08-08"
tags: [srs, fixture, regression]
summary: "Deterministic SRS for user-profile-jwt"
status: reviewed
related: ["prd-enhanced.md"]
artifact_type: srs
source: "prd-enhanced.md"
cot_level: strict
version: "1.0"
timestamp: 2026-08-08T12:30:00+07:00
---

# SRS: user-profile-jwt

## Functional Requirements

### FR-001 Profile endpoint

Return profile data for the authenticated user.

### FR-002 Password hashing

Passwords stored as bcrypt hashes, never plaintext.

### FR-003 Rate limiting

Login endpoint limits to 5 failed attempts per 15 minutes.

## Acceptance Criteria

### AC-001 Profile returns JSON

GET /api/profile returns 200 with profile JSON when JWT valid.

### AC-002 Passwords hashed

DB stores bcrypt hash for every password.

### AC-003 Rate limit enforced

Login returns 429 after 5 failed attempts.

## Chain of Truth Report

| Stage | Detail |
|-------|--------|
| Source | prd-enhanced.md |
| Verification | AC-001..003 derived from AC in PRD |

## Handoff

Next recommended skill: lcs-task-slicer
