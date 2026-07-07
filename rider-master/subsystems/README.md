# subsystems/ — units of pausable work

One folder per loosely-coupled subsystem (3–8 is healthy). Create/pause/
resume/retire ONLY via `kernel/protocols/P10-SUBSYSTEM.md` — the pause ritual
is what lets you drop hardware work today and resume in a month without
archaeology.

Each subsystem folder (copied from `_TEMPLATE/`):

| Path | Holds |
|---|---|
| `STATUS.md` | State, current truth, resume point — the 60-second orientation |
| `design/` | CAD, schematics, design docs, calculations for THIS subsystem |
| `src/` | Code owned by this subsystem |
| `test/` | Subsystem-local tests + test data |
| `docs/` | Deep documentation too detailed for STATUS.md |

Rules of the land:
- Talk to other subsystems only through `integration/interfaces/` (LAW L8).
- Facts that outlive the subsystem (specs, lessons, decisions) go to the
  shared knowledge tree per MAP.md — subsystem folders are not knowledge silos.
