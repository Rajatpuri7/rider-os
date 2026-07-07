# TEST-PLAN — <what is under test>

- **ID**: TP-<slug> · **Date**: YYYY-MM-DD
- **Verifies**: <requirement IDs and/or task done-when items — every row below
  must trace to one>
- **Target V-level**: V1 / V2 / V3 (per P05 table)

## Environment / setup
<Versions, hardware rev, calibration state, test rig description, datasets.
The reproducibility rule (P05) applies: someone else must be able to run this.>

## Test cases
| # | Exercises | Steps | Expected result | Verifies |
|---|---|---|---|---|
| 1 | <nominal path> | | | R-… |
| 2 | <edge: zero/empty> | | | |
| 3 | <edge: max/saturation> | | | |
| 4 | <failure injection: disconnect, garbage input, power-cycle> | | | |
| 5 | <repeat-run: same result twice?> | | | |

> The edge rows are mandatory prompts, not suggestions — delete a row only by
> writing why it doesn't apply.

## Pass criteria for the plan as a whole
<e.g. "all cases pass" or "cases 1–3 pass, case 4 degrades gracefully">

## Risks while testing
<Can this test damage hardware? Need supervision? Current limits set? (LAW L11)>
