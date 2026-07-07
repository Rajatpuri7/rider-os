# BOOT.md — Session boot sequence

> Run this at the start of EVERY session, before doing anything the human asked.
> Total cost: ~2 minutes of reading. Skipping boot is the #1 cause of bad work.

## Step 0 — Identify session type

- Fresh master copy (`PROJECT_PROFILE.yaml` → `status: uninitialized`)?
  → STOP. Run `kernel/protocols/P01-INITIALIZE.md`. Do nothing else.
- Otherwise continue.

## Step 1 — Load minimal state (ALWAYS, in this order)

1. `PROJECT_PROFILE.yaml` — what project this is, which domains, hard constraints.
2. `state/NOW.md` — current focus, active tasks, blockers, next actions.
3. `kernel/LAWS.md` — the rules you operate under.

## Step 2 — ROUTE the request (the human never names a protocol — you do)

The human describes what they want in plain language ("build X", "design a
PCB", "analyze this paper", "write docs", "why is this broken?"). YOU classify
the request against the table below and load only that row. Routing rules:

- **Composite requests** ("build me X" from scratch) are chains, not one row:
  route P03-PLAN → P04-EXECUTE → P05-VERIFY, one protocol at a time, in order.
- **Multiple intents** in one message: handle intake (P02) and decisions (P06)
  before execution — they change what execution should do.
- **No row fits**: it's either a question (answer from `state/` + `knowledge/`,
  no protocol needed) or unplanned work (route to P03-PLAN — LAW L1: no work
  without a task).
- Say your route in the ORIENTATION block (Step 3). If the human explicitly
  names a different protocol, theirs wins.

| The human wants... | Additionally read... |
|---|---|
| Status briefing | `state/RISKS.md`, `state/QUESTIONS.md`, `planning/ROADMAP.md` |
| To plan something | `planning/ROADMAP.md`, relevant `subsystems/*/STATUS.md`, `kernel/protocols/P03-PLAN.md` |
| To build/code/execute | The active task file in `planning/active/`, that subsystem's `STATUS.md` + `design/`, `kernel/protocols/P04-EXECUTE.md`, playbooks for the task's domains |
| To verify/test | The task file, `verification/test-plans/` for it, `kernel/protocols/P05-VERIFY.md` |
| To decide something | `knowledge/decisions/INDEX.md` (check it isn't already decided!), `kernel/protocols/P06-DECIDE.md` |
| To research | `state/QUESTIONS.md`, `knowledge/research/INDEX.md`, `kernel/protocols/P07-RESEARCH.md` |
| To debug | `kernel/protocols/P08-DEBUG.md`, `state/LESSONS.md` (was this seen before?) |
| To audit / clean up | `kernel/protocols/P09-AUDIT.md` |
| New files were dropped | `kernel/protocols/P02-INTAKE.md` |
| Start/pause/resume/retire a subsystem | `kernel/protocols/P10-SUBSYSTEM.md`, that subsystem's `STATUS.md` |
| Environment issues | `kernel/protocols/P11-ENVIRONMENT.md`, `env/ENVIRONMENT.yaml` |

Do NOT read the whole tree. Metered context is a feature: read what the table
says, follow links from there only when a file explicitly points you onward.

## Step 3 — Orient before acting (say this out loud to the human)

Produce a 5-line orientation before touching anything:

```
ORIENTATION
Project: <name> — <one_liner>
Now:     <current focus from NOW.md>
Asked:   <what the human wants this session, in your own words>
Protocol:<which P## applies>
Concerns:<anything in NOW/RISKS/QUESTIONS that collides with the request, or "none">
```

If the request conflicts with a LAW, a constraint in PROJECT_PROFILE.yaml, or an
existing decision in `knowledge/decisions/`, raise it NOW, not after doing the work.

## Step 4 — Check the failure-mode list for your task type

Open `kernel/FAILURE-MODES.md`, find the section matching your task type, and
keep its countermeasures in mind. This is your pre-flight checklist.

## Step 5 — Work

Follow the protocol. When in doubt at any point: `MAP.md` for "where does this
go", `LAWS.md` for "am I allowed", the protocol for "what next".

## Session end (never skip — see P04 §Session-End)

1. Update `state/NOW.md` (focus, next actions, blockers).
2. Write `state/sessions/YYYY-MM-DD-<n>.md` from the SESSION-LOG template.
3. Move finished task files `planning/active/` → `planning/done/`.
4. New questions → `state/QUESTIONS.md`; new risks → `state/RISKS.md`;
   lessons → `state/LESSONS.md`.
5. Tell the human, in 3 lines: what changed, what's verified vs unverified,
   what's next.
