# P03 — PLAN (from goal to executable tasks)

Use for: initial roadmapping, phase planning, and decomposing any goal bigger
than one task.

## Steps

1. **State the goal** in one sentence with a measurable end condition. If you
   can't, the goal isn't understood — interview the human first.
2. **Check reality**: read `state/NOW.md`, `state/RISKS.md`, relevant
   `subsystems/*/STATUS.md`, and PROJECT_PROFILE constraints. A plan that
   ignores current state is fiction.
3. **Find the riskiest assumption.** Ask: "what, if false, kills this plan?"
   Design the cheapest possible experiment to test it. That experiment is
   task #1. (Fail fast beats plan pretty.)
4. **Decompose** into tasks where each:
   - has one deliverable and a binary done-when,
   - fits in roughly one working session,
   - names its dependencies (other tasks, parts arriving, human input),
   - names its subsystem and domain(s).
   Near-term: fine-grained. Beyond ~2 weeks: coarse milestones only — detail
   them when they get close (planning far detail is waste, LAW L5).
5. **Mark the critical path.** Which chain of dependencies sets the end date?
   Long-lead items (part orders, access to hardware/labs, approvals) go earliest.
6. **Parallel-work map.** For each task note what it's blocked by. Ensure at
   any moment there exist runnable tasks from ≥2 different subsystems — this is
   what lets work continue when hardware is unavailable.
7. **Write it down**:
   - `planning/ROADMAP.md` — phases, milestones, critical path (update, don't append-forever).
   - One task file per near-term task in `planning/backlog/` (template:
     `kernel/templates/TASK.md`).
8. **Sanity gate** before presenting: Does every MUST requirement trace to at
   least one task or milestone? Does any task violate a constraint or ADR?
   Is the riskiest assumption tested early? Fix, then present to the human.

## Re-planning trigger

Re-run this protocol (not ad-hoc patching) when: a milestone slips >20%, a
riskiest-assumption experiment fails, a constraint changes, or an audit (P09)
finds plan/reality divergence.
