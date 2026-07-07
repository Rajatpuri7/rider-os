# P01 — INITIALIZE (run once, on a fresh master copy)

Goal: transform an empty master + a pile of dropped files into an oriented,
domain-adapted, environment-checked project. Do not skip steps. Do not start
engineering work during initialization.

## Phase A — Survey (read-only)

1. List everything in `intake/inbox/` (names, types, sizes — do not deep-read yet).
2. Skim each document's first page / each code repo's README / each CAD file's
   name. Build a one-line-per-file inventory in `intake/INTAKE-LOG.md`.
3. Draft your best guess of: what the project is, its domains, its maturity
   (idea / partial build / rescue of existing work).

## Phase B — Interview the human (mandatory, batched)

Ask ALL of these in one message. Do not guess answers you could ask for.

1. One sentence: what does success look like?
2. Hard constraints? (deadline, budget, mandated parts/tools, competition or
   course rules, supervisor requirements)
3. Which domains apply? (offer your Phase-A guess from the PROJECT_PROFILE list
   for confirmation)
4. What already exists and what state is it in? (working / broken / unknown)
5. What's the single most urgent thing?
6. Anything failure can damage — hardware, deadlines, people? (sets the
   safety-reliability flag)
7. What tools/environments do you already use for this? (IDE, OS, sims, MCU
   toolchains)

## Phase C — Fill the profile

1. Complete every field of `PROJECT_PROFILE.yaml`. `status: active`.
2. For each true domain flag, skim that playbook now
   (`kernel/playbooks/<domain>.md`) — each playbook's "Init additions" section
   adds domain-specific interview questions and structure. Apply them.

## Phase D — Classify intake

Run `kernel/protocols/P02-INTAKE.md` over everything in the inbox.

## Phase E — Seed the knowledge base

1. `knowledge/requirements/REQUIREMENTS.md`: extract every requirement found in
   intake docs + interview answers. Mark each: source, MUST/SHOULD/COULD,
   verified-by (how we'll prove it, even if rough).
2. `state/QUESTIONS.md`: everything unknown that shapes design. This list being
   long is GOOD — it's the map of ignorance.
3. `state/RISKS.md`: initial register. Prompt yourself with: long-lead parts?
   single points of failure? unproven algorithms? deadline collisions?
   dependency on people/access?
4. `knowledge/GLOSSARY.md`: project-specific terms, acronyms, part nicknames.

## Phase F — Decompose into subsystems

1. Propose 3–8 subsystems (loosely coupled, independently pausable). For each,
   copy `subsystems/_TEMPLATE/` → `subsystems/<name>/` and fill `STATUS.md`.
2. Draft `integration/ARCHITECTURE.md`: block diagram (mermaid), data/power/
   control flows between subsystems.
3. For every arrow between subsystems, create a stub in
   `integration/interfaces/` — even one line ("TBD: protocol between X and Y")
   makes the dependency visible.

## Phase G — Environment

Run `kernel/protocols/P11-ENVIRONMENT.md`. Output: `env/ENVIRONMENT.yaml`
filled, `ops/doctor.py` passing or a setup task created for what's missing.

## Phase H — First plan

1. Fill `planning/ROADMAP.md`: phases, milestones, critical path, riskiest
   assumption + the cheapest experiment to test it (schedule that FIRST).
2. Create the first 2–3 task files in `planning/backlog/`, promote one to
   `planning/active/`.

## Phase I — Initialization report

Write `state/NOW.md` fresh, then give the human:
project understanding (5 lines) / subsystem list / top 5 risks / top 5 open
questions / environment status / proposed first task. Get explicit confirmation
before starting engineering work.
