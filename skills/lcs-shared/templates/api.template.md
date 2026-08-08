---
title: "API Specification: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: api
cot_level: strict
version: "1.0"
status: draft
tags: [api, specification]
summary: "API endpoint specifications for {feature-name}"
source: "srs.md"
related: ["srs.md", "tests.md"]
---

# API Specification: {feature-name}

## Endpoints

### {METHOD} {path}
- **SRS Source:** FR-001
- **Description:** ...
- **Auth:** required / optional / none

#### Request
```json
{
  "field": "type — description"
}
```

#### Response (200)
```json
{
  "field": "type — description"
}
```

#### Errors
| Code | Condition | Message |
|------|-----------|---------|
| 400 | {condition} | {message} |

## Handoff
→ `lcs-task-slicer` — Tasks reference these API specs.
