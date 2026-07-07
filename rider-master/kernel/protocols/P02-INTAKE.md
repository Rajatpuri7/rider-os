# P02 — INTAKE (classify dropped files)

Run whenever `intake/inbox/` is non-empty. Raw human-dropped files become
classified, indexed, and summarized project knowledge.

## Per file, in order

1. **Identify**: what is it? (paper / datasheet / requirements doc / code /
   CAD / dataset / image / notes / unknown)
2. **Log** one row in `intake/INTAKE-LOG.md`:
   `| date | filename | type | one-line summary | destination | actions spawned |`
3. **Route the original** (move, don't copy — LAW L7):
   - Papers, datasheets, manuals, standards → `knowledge/reference/`
     (rename to `<type>-<subject>-<year>.<ext>`, e.g. `datasheet-bno055-2021.pdf`)
   - Existing code → `subsystems/<name>/src/` if it maps to one subsystem,
     else `intake/processed/<repo-name>/` until decomposition is decided
   - CAD/mechanical → the owning subsystem's `design/`
   - Datasets → the owning subsystem's `test/data/` or `intake/processed/` if unowned
   - Notes/requirements from the human → mine them (step 4), then archive the
     original in `intake/processed/`
   - Media (photos of hardware, whiteboards) → `knowledge/reference/media/`
     with a caption line in the INTAKE-LOG
4. **Mine it** — this is the step that builds understanding, don't skip:
   - Requirements found → `knowledge/requirements/REQUIREMENTS.md` (with source)
   - Facts worth keeping (specs, limits, pinouts, formulas) → a research note
     in `knowledge/research/` citing the reference file + page
   - Questions raised → `state/QUESTIONS.md`
   - Risks implied → `state/RISKS.md`
   - New jargon → `knowledge/GLOSSARY.md`
5. **Conflict check**: does anything in this file contradict existing
   requirements, ADRs, or research notes? If yes, DO NOT silently pick one —
   log the conflict in `state/QUESTIONS.md` and flag it to the human.

## Special cases

- **Unreadable/ambiguous file**: leave in inbox, add INTAKE-LOG row with
  `destination: BLOCKED — <why>`, ask the human.
- **Huge file** (long PDF, big codebase): route it, write a skim-level summary,
  and create a backlog task "Deep-read <file>" instead of stalling intake.
- **Duplicate of existing content**: archive it, note which file supersedes it.

## Exit criteria

Inbox empty (or only BLOCKED items awaiting the human), INTAKE-LOG complete,
all mined items filed. Report to human: N files processed, M requirements
extracted, K questions raised, conflicts found.
