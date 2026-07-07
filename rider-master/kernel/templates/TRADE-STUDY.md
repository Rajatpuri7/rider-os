# TRADE-STUDY — <subject>

- **Date**: YYYY-MM-DD · **Feeds**: ADR-####
- **Decision statement**: <copied from the framing step of P06 — written BEFORE options>

## Disqualifying constraints (pass/fail — applied first)
| Constraint | Source | A | B | C |
|---|---|---|---|---|
| <e.g. must run on 5V/2A> | R-PWR-003 | pass | FAIL | pass |

Options failing any row are OUT regardless of scores below.

## Weighted criteria (weights sum to 100, set BEFORE scoring)
| Criterion | Weight | Why this weight |
|---|---|---|
| Fitness for requirement | | |
| Simplicity / integration effort | | |
| Cost (money + time) | | |
| Availability / lead time | | |
| Ecosystem, docs, community | | |
| Reversibility | | |

## Scores (1–5). EVERY cell: number + one-line rationale. Numbers alone are theater.
| Criterion (wt) | Option A | Option B | Option C |
|---|---|---|---|
| <criterion> (w) | 4 — <why> | 2 — <why> | 3 — <why> |
| **Weighted total** | | | |

## Sensitivity check (mandatory)
Which single weight or score change flips the winner? <answer>
Verdict: robust / fragile — <if fragile, say so to the human; a fragile win is
a judgment call, not a computed result>.

## Unknowns that could invalidate this
<Facts assumed but not verified. Each is either accepted as a risk
(→ state/RISKS.md) or tested first (→ EXPERIMENT).>

## Recommendation
<One paragraph → feeds the ADR's Decision section.>
