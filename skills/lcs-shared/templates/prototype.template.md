---
title: "Prototype: {feature-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-prototype"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [prototype, validation, quick-test]
summary: "Isolated prototype to validate {feature-name} approach"
status: draft
artifact_type: prototype
source: "{source-file}"
cot_level: strict
version: "1.0"
---

# Prototype: {feature-name}

## Purpose

<!-- What specific hypothesis are we testing? -->

{hypothesis}

## Design Question

<!-- What decision will this prototype answer? -->

{design-question}

## Prototype Scope

### In Scope
- {scope-item-1}
- {scope-item-2}

### Out of Scope
- {exclusion-1}
- {exclusion-2}

## Implementation

### Files

| File | Purpose |
|---|---|
| {file} | {purpose} |

### Key Decisions

| Decision | Choice | Rationale |
|---|---|---|
| {decision} | {choice} | {rationale} |

## Validation

### Test Cases

| # | Input | Expected Output | Actual |
|---|---|---|---|
| 1 | {input} | {expected} | {actual} |

### Results

{results-summary}

## Conclusions

- **Validated:** {what-was-confirmed}
- **Rejected:** {what-was-disproven}
- **New Questions:** {new-questions}

## Recommendation

{recommendation-for-next-steps}

## Handoff

Next recommended skill: lcs-toprd
Next file read: {next-file}
Current phase: prototype

## Archive

This prototype is isolated to: `.lcs/work-items/{ts}-{slug}-proto/`
