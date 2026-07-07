# P04 — EXECUTE (the core work loop)

The protocol for actually doing engineering work. One task at a time.

## Pre-flight gate (all must be true before producing anything)

- [ ] A task file exists in `planning/active/` for this work (LAW L1).
      If not: promote from backlog or create one now (template TASK.md).
- [ ] You restated the task's objective and done-when in your own words in the
      task's Work Log. If your restatement feels off, ask the human first.
- [ ] You read the task's listed context files + the owning subsystem's
      `STATUS.md` + relevant playbook(s) per PROJECT_PROFILE domains.
- [ ] You checked FAILURE-MODES.md for this task type and noted the top 3
      applicable failure modes in the Work Log.
- [ ] Max 3 tasks in `planning/active/`. More = you're multitasking; demote one.

## Work loop (repeat until done-when is met)

1. **Pick the smallest next step** that produces something checkable.
2. **Predict** in the Work Log, one line: what you expect this step to produce.
3. **Do it.**
4. **Check it** against the prediction. Surprised? Understand why BEFORE
   continuing — surprises are the system telling you your model is wrong.
5. **Log it**: timestamped Work Log entry — what/result/evidence path.
   Facts learned that outlive the task → route per MAP.md (research note,
   LESSONS, GLOSSARY), don't bury them in the log.

## While working

- Blocked >30 min on one approach → write down why, try a different angle;
  blocked on 2 distinct angles → switch to P08-DEBUG (if it's a defect) or ask
  the human (if it's ambiguity). Grinding is not a strategy.
- Discover work outside the task's scope → one line in `planning/backlog/`,
  keep moving (LAW L5).
- Discover the task is 3× bigger than thought → stop, split it (P03 step 4),
  tell the human.
- Touching an interface file → P04-Interlock: update the interface doc FIRST,
  list affected subsystems in the change note.

## Done gate

- [ ] Every done-when criterion checked with evidence (run output, test result,
      measurement, screenshot) linked from the task file. Prediction ≠ evidence.
- [ ] Verification recorded per P05 (even a 3-line report). No exceptions —
      "obviously works" is FAILURE-MODE G6.
- [ ] Task file: status → done, moved to `planning/done/`.
- [ ] Subsystem `STATUS.md` updated if subsystem state changed.
- [ ] `knowledge/requirements/REQUIREMENTS.md`: mark any requirement this task
      satisfies with the evidence link (traceability).

## Session-End ritual (LAW L10 — runs even if the task isn't done)

1. `state/NOW.md`: current focus, exact next action ("resume at: ..."), blockers.
   Write the next action so specifically that a different model cold-starts in
   one minute.
2. Session log → `state/sessions/YYYY-MM-DD-<n>.md` (template SESSION-LOG.md).
3. Sweep: new questions → QUESTIONS.md, risks → RISKS.md, lessons → LESSONS.md.
4. 3-line human report: changed / verified-vs-unverified / next.
