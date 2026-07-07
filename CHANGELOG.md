# Changelog

All notable changes to this repository. The kernel keeps its own authoritative
log in [rider-master/kernel/CHANGELOG.md](rider-master/kernel/CHANGELOG.md);
this file tracks releases of the repo as a whole.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: SemVer,
matching the kernel version.

## [1.1.0] — 2026-07-08

### Added
- Initial public release.
- `rider-master/` template: kernel (BOOT, 12 LAWS, FAILURE-MODES, PROMPTS, META,
  11 protocols P01–P11, 11 templates, 11 domain playbooks), full state tree,
  and stdlib-only ops tooling (`validate.py`, `doctor.py`, `bundle.py`).
- Intent router in BOOT.md Step 2 — users describe work in plain language; the
  model classifies and routes it.
- Repository docs: README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, issue/PR
  templates, CI validation workflow.
