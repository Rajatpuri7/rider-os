# delivery/ — what leaves the project

| Path | Holds |
|---|---|
| `releases/` | Versioned, shippable snapshots (firmware images, installers, submitted PDFs) with a RELEASE-NOTES.md each: what's in it, built from which state, verified at which V-level |
| `docs/` | Outward-facing documents: reports, thesis chapters, manuals, presentations — written as-you-go (research playbook), not at the deadline |
| `demos/` | Demo scripts/checklists and recordings. A demo has a WRITTEN runbook: setup steps, reset-between-runs procedure, known-fragile points — demos fail on logistics more than on engineering |

Release rule: a release is cut FROM verified state, and its notes say exactly
what was and wasn't verified (L3 applies to shipping too).
