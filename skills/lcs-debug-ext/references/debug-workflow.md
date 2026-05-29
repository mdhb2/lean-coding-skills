# Debug Workflow Reference

Use this reference when the investigation path is unclear or the report needs stronger evidence discipline.

## Feedback Loop Principles

A feedback loop is the smallest repeatable signal that says whether the bug is present. Favor loops that are fast, specific, and easy to rerun.

Preferred order:

1. Existing failing test.
2. Small targeted test command.
3. CLI invocation with fixture input.
4. HTTP request against a local or dev server.
5. Minimal harness for the failing path.
6. Manual reproduction checklist.
7. Human-in-the-loop notes using `scripts/hitl-loop.template.sh`.

Good feedback loops report one clear result: pass, fail, symptom observed, or symptom not observed. Weak loops depend on broad manual exploration, hidden state, or many unrelated subsystems.

## Lightweight Reproduction Strategies

- Start from the user-provided failing command, route, screen, or test.
- Reduce inputs only enough to isolate the symptom.
- Prefer real call sites over artificial unit-only paths when the bug depends on integration behavior.
- Record exact commands, input, environment clues, and observed output.
- If a server is required, document that requirement rather than pretending a command is self-contained.

## Evidence Collection Guidance

Capture evidence before forming root-cause claims:

- Error text and stack trace.
- Relevant log lines.
- Failing command and exit code.
- Request payload or input sample.
- Expected vs actual behavior.
- Source paths inspected.
- Recent diffs when available.
- Environment details when relevant.

Separate confirmed facts from hypotheses. User reports are evidence, but they are not automatically confirmed observations unless reproduced or directly supported by logs, traces, screenshots, test output, or source code.

## Failure Characterization

Classify reproduction status:

- Reproduced: the agent observed the same symptom through a feedback loop.
- Partially reproduced: related failure observed, but symptom differs or evidence is incomplete.
- Not reproduced: attempted loop did not produce the symptom.
- Evidence-only: no run was possible; investigation is based on provided artifacts.

Classify confidence:

- High: reproduced symptom plus code evidence supports a narrow cause.
- Medium: strong evidence exists but reproduction or disproof is incomplete.
- Low: evidence is sparse, indirect, or mostly user-provided.

## Non-Deterministic Bugs

For flaky or timing-sensitive behavior:

- Do not run expensive stress loops by default.
- Prefer 3-5 lightweight repetitions when a cheap command exists.
- Record observed count, run count, and confidence.
- Look for shared state, async timing, race conditions, cache, network dependency, clock dependency, ordering, retries, and environment variance.
- Suggest heavier stress loops only as optional follow-up when the user approves the cost.

## When To Stop And Ask

Stop and ask for more evidence when:

- No symptom, log, command, or reproduction path is available.
- The expected behavior is unknown.
- The relevant subsystem cannot be identified from available context.
- A required service, secret, account, dataset, or environment is unavailable.
- The next step would require modifying source files, tests, config, docs, or instructions.

Ask for the smallest useful artifact: failing command, exact error, stack trace, log excerpt, input sample, HAR file, screenshot, screen recording, reproduction steps, or environment notes.

## When Not To Guess

Do not state root cause as fact when:

- Only one plausible hypothesis was considered.
- No predicted observation was checked.
- Similar errors exist but source evidence differs.
- A proposed patch has not been validated against a feedback loop.

Use `Unknown`, `Probable`, or `[TODO]` instead.

## Avoid Over-Instrumentation

- Probe boundaries that distinguish hypotheses.
- Use one variable at a time.
- Prefer one targeted log over broad logging.
- Give every temporary debug log a unique prefix such as `[DEBUG-lcs-7f3a]`.
- Include cleanup command: `grep -R "\[DEBUG-lcs-7f3a\]" .`.
- Do not recommend permanent noisy logs unless the product needs observability there.
