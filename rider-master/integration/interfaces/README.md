# interfaces/ — the contracts between subsystems

One file per interface, template `kernel/templates/INTERFACE.md`, named
`IF-<slug>.md`. Interfaces live HERE and only here — never inside a subsystem
(MAP.md) — because they are jointly owned.

The change process (in each doc's footer) is what makes pausing subsystems
safe: paused subsystems get changes flagged into their STATUS.md inbox and
reconcile on resume (P10).
