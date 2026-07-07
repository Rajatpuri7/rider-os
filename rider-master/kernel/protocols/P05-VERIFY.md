# P05 — VERIFY (evidence-based verification)

Nothing in this system is "done" or "true" without passing through here.

## Verification levels (always state which you achieved)

| Level | Meaning | Example |
|---|---|---|
| V0 | Reviewed only — logic read, no execution | Code review, design review |
| V1 | Executed in isolation | Unit test, breadboard test of one module |
| V2 | Executed with real neighbors | Integration test, HIL, subsystem on the bench |
| V3 | Executed in target conditions | On-vehicle, field test, full pipeline on real data |

Claiming a higher level than achieved is the cardinal sin (FAILURE-MODE G6).
A V1 pass does NOT imply V2 will pass — say "V1 done, V2 pending".

## Procedure

1. **Fetch the criteria** from the task file / requirement / test plan. If no
   criteria exist, STOP — write them first and get them sanity-checked (you
   cannot verify against vibes).
2. **Plan the check** (for anything non-trivial, use template TEST-PLAN.md):
   what will be exercised, at which V-level, expected results, environment/setup,
   edge cases (zero, max, disconnect, power-cycle, garbage input, repeat-run).
3. **Execute and capture.** Raw outputs (logs, terminal output, measurements,
   photos, scope shots) → `verification/evidence/<task-or-test-id>/`.
   Capture BEFORE interpreting — evidence first, narrative second.
4. **Compare** result vs expected, item by item. Partial pass = fail with
   detail, never rounded up to pass.
5. **Report** → `verification/test-reports/` (template TEST-REPORT.md):
   verdict, V-level, evidence links, deviations, anomalies (anomalies you can't
   explain → `state/QUESTIONS.md` — unexplained weirdness always returns).
6. **Propagate**: task file gets verdict + report link; REQUIREMENTS.md rows
   this verifies get status + link; regressions → P08 + a task.

## Reproducibility rule

A verification someone else can't re-run is anecdote, not evidence. The report
must record: exact commands / procedure, environment (versions, hardware rev,
calibration state), input data used. If reproduction needs a rig, describe the
rig.

## Independent-check heuristic

For safety-tagged or irreversible items: verify by a DIFFERENT method than the
one used to build (e.g., code computed it → check against hand calculation or
simulation; CAD says it fits → check against printed template or measurement).
Same-method verification shares the same blind spots.
