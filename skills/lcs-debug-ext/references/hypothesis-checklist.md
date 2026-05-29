# Hypothesis Checklist

Use this reference when forming or reviewing the ranked hypotheses section.

## Generate 3-5 Ranked Hypotheses

Start with multiple plausible causes so the investigation does not anchor on the first explanation. Rank by evidence fit, likelihood, blast radius, and ease of falsification.

Each hypothesis should include:

- Name.
- Why it is plausible.
- Supporting evidence.
- Evidence that would disprove it.
- Predicted observation.
- Confidence: High, Medium, or Low.
- Targeted probe.

If fewer than 3 useful hypotheses exist, explain why. Sparse evidence is a valid reason.

## Make Hypotheses Falsifiable

A useful hypothesis predicts something observable. Use this format:

```text
If <X> is the cause, then <Y observation> should be true, and <Z check> should confirm or disprove it.
```

Weak:

```text
Maybe auth is broken.
```

Better:

```text
If expired session middleware is rejecting valid users, then the request should fail before controller code runs, and a boundary log before and after middleware should confirm or disprove it.
```

## Define Predictions

Predictions should be concrete:

- A function receives `null` where a value is expected.
- A request fails before a route handler is reached.
- A config value differs between local and CI.
- A database query returns duplicate rows.
- A cache key omits tenant or user identity.
- A retry path runs twice and mutates state twice.

Avoid predictions that cannot be checked from logs, tests, debugger output, source inspection, or a small command.

## Avoid Anchoring

- Write hypotheses before choosing a favored fix.
- Include at least one alternative outside the initially suspected file when evidence supports it.
- Check whether observed symptoms could be downstream effects.
- Prefer disproof probes that separate two competing causes.
- Lower confidence when evidence comes from pattern matching rather than reproduction.

## Assign Confidence

High confidence requires reproduced behavior or direct artifact evidence plus a narrow predicted check.

Medium confidence means the hypothesis fits evidence, but reproduction, environment, or disproof is incomplete.

Low confidence means sparse evidence, broad symptom, or indirect reasoning.

## Map Hypotheses To Probes

Each hypothesis should have one targeted probe:

| Hypothesis Type | Good Probe |
| --- | --- |
| Boundary input mismatch | Log or inspect input at caller and callee |
| Async timing or race | Repeat lightweight run 3-5 times and compare ordering |
| Config/environment drift | Compare effective config at runtime |
| Data shape issue | Capture minimal failing payload and schema expectation |
| Query or persistence bug | Inspect generated query and affected records |
| Cache/state leak | Add cache key inspection and state reset check |
| Regression from diff | Compare changed branch against known-good behavior |

The probe should confirm or disprove the hypothesis without modifying production behavior.
