# STATUS — <subsystem name>

> The 60-second orientation for anyone (human or model) touching this
> subsystem. Update on every state change and at every session end that
> touched this subsystem (LAW L10).

- **State**: planning | active | paused | blocked | verified | retired
- **Last updated**: YYYY-MM-DD
- **Owner tasks**: <active/backlog task IDs for this subsystem>

## Purpose (2–3 lines)
<What this subsystem does for the system, and what it explicitly does NOT do.>

## Current truth (keep brutally honest)
- What works, at which V-level: <e.g. "driver reads sensor at 100 Hz — V1 only, bench">
- What is built but unverified: …
- What doesn't exist yet: …

## Interfaces (contracts this subsystem lives by)
| Interface | With | Doc |
|---|---|---|
| | | `integration/interfaces/IF-…` |

## Interface-change inbox (cleared on resume — P10)
<Lines added by OTHER subsystems when they change a shared contract.>

## Resume point (the pause ritual's output — P10)
- Next action, precisely: <…>
- Loose ends: <…>
- Gotchas: <fragile connector, half-migrated config, …>

## Local decisions & lessons index
<Links to ADRs and LESSONS entries that shaped this subsystem.>
