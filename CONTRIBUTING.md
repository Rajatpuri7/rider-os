# Contributing to RIDER

Thanks for wanting to make the system smarter. RIDER's core principle applies to
itself: **every kernel change must be driven by a recorded lesson, never by
speculation** (see [kernel/META.md](rider-master/kernel/META.md)). "This might be
useful" is not a lesson; "I watched a model do X and this step prevented it" is.

## What we want most

1. **Failure modes + countermeasures** — you watched an AI model ruin work in a
   reproducible way, and you have a countermeasure that works. This becomes a row
   in `kernel/FAILURE-MODES.md`. The highest-value PR type by far.
2. **Domain playbooks** — you work in a domain we don't cover (web backend, data
   engineering, biotech, …). One file: `kernel/playbooks/<domain>.md`, following
   the structure of the existing eleven.
3. **Protocol hardening** — a step that was ambiguous to a real model, made
   precise. Include which model tripped and how.
4. **Bug fixes in `ops/`** — the scripts are stdlib-only and cross-platform;
   keep them that way.

## What we'll decline

- Speculative features ("later can scaffold for itself")
- New dependencies for the ops scripts
- Kernel files growing past ~200 lines (the kernel competes for model context —
  see the anti-bloat rule in META.md)
- Restructuring the tree without a lesson demonstrating the current layout fails

## How to submit

1. Fork, branch from `main`.
2. Make the change. For kernel changes, add a row to
   `rider-master/kernel/CHANGELOG.md` naming the lesson that drove it.
3. Run the validator — it must pass: `python rider-master/ops/validate.py`
4. Open a PR using the template. CI runs the same validator on Linux and Windows.

## Versioning

The kernel uses SemVer (`kernel/CHANGELOG.md` holds the version):
- **Major** — breaking layout/protocol changes (models booted on old copies would misbehave)
- **Minor** — new protocols, playbooks, templates, or router capabilities
- **Patch** — wording fixes, script bug fixes

Releases are tagged `v<version>` and ship a zip of `rider-master/`.

## Questions

Open a [Discussion](../../discussions) rather than an issue — issues are for
defects and concrete proposals.
