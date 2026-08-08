---
title: "Research: {topic}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-research"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [research, evidence, technical]
summary: "Evidence-based research findings on {topic}"
status: draft
artifact_type: research
source: "{source-file}"
cot_level: standard
version: "1.0"
---

# Research: {topic}

## Question

<!-- What specific question are we answering? -->

{research-question}

## Findings

### Finding 1: {title}

**Evidence:**
- Source: {primary-source-url}
- Date: {date}
- Reliability: {high/medium/low}

**What we learned:**
{finding-detail}

**Confidence:** {high/medium/low}
**Caveats:** {limitations}

### Finding 2: {title}

**Evidence:**
- Source: {primary-source-url}
- Date: {date}
- Reliability: {high/medium/low}

**What we learned:**
{finding-detail}

**Confidence:** {high/medium/low}
**Caveats:** {limitations}

## Sources

| # | Source | Type | Reliability | Date |
|---|---|---|---|---|
| 1 | {url-or-ref} | {official-doc/blog/paper} | {high/medium/low} | {date} |

## Rejected Sources

<!-- Sources checked but not used, with reasons -->

| Source | Reason Rejected |
|---|---|
| {url} | {reason} |

## Recommendations

Based on findings:

1. **Recommendation 1:** {recommendation}
   - Evidence: {which-finding}
   - Confidence: {high/medium/low}

2. **Recommendation 2:** {recommendation}
   - Evidence: {which-finding}
   - Confidence: {high/medium/low}

## Open Questions

- [ ] {question-1}

## Handoff

Next recommended skill: lcs-toprd
Next file read: {next-file}
Current phase: research
