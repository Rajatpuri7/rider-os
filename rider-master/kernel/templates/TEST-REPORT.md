# TEST-REPORT — <what was tested>

- **ID**: TR-<slug> · **Date**: YYYY-MM-DD · **Plan**: <TP link or "ad-hoc (why)">
- **Verdict**: PASS / FAIL / PARTIAL (partial = fail with detail, never rounded up)
- **V-level achieved**: V0 / V1 / V2 / V3 — <one line on what that means here>

## Environment actually used
<If it differs from the plan, say where and why — silent env drift invalidates comparison.>

## Results
| Case | Expected | Observed | Verdict | Evidence |
|---|---|---|---|---|
| 1 | | | pass/fail | `verification/evidence/...` |

## Deviations & anomalies
<Everything odd, even in passing cases. Unexplained anomalies → state/QUESTIONS.md
— they always come back. "None observed" only if you actually looked.>

## Propagation done (checklist)
- [ ] Task file updated with verdict + this link
- [ ] REQUIREMENTS.md rows updated (status + evidence link)
- [ ] Failures → P08 debug entry or new task
- [ ] Anomalies → QUESTIONS.md
