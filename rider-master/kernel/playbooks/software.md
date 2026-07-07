# PLAYBOOK — software

> Loaded when PROJECT_PROFILE `domains.software: true` and the task touches code.

## Judgment rules
- Boring beats clever: pick the stdlib/most-used library; novelty needs an ADR.
- Make it work → make it right → make it fast, with evidence gates between.
  Optimizing unprofiled code is FAILURE-MODE material — profile first, always.
- Errors are part of the interface: define failure behavior (raise? retry?
  degrade?) at design time, not when the first exception hits.
- State is the enemy of debuggability: prefer pure functions, explicit inputs,
  dependency injection over globals and singletons.
- Delete-friendly code > extensible code: small modules with one reason to
  change; abstractions only after the 2nd–3rd concrete use (rule of three).
- Every external input is hostile until validated (files, serial, network, user).

## Gotchas that burn people
- Off-by-one at boundaries: empty list, single element, exactly-full buffer.
- Time: timezones, monotonic vs wall clock (NEVER wall clock for durations),
  DST, leap seconds if you log across midnight.
- Floating point: never `==`; accumulate error in long sums; -0.0 exists.
- Unicode/encoding at every I/O boundary — declare encodings explicitly.
- Concurrency: shared mutable state needs a documented ownership story.
  "It's probably atomic" is how heisenbugs are born.
- Paths: use pathlib/os.path, never string concat; spaces and non-ASCII happen.

## Minimum quality bar (any language)
- Version control from minute one; commit at every green state; messages say WHY.
- Reproducible env: lockfile / pinned requirements / container — a build that
  needs "the right machine" is broken (P11).
- Tests: every bug fix gets the test that would have caught it. New code:
  happy path + edge + failure path minimum.
- Lint/format on, config committed — zero style debates ever again.

## Verification specifics (extends P05)
- V1 = unit tests green in CI-like conditions (fresh checkout, not your dirty tree).
- V2 = integration against real neighbors (real DB, real serial device, real FS).
- Repeat-run rule: run twice; flaky-once = failing (log it, don't shrug it).

## Environment (feeds P11)
Runtime + version manager, package manager with lockfile, linter/formatter,
test runner, debugger, git. Language-specifics recorded in env/ENVIRONMENT.yaml.

## Init additions (P01 Phase C)
Ask the human: target runtime/OS, language constraints, existing codebase to
inherit (state? tests? docs?), deployment target, CI availability.
