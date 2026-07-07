# P11 — ENVIRONMENT (toolchain determination, check, setup)

Goal: no session ever dies on "tool not installed / wrong version /
works-on-my-machine". The manifest `env/ENVIRONMENT.yaml` is the single source
of truth for what this project needs; `ops/doctor.py` checks it mechanically.

## Step 1 — Derive what's needed (don't guess from vibes)

Collect requirements from three sources:
1. **Domains**: every `true` flag in `PROJECT_PROFILE.yaml` → that playbook's
   "Environment" section lists its typical toolchain.
2. **Intake artifacts**: build/config files found in the project declare needs —
   `requirements.txt`/`pyproject.toml` (Python deps), `platformio.ini`/
   `CMakeLists.txt`/Makefiles (embedded toolchains), `package.json` (Node),
   `*.slx` (MATLAB/Simulink + toolboxes), `*.step/*.f3d` (CAD seats),
   Dockerfiles, `.ino` (Arduino cores/libraries).
3. **The human**: IDE of choice, OS, board/debugger drivers, license servers,
   simulators, MCP servers / agent tooling they use.

## Step 2 — Record in the manifest

Fill `env/ENVIRONMENT.yaml` (schema documented in the file header). Every entry
carries: why it's needed, how to CHECK it (a command), min version if it
matters, and install commands per OS. Entries without a check command go under
the manual sections (IDE extensions, MCP servers) — doctor lists them as
human-verify reminders.

## Step 3 — Check

Run `python ops/doctor.py`. It reports PASS / WRONG-VERSION / MISSING per tool
and prints the install command for this machine's OS. Exit code non-zero =
required items missing.

## Step 4 — Install (with consent)

- User-level installs (pip packages, pio platforms, VS Code extensions):
  proceed, log what was installed in the session log.
- System-level installs, drivers, license-touching, or anything sudo/admin:
  present the exact commands to the human first (LAW L11 spirit).
- Can't install now (no admin rights, license pending, big download)? Create a
  setup task in `planning/backlog/` and record the blocker in `state/NOW.md` —
  then find work that doesn't need it (that's what subsystem modularity is for).

## Step 5 — Capture the weird stuff

Anything a fresh machine would trip over goes in `env/setup/` as a note:
board driver quirks, udev rules, PATH tweaks, license server addresses, "you
must run X once before Y works", pinned versions and WHY they're pinned.
The test: could the human rebuild the dev machine from `env/` alone?

## Re-run triggers

New domain flag turned on · new subsystem with new tech · machine change ·
any "works here, fails there" bug (that's an environment diff until proven
otherwise) · resuming a subsystem after a pause (P10).
