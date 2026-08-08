---
title: "Debug Report (Report-Only): {issue-description}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-debug-ext"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: debug_ext
cot_level: very_strict
version: "1.0"
status: draft
tags: [debug, report-only, diagnosis]
summary: "Evidence-based diagnosis without code changes for {issue-description}"
source: "codebase, logs, error traces"
related: []
---

# Debug Report (Report-Only): {issue-description}

> **Changes applied: None**

## Confirmed Facts
1. {Fact 1 — verified with evidence}
2. {Fact 2}

## Hypotheses (Ranked)

### H1 (High confidence): {description}
- **Evidence:** {what supports this}
- **Evidence against:** {what contradicts}
- **Confidence:** high / medium / low

### H2 (Medium confidence): {description}
- **Evidence:** ...
- **Confidence:** ...

## Reproduction Notes
```bash
# Steps to reproduce
{commands}
```

## Instrumentation Suggestions
- {Where to add logging}
- {What metrics to check}

## Regression Test Proposal
```{language}
// Proposed test to prevent recurrence
{test code}
```

## Patch Proposal
> ⚠️ NOT applied. Review and apply manually.

```diff
{proposed diff}
```

## [TODO] Missing Evidence
- {What evidence could not be obtained}

## [ASK USER] Decisions Needed
- {What requires human decision}

## Chain of Truth Report
| Stage | Detail |
|-------|--------|
| Source | {files read, logs checked} |
| Assumption | {assumptions made} |
| Plan | {investigation approach} |
| Action | {commands run, analysis performed} |
| Verification | {what was verified} |
| Report | {findings summary} |

## Handoff
→ User review — Apply patch proposal if approved.
