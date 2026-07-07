# RIDER — Reasoning-Integrated Directory for Engineering Rigor

**The rider, not the horse.** Any competent AI model dropped into this directory
performs dramatically above its weight class, because the reasoning discipline —
boot sequence, laws, protocols, checklists, state files, verification gates —
lives in the files, not in the model.

## For humans: how to start a new project

1. Copy `rider-master/` → rename to your project name.
2. Dump every file you have (papers, CAD, code, datasheets, notes, images,
   requirements) into `intake/inbox/`. Don't organize anything yourself.
3. Open the folder with any AI agent (Claude Code, Codex, Gemini CLI, Cursor,
   anything) and say: **"Initialize this project."**
   - For chat-only models without file access, use the prompts in
     `kernel/PROMPTS.md` instead.
4. Answer the interview questions the agent asks (P01 forces it to interview you).
5. Work. Every session thereafter: open the folder, say what you want, the entry
   files force the agent to boot correctly.

## For humans: daily commands (say these to any agent)

| Say | What happens |
|---|---|
| "Initialize this project" | P01: interview, classify intake, fill profile, set up env |
| "Boot and give me a status briefing" | Boot sequence + summary of NOW/risks/questions |
| "Plan <thing>" | P03: task decomposition with gates |
| "Work on <task>" | P04: disciplined execution loop |
| "Verify <task>" | P05: evidence-based verification |
| "We need to decide <X>" | P06: ADR / trade-study procedure |
| "Research <topic>" | P07: research synthesis into knowledge/ |
| "Debug <problem>" | P08: hypothesis-driven debugging |
| "Audit the project" | P09: consistency/gap/drift audit |
| "Check my environment" | P11 + `python ops/doctor.py` |
| "End session" | Session-end ritual: logs + NOW.md update |

## Design principles (why this works)

1. **Externalized state.** Models forget; files don't. All working memory lives
   in `state/`. Any model, any day, can resume from `state/NOW.md` in minutes.
2. **Procedure over judgment.** Weak models fail at open-ended judgment but
   follow checklists well. Every hard cognitive act is a numbered protocol.
3. **Gates, not vibes.** Nothing is "done" without evidence. Nothing is built
   without a task. Nothing is decided without an ADR. The gates are the quality.
4. **Metered context.** Protocols tell the model exactly which files to read for
   each job — enough to be right, little enough to not drown.
5. **Loose coupling, shared truth.** Subsystems only touch through
   `integration/interfaces/`. Pause any subsystem; the rest keep moving.
6. **Append-biased memory.** History is moved to `archive/`, never destroyed.
   The project can always explain itself.

## Layout

See `MAP.md`. Kernel internals: `kernel/README.md`.
