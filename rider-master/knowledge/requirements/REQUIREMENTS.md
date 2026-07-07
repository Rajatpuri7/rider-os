# REQUIREMENTS — what the system must do/be

> One home for all requirements (LAW L7). Every MUST must trace to ≥1 task or
> milestone and carry a verify-method — untraceable MUSTs are silent scope
> loss (audited in P09 sweep D). Safety-tagged rows follow the
> safety-reliability playbook's independent-check rule.

Row format (table per subsystem or per theme, as fits the project):

| ID | Requirement (testable phrasing) | Level | Source | Verify by | Status | Evidence |
|---|---|---|---|---|---|---|
| R-SYS-001 | *(example)* Robot stops within 0.5 m of obstacle at max speed | MUST | competition rules §3.2 | field test scenario TP-estop | unverified | — |

Conventions:
- **ID**: `R-<SUBSYS>-###`, never renumbered, never reused.
- **Level**: MUST / SHOULD / COULD (MoSCoW; WON'T items → archive note, keeps
  descoping explicit).
- **Testable phrasing**: numbers and conditions, not adverbs. "fast" is not a
  requirement; "≤50 ms at p95" is.
- **Status**: unverified | V1 | V2 | V3 | FAILED (link the report either way).

---

*(populated by P01 phase E and P02 mining)*
