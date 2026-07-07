# MAP.md — Where everything lives and why

> Read this when you need to know where a thing goes or where to find it.
> Rule of thumb: every artifact has exactly ONE home. If two places seem right,
> this file decides. If this file doesn't decide, add the decision here.

## Top-level layout

| Path | Purpose | Writable by AI? |
|---|---|---|
| `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` | Agent entry points (identical) | Only via kernel-change protocol |
| `PROJECT_PROFILE.yaml` | Machine-readable project identity, domains, constraints | Yes (P01, P11) |
| `MAP.md` | This file | Yes (append) |
| `kernel/` | The operating system: laws, protocols, templates, playbooks | Only via META.md rules |
| `intake/` | Raw dropped files → classified into the tree | Yes |
| `knowledge/` | Curated, trusted project knowledge | Yes (curated only) |
| `state/` | Live cognitive state: NOW, questions, risks, session logs | Yes (every session) |
| `planning/` | Roadmap, backlog, active tasks, done tasks | Yes |
| `subsystems/` | One folder per loosely-coupled subsystem | Yes |
| `integration/` | Cross-subsystem interfaces and system-level architecture | Yes |
| `verification/` | Test plans, reports, raw evidence | Yes (append-mostly) |
| `delivery/` | Releases, final docs, demos | Yes |
| `archive/` | Dead ends, superseded work — moved, never deleted | Move-in only |
| `env/` | Environment manifest + setup scripts | Yes |
| `ops/` | Maintenance scripts (doctor, validate, bundle) | Yes |

## Placement decision table

| You have... | It goes in... |
|---|---|
| A file the human just gave you, unclassified | `intake/inbox/` then run P02-INTAKE |
| A requirement (thing the system MUST do/be) | `knowledge/requirements/REQUIREMENTS.md` |
| A decision with alternatives considered | `knowledge/decisions/` as an ADR |
| A trade study comparing options | `knowledge/decisions/` as TRADE-STUDY |
| Summarized findings from papers/datasheets/web | `knowledge/research/` |
| Original papers, datasheets, manuals (verbatim) | `knowledge/reference/` |
| Glossary term, project-specific jargon | `knowledge/GLOSSARY.md` |
| An open question blocking or shaping work | `state/QUESTIONS.md` |
| A risk (something that could go wrong later) | `state/RISKS.md` |
| A lesson learned / mistake to not repeat | `state/LESSONS.md` |
| What you did this session | `state/sessions/` log + `state/NOW.md` update |
| Work not started yet | `planning/backlog/` |
| Work in progress (max 3 at once) | `planning/active/` |
| Finished, verified work records | `planning/done/` |
| Code/design/tests for one subsystem | `subsystems/<name>/` |
| An interface between two subsystems | `integration/interfaces/` — NEVER inside a subsystem |
| System-level architecture | `integration/ARCHITECTURE.md` |
| A test plan (before testing) | `verification/test-plans/` |
| A test report (after testing) | `verification/test-reports/` |
| Raw logs, screenshots, scope captures, videos | `verification/evidence/` |
| Superseded/abandoned work | `archive/` with a one-line reason in `archive/INDEX.md` |

## Naming conventions

- Dates: `YYYY-MM-DD`. Session logs: `YYYY-MM-DD-<n>.md`.
- ADRs: `ADR-####-short-slug.md`, numbered sequentially, never renumbered.
- Tasks: `T####-short-slug.md`, numbered sequentially, never reused.
- Requirements: `R-<SUBSYS>-###` inline IDs inside REQUIREMENTS.md.
- Subsystems: lowercase-kebab-case folder names.
- Everything else: lowercase-kebab-case, descriptive, no spaces.
