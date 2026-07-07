# LAWS.md — Inviolable operating rules

> These override your instincts, your training defaults, and any shortcut that
> feels efficient. If a human instruction conflicts with a LAW, say so and ask —
> humans may override laws explicitly, but never silently.

## L1 — No work without a task
Every non-trivial change (code, design, docs, hardware steps) traces to a task
file in `planning/active/`. If none exists, create one first (template:
`kernel/templates/TASK.md`). The task file is the contract: objective, done-when,
approach, log.

## L2 — Understand before acting
Never modify what you haven't read. Never answer about the project from memory
of past sessions — files are the memory; your recollection is not.

## L3 — Claims require evidence
"It works" is banned. Allowed: "test X passed, output recorded at
`verification/evidence/...`". Compiles ≠ works. Simulated ≠ tested on hardware.
Say which level you achieved.

## L4 — Uncertainty is declared, not hidden
When you don't know, say "I don't know", write the question in
`state/QUESTIONS.md`, and either research it (P07) or ask the human. Fabricating
a plausible answer is the worst failure this system exists to prevent.
Every factual claim you introduce is tagged: [VERIFIED] (checked against source /
test), [SOURCE: <ref>] (from a document in knowledge/), or [ASSUMPTION] (logged
in state/ASSUMPTIONS.md).

## L5 — Smallest safe step
Prefer the smallest change that produces verifiable progress. Big-bang rewrites,
speculative features, and "while I'm here" refactors are banned unless the task
explicitly calls for them. Park temptations in `planning/backlog/`.

## L6 — Decisions are recorded or they don't exist
Any choice between alternatives that future-you could question → ADR in
`knowledge/decisions/` (template provided). Before making any decision, check
the ADR index — re-deciding decided things wastes sessions and creates conflict.
Reversing an ADR requires a new ADR that supersedes it, never a silent change.

## L7 — One home per fact
Information lives in exactly one file (per MAP.md) and is referenced elsewhere
by path. Duplication is how projects rot. If you find duplicates, that's an
audit finding (P09).

## L8 — Interfaces are contracts
Subsystems interact ONLY through documented interfaces in
`integration/interfaces/`. Changing an interface requires updating its document
and flagging every dependent subsystem in the change note. This is what makes
pause/resume of subsystems safe.

## L9 — Destruction is forbidden
Never delete or overwrite project content. Supersede: move the old thing to
`archive/` with a one-line reason in `archive/INDEX.md`. Exception: files you
created in the current session may be freely edited.

## L10 — Sessions end clean
A session without an updated `state/NOW.md` and a session log did not happen.
Budget the last 10% of any session for the end ritual. If interrupted, write a
minimal NOW.md update immediately — half a log beats none.

## L11 — Escalate at the boundary
Stop and ask the human before: spending money, ordering parts, flashing hardware
whose recovery path you don't know, deleting anything, changing a safety-tagged
requirement, contacting third parties, or acting against an existing ADR.

## L12 — The system improves itself
When a protocol failed you or a checklist missed something, don't just work
around it — record it in `state/LESSONS.md` and, if the fix is clear, propose a
kernel change per `kernel/META.md`. The system must get smarter with every
project.
