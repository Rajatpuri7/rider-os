# P08 — DEBUG (systematic defect hunting)

Enter when behavior differs from expectation. The discipline: **understand,
then fix** — a fix without a root cause is a time bomb with a snooze button.

## Step 0 — Freeze and capture

Before touching anything: record the exact symptom (verbatim error text, wrong
value, misbehavior), the conditions (inputs, environment, hardware state,
versions), and evidence (log, screenshot, scope shot) →
`verification/evidence/debug-<date>-<slug>/`. Check `state/LESSONS.md` — has
this been seen before?

## Step 1 — Reproduce

- Reproducible on demand → proceed.
- Intermittent → characterize first: how often per N tries? correlated with
  what (temperature, timing, cable position, payload size)? Add instrumentation
  and gather occurrences. **You cannot fix what you cannot see happen.**
- Vanished → don't celebrate. Log it as a risk with the trigger unknown;
  unexplained recoveries always return (usually in a demo).

## Step 2 — What changed?

Most bugs live in the last change: recent commits, config edits, library
updates, rewired connectors, new battery, different room/lighting. Diff
against the last known-good state if one exists.

## Step 3 — Hypotheses BEFORE probes

Write ≥3 candidate causes covering DIFFERENT layers (input/data, config/
environment, code logic, timing/concurrency, hardware/electrical). Rank by
likelihood × cheapness-to-test. Writing them first prevents tunnel vision —
the #1 debugging failure is testing one theory forever.

## Step 4 — Test hypotheses, one variable at a time

- Run the cheapest DECISIVE test first — prefer probes that cut the search
  space in half (binary search across the pipeline: is the data already wrong
  at the input? at the boundary? only at the output?).
- Change ONE thing per probe. Shotgun edits destroy the evidence trail.
- Log every probe: hypothesis | probe | expected | observed. A disproven
  hypothesis is progress; an untested one is a superstition.

## Hardware addendum (when anything physical is involved)

Check in this order before blaming code: power rails under load (measure,
don't assume), grounds shared, connectors seated (reseat anyway), cable
continuity, brownout/reset events, EMI from motors/servos. Half of all
"firmware bugs" on a bench are wiring. Swap-known-good is the fastest divider:
known-good board, cable, sensor, power supply.

## Step 5 — Fix the cause

The fix must explain **all** observations — a fix that explains 4 of 5
symptoms is treating a different bug. If the root cause is upstream (bad
requirement, wrong assumption, interface mismatch), fix it there (LAW L8) and
flag dependents.

## Step 6 — Prove and protect

1. Re-run the original failing case → passes. Re-run neighbors → no regression.
2. Where possible, add the automated check that would have caught this.
3. Evidence per P05, at the honest V-level.

## Step 7 — Harvest

`state/LESSONS.md`: root-cause class, how it could have been caught earlier,
any rule-of-thumb. If a protocol/checklist should have caught it → propose a
kernel change per `kernel/META.md` (LAW L12).

## Escalation valve

Two hypothesis rounds dead + confusion increasing → STOP. Widen the frame:
re-read `state/ASSUMPTIONS.md` (one of them is probably false), ask "what
would have to be true for this behavior to be CORRECT?", write the situation
to `state/QUESTIONS.md`, and bring the human a crisp brief: symptom, repro,
hypotheses killed, evidence paths.
