---
title: "Database Changes: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-tosrs"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: db
cot_level: strict
version: "1.0"
status: draft
tags: [database, schema, migration]
summary: "Database schema changes for {feature-name}"
source: "srs.md"
related: ["srs.md", "tests.md"]
---

# Database Changes: {feature-name}

## Schema Changes

### Table: {table_name}
- **Operation:** create / alter / drop
- **SRS Source:** FR-001

```sql
-- Migration
{DDL statement}
```

| Column | Type | Nullable | Default | Notes |
|--------|------|----------|---------|-------|
| id | uuid | no | gen_random_uuid() | PK |
| {col} | {type} | {y/n} | {default} | {notes} |

## Indexes
| Table | Columns | Type | Reason |
|-------|---------|------|--------|
| {table} | {cols} | btree/gin/gist | {why} |

## Migrations
1. `{timestamp}_{description}.sql` — {what it does}

## Handoff
→ `lcs-task-slicer` — Tasks include migration steps.
