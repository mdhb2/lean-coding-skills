# Inquiry Checkpoints

Use this file to investigate and validate every generated doc.

## STACK
- Required questions: What languages, runtimes, frameworks, package managers, and production/development dependencies exist?
- Evidence expectation: manifests, lockfiles, build configs, runtime configs, scan output.
- Avoid unsupported claims: inferred stack from folder names only.
- Unknown markers: `[TODO]` if missing evidence, `[ASK USER]` for intended platform/runtime support.
- Validation: every stack claim must map to at least one concrete file path.

## STRUCTURE
- Required questions: What are top-level dirs, entry points, key modules, generated folders, and workspace boundaries?
- Evidence expectation: repository tree, manifests, module configs, entrypoint files.
- Avoid unsupported claims: labeling generated folders as source architecture.
- Unknown markers: `[TODO]` for uncertain directory role, `[ASK USER]` for ownership intent.
- Validation: key structure notes include concrete paths.

## ARCHITECTURE
- Required questions: What layers/modules exist? How does data/control flow? How is state managed?
- Evidence expectation: source imports, routing, service boundaries, config wiring.
- Avoid unsupported claims: naming patterns (hexagonal/clean/event-driven) without direct evidence.
- Unknown markers: `[TODO]` for unresolved flow, `[ASK USER]` for intended architecture and tradeoffs.
- Validation: include intent-vs-reality section with evidence.

## CONVENTIONS
- Required questions: naming, formatting, imports, errors, logging, config, API conventions.
- Evidence expectation: lint/format configs, representative source files, style rules in CI.
- Avoid unsupported claims: “team standard” without evidence.
- Unknown markers: `[TODO]` when convention appears inconsistent, `[ASK USER]` for undocumented standards.
- Validation: each convention linked to observed files.

## INTEGRATIONS
- Required questions: external APIs, databases, auth, queues, storage, observability, required env vars.
- Evidence expectation: dependencies, client initialization code, docker compose, migration files, env examples.
- Avoid unsupported claims: inferring services from variable names alone.
- Unknown markers: `[TODO]` when integration cannot be confirmed, `[ASK USER]` for ownership/SLA intent.
- Validation: every integration lists proof paths.

## TESTING
- Required questions: frameworks, test layout, commands, fixtures/mocking, coverage, CI execution, gaps.
- Evidence expectation: test files, package scripts, CI jobs, coverage tooling configs.
- Avoid unsupported claims: asserting quality level without measurable signal.
- Unknown markers: `[TODO]` for missing command or coverage details, `[ASK USER]` for target test policy.
- Validation: testing gaps clearly separate observed vs expected behavior.

## CONCERNS
- Required questions: debt, security, performance, maintainability, churn, complexity, doc drift, open questions.
- Evidence expectation: scan markers, large files, churn report, config mismatches, outdated docs.
- Avoid unsupported claims: high-risk labels without concrete indicators.
- Unknown markers: `[TODO]` for unresolved risk validation, `[ASK USER]` for priority and risk appetite.
- Validation: concerns are ranked and evidence-backed.
