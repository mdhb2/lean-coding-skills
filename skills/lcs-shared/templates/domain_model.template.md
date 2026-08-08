---
title: "Domain Model: {project-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-domain-modeling"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [domain-model, ubiquitous-language]
summary: "Ubiquitous language and domain boundaries for {project-name}"
status: draft
artifact_type: domain_model
source: "{source-file}"
cot_level: standard
version: "1.0"
---

# Domain Model: {project-name}

## Domain Boundaries

<!-- List bounded contexts and their responsibilities -->

| Bounded Context | Responsibility | Owner |
|---|---|---|
| {context-1} | {responsibility} | {owner} |

## Ubiquitous Language

<!-- Glossary of domain terms with precise definitions -->

| Term | Definition | Used In |
|---|---|---|
| {term} | {definition} | {bounded-context} |

## Entities & Value Objects

<!-- Key domain objects -->

### Entities (have identity)

| Entity | Properties | Invariants |
|---|---|---|
| {entity} | {properties} | {invariants} |

### Value Objects (no identity, immutable)

| Value Object | Properties | Validation |
|---|---|---|
| {value-object} | {properties} | {validation} |

## Domain Events

<!-- Things that happened in the domain -->

| Event | Trigger | Payload |
|---|---|---|
| {event} | {trigger} | {payload} |

## Aggregate Boundaries

<!-- Which entities belong together -->

| Aggregate | Root Entity | Contained Entities | Consistency Boundary |
|---|---|---|---|
| {aggregate} | {root} | {contained} | {boundary} |

## Relationships

<!-- How bounded contexts connect -->

| From | To | Type | Mechanism |
|---|---|---|---|
| {context-a} | {context-b} | {sync/async} | {mechanism} |

## Anti-Corruption Layers

<!-- Interfaces that translate between contexts -->

| ACL | Translates From | Translates To | Purpose |
|---|---|---|---|
| {acl} | {external} | {internal} | {purpose} |

## Open Questions

- [ ] {question-1}
- [ ] {question-2}

## Sources Checked

- {source-1}
- {source-2}

## Handoff

Next recommended skill: lcs-toprd
Next file read: {next-file}
Current phase: domain-modeling
