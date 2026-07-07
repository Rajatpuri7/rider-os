# P09 — AUDIT (project health check)

The immune system. Run: after every milestone, on returning from a gap
>1 week, when anything "feels messy", and ideally every ~5 working sessions.
An audit FINDS problems and files them — it does not fix them inline (LAW L1/L5).

## Step 0 — Mechanical checks first

Run `python ops/validate.py`. It catches structural rot cheaply: broken links,
duplicate IDs, missing sections, stale NOW.md, overfull `planning/active/`.
Triage its output before manual sweeps.

## Sweep A — State vs reality

- Does `state/NOW.md` describe what is actually true? (Compare to task files,
  recent session logs.)
- Every `subsystems/*/STATUS.md`: last-updated recent enough for its activity?
  Resume-point still executable?
- `planning/active/`: is each task genuinely being worked? Stalled >2 sessions
  → back to backlog with a note, or split, or escalate its blocker.

## Sweep B — Plan drift

- `planning/ROADMAP.md` vs `planning/done/`: are we where the plan says?
  Slippage >20% on a milestone → flag for re-plan (P03), don't quietly slide dates.
- Riskiest-assumption experiments: actually run early, or perpetually deferred?

## Sweep C — Ledger hygiene

- `state/QUESTIONS.md`: answered-in-practice but still open? Blocking something
  yet assigned to nobody?
- `state/RISKS.md`: any risk materialized (→ it's now an issue/task)? Expired?
  New risks implied by recent lessons?
- `state/ASSUMPTIONS.md`: any assumption now cheaply checkable? Any silently
  load-bearing assumption not in the ledger at all?

## Sweep D — Knowledge integrity

- Duplication scan (LAW L7): same fact/spec/pinout stated in two places?
  Pick the MAP.md home, make others link to it.
- Conflict scan: requirements vs accepted ADRs vs what's actually built —
  any triple that disagrees? (This is the highest-value check in the audit.)
- Every MUST requirement: has a verify-method and traces to ≥1 task/milestone?
  Untraceable MUSTs are silent scope loss.
- Orphans: interfaces no subsystem references, reference files nothing cites,
  tasks pointing at moved/dead paths.

## Sweep E — Kernel feedback (LAW L12)

Read recent `state/LESSONS.md` entries: any lesson that repeats, or that a
protocol/checklist should have prevented? → Draft a kernel change proposal per
`kernel/META.md`.

## Output — the audit report

Write a session log (`state/sessions/YYYY-MM-DD-<n>.md`, Type: audit) with:
findings ranked by severity, each finding → its disposition (new task in
backlog / question / risk / kernel proposal / fixed-trivially-inline).
Update `state/NOW.md` if the audit changed what "next" means. Report the top 3
findings to the human in plain language.
