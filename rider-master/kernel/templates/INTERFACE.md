# INTERFACE — <side A> ⇄ <side B>

> This document is the contract (LAW L8). Subsystems build against THIS, not
> against each other's internals. Change process is at the bottom.

- **ID**: IF-<slug> · **Status**: draft | stable | deprecated
- **Parties**: `subsystems/<a>/` ⇄ `subsystems/<b>/`
- **Kind**: data | electrical | mechanical | API | protocol | timing | human-procedure

## Contract
<The precise agreement. Pick the relevant blocks, delete the rest:>

**Data/API**: message formats, units (!), frames of reference, ranges, update
rates, encoding, error values, timeout behavior.

**Electrical**: connector + pinout table, voltage levels, current budget, logic
family, protection present/absent.

**Mechanical**: mounting pattern, envelope, mass budget, fastener spec,
tolerances, datum references.

**Timing**: who initiates, deadlines, jitter tolerance, startup order,
failure/absence behavior (what does B do when A is silent?).

## Assumptions each side may make about the other
- A may assume: …
- B may assume: …
<Anything not listed here may NOT be assumed.>

## Verification
How compliance is checked: <loopback test, checker script, gauge, continuity
test…> — link test plans/reports when they exist.

## Change log (append-only)
| Date | Change | Why | Dependents flagged |
|---|---|---|---|
| | initial draft | | — |

## Change process
1. Propose the change HERE first (not in code/CAD).
2. List every dependent subsystem in the change-log row.
3. Notify: add a line to each dependent's `STATUS.md` inbox + `state/NOW.md`.
4. Then implement on both sides.
