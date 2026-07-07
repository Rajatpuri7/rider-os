# META.md — How the kernel itself evolves

> The kernel (`kernel/`) is the operating system. It changes rarely and
> deliberately. Everything else in the tree changes freely.

## Change rules

1. Kernel changes happen only when driven by a recorded lesson
   (`state/LESSONS.md`) or explicit human request — never as a side effect of
   normal work.
2. Every kernel change is logged in `kernel/CHANGELOG.md`: date, file, what,
   why, which lesson/request drove it.
3. Protocols may gain steps; removing a step requires human approval (steps
   exist because something once went wrong).
4. Never edit the master copy while working inside a project copy. Improvements
   flow: project copy → tested in practice → human ports them back to
   `rider-master/` at project end (see §Harvest).

## Harvest ritual (end of every project)

Run once per project, ~30 minutes, highest-leverage activity in this system:

1. Read `state/LESSONS.md` end to end.
2. For each lesson ask: is this project-specific, or universal?
3. Universal lessons become: a new FAILURE-MODES row, a protocol step, a
   template field, or a playbook item — in the MASTER copy.
4. Log each port in the master's `kernel/CHANGELOG.md`.
5. The master's version bumps in `kernel/CHANGELOG.md` header.

This is how the system compounds: every project makes every future project
smarter, regardless of which model runs it.

## Extension points

- New domain → add `kernel/playbooks/<domain>.md` + a flag in
  PROJECT_PROFILE.yaml's domain list.
- New recurring activity → new `kernel/protocols/P##-NAME.md`, register it in
  BOOT.md's Step-2 table.
- New artifact type → new template in `kernel/templates/` + a MAP.md row for
  where instances live.

## Anti-bloat rule

The kernel competes for model context. Before adding, ask: does this pay rent
on every project? Project-specific guidance belongs in that project's
`knowledge/`, not in the kernel. If a kernel file exceeds ~200 lines, split or
prune it.
