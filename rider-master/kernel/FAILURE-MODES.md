# FAILURE-MODES.md — Known ways AI models ruin engineering work, and the antidotes

> This file is the distilled scar tissue. Before starting a task, read the
> General section plus the section matching your task type. Each entry:
> the failure, how it smells, the countermeasure.

## General (every task type)

| # | Failure | Smell | Countermeasure |
|---|---|---|---|
| G1 | Premature action | Producing code/designs within the first minute | Boot first. Write the ORIENTATION block. No output before understanding. |
| G2 | Context amnesia | Contradicting last week's decisions | `state/NOW.md` + ADR index are authoritative. Check both before proposing anything. |
| G3 | Confident fabrication | Precise-sounding numbers, APIs, pinouts with no source | LAW L4 tags. If you can't cite a file in `knowledge/` or a test, mark [ASSUMPTION]. |
| G4 | Sycophancy | Agreeing with the human's flawed premise to be helpful | Your job is correct engineering, not agreement. State disagreement + reason + defer to human's final call. |
| G5 | Scope creep | "I also refactored/improved/added..." | LAW L5. Extra ideas → `planning/backlog/`, one line each. |
| G6 | Verification theater | "This should work now" | Banned phrase. Run it, or say "UNVERIFIED" in bold. |
| G7 | Duplicate work | Rebuilding something that exists | Search `planning/done/`, the subsystem tree, and `knowledge/` before creating anything. |
| G8 | Summary drift | Each retelling of a fact mutates it | Don't retell — link to the one home of the fact (LAW L7). |
| G9 | Question hoarding | Asking the human 15 things one at a time | Batch questions. Attempt answers from `knowledge/` first; ask only what files can't answer. |
| G10 | Silent failure swallowing | try/except pass, ignoring stderr, skipping failed steps | Every error is either handled with a reason or surfaced. Never both ignored and unreported. |

## Planning tasks

| # | Failure | Countermeasure |
|---|---|---|
| P1 | Plans that are prose, not plans | Every plan item has: deliverable, done-when, dependencies. If you can't state done-when, you don't understand the item. |
| P2 | No failure path | Every plan names its riskiest assumption and the cheapest experiment to test it FIRST (fail fast). |
| P3 | Uniform granularity | Near-term items small and concrete; far-term items coarse. Refining month-3 details today is waste. |
| P4 | Ignoring the critical path | Identify which item, if late, delays everything. Hardware lead times are usually it. Order/verify long-lead items first. |

## Implementation tasks (code, CAD, circuits)

| # | Failure | Countermeasure |
|---|---|---|
| I1 | Editing without reading | Read the file and its neighbors first. Match existing style, don't impose your own. |
| I2 | Interface breakage | Touching anything in `integration/interfaces/`? Update the doc + list affected subsystems BEFORE coding. |
| I3 | Happy-path-only | Ask: what happens at zero, at max, at disconnect, at power loss, at garbage input? Handle or explicitly document as out of scope. |
| I4 | Magic numbers | Every constant gets a name and a source comment (datasheet page, measurement, ADR). |
| I5 | Untestable output | If you can't describe how to verify it, redesign it until you can. Design for test is not optional in hardware projects. |
| I6 | Dependency sprawl | New library/tool = new failure surface. Justify in the task log; add to `env/ENVIRONMENT.yaml` or it doesn't exist. |

## Debugging tasks

| # | Failure | Countermeasure |
|---|---|---|
| D1 | Shotgun fixes | One hypothesis, one change, one measurement. Revert what didn't help. P08 is mandatory. |
| D2 | Fixing symptoms | Ask "why" until you reach a cause you can prove. Patch + open a task for the root cause if you must ship. |
| D3 | Trusting the report | Reproduce before fixing. The reported symptom is data, not diagnosis. |
| D4 | Forgetting the fix | Every resolved bug → one line in `state/LESSONS.md`: symptom, root cause, fix. |

## Research tasks

| # | Failure | Countermeasure |
|---|---|---|
| R1 | Source-free synthesis | Every claim in a research note carries a source. No source = clearly marked speculation. |
| R2 | First-result bias | Minimum two independent sources for load-bearing facts (part specs, algorithm claims, prices). |
| R3 | Stale data | Record source dates. Component availability, prices, API versions decay fast — note the retrieval date. |
| R4 | Answering the wrong question | Restate the research question at the top of the note; check the conclusion actually answers it. |

## Decision tasks

| # | Failure | Countermeasure |
|---|---|---|
| C1 | Two-option tunnel vision | Trade studies list ≥3 options including "do nothing / defer". |
| C2 | Criteria invented after preference | Write weighted criteria BEFORE scoring options. |
| C3 | Hidden constraint violation | Check PROJECT_PROFILE constraints and existing ADRs before recommending. |
| C4 | Reversibility blindness | State whether the decision is reversible. Irreversible decisions get stricter evidence + human sign-off (LAW L11). |

## Hardware-touching tasks

| # | Failure | Countermeasure |
|---|---|---|
| H1 | Datasheet-free confidence | Pin assignments, voltage levels, current limits: verify against the datasheet in `knowledge/reference/`, cite page. |
| H2 | No rollback path | Before flashing/rewiring: know how to get back to the last working state. Write it down first. |
| H3 | Ideal-world models | Real sensors drift, real clocks skew, real PWM chips run fast. Leave calibration knobs; plan a calibration step. |
| H4 | Smoke-test skipping | Power-on checklist before full integration: voltages at test points, current draw sanity, magic smoke watch. |
