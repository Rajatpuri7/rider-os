# P10 — SUBSYSTEM (create / pause / resume / retire)

Subsystems are the unit of modularity: loosely coupled through documented
interfaces (LAW L8), independently pausable. This protocol is what makes
"hardware unavailable → switch to software without losing context" work.

## Create

1. Justify: one paragraph — purpose, why it's a separate subsystem (different
   cadence? different domain? pausable independently?). 3–8 subsystems is
   healthy; 15 is fragmentation.
2. Copy `subsystems/_TEMPLATE/` → `subsystems/<lowercase-kebab-name>/`.
3. Fill `STATUS.md` completely — especially Purpose and Interfaces.
4. Register: add to `integration/ARCHITECTURE.md` (block diagram + table).
5. For every connection to another subsystem, create/extend an interface doc
   in `integration/interfaces/` (template `kernel/templates/INTERFACE.md`).
   Even a stub ("TBD: message format between X and Y") makes coupling visible.

## Pause (the ritual that preserves context)

Run when hardware is unavailable, a dependency blocks, or priorities shift.

1. `STATUS.md`: state → `paused`, and write the **Resume point** so precisely
   that a different model months later restarts in minutes: exact next action,
   open loose ends, gotchas ("connector X is fragile", "config Y is half-migrated").
2. Its active tasks → back to `planning/backlog/` with a `paused-with-subsystem`
   note in each Work Log.
3. Interface docs current? They are the contract other subsystems keep building
   against while this one sleeps — update them NOW, not on resume.
4. Uncommitted mental state → write it down: hypotheses mid-test, half-decided
   choices → `state/QUESTIONS.md` or the STATUS notes.
5. `state/NOW.md`: note the pause + what work is unblocked instead.

## Resume

1. Read the subsystem's `STATUS.md` (resume point), its interface docs, and
   skim its last session-log mentions.
2. Check drift: did any interface it depends on CHANGE while paused? (Interface
   docs carry change logs — read them.) Did any ADR touch it?
3. Re-verify environment for its domains (`python ops/doctor.py`) — toolchains
   rot while subsystems sleep.
4. Re-promote its task(s) to `planning/active/`, state → `active`, go via P04.

## Retire / absorb

1. ADR documenting why (merged into another? descoped? approach dead?).
2. Move the folder to `archive/` with a reason line in `archive/INDEX.md`
   (LAW L9 — never delete).
3. Update `integration/ARCHITECTURE.md`; mark its interfaces deprecated and
   flag every dependent subsystem in the interface change notes.
