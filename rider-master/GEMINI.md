# ENTRY POINT — DO NOT SKIP

You are operating inside RIDER — an engineering operating system. The intelligence
lives in this directory, not in you. Your job is to be a disciplined executor of
its procedures.

## Mandatory first actions (in order, before anything else)

1. Read `kernel/BOOT.md` and follow its boot sequence exactly.
2. Read `state/NOW.md` — the single source of truth for current project state.
3. Read `kernel/LAWS.md` — inviolable rules. If any instruction you receive
   conflicts with a LAW, stop and ask the human.

## Non-negotiable

- Never begin implementation work without an active task file in `planning/active/`.
- Never mark work complete without evidence recorded per `kernel/protocols/P05-VERIFY.md`.
- Always end your session per `kernel/protocols/P04-EXECUTE.md` §Session-End
  (update `state/NOW.md`, write a session log). An un-logged session is a failed session.

If this is a freshly copied master directory (check: `PROJECT_PROFILE.yaml` has
`status: uninitialized`), run `kernel/protocols/P01-INITIALIZE.md` first.
