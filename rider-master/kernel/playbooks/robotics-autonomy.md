# PLAYBOOK — robotics-autonomy

> Whole-robot integration: perception→planning→actuation stacks, ADAS/AV,
> mobile robots, manipulators. This playbook is about the SYSTEM; each part
> also loads its own playbook.

## Judgment rules
- Define the ODD (Operational Design Domain) first: which surfaces, lighting,
  speeds, obstacles, weather is the robot designed for? Every requirement and
  test derives from it; without it "works" is unfalsifiable.
- Teleop before autonomy: manual control end-to-end proves the whole
  chain (power, comms, actuation, e-stop) before any intelligence is added.
  Autonomy debugging on an unproven base conflates two problem classes.
- The state machine IS the robot: modes (idle/manual/auto/fault/e-stop) and
  their transitions designed and documented before behaviors. Every mode
  answers: what are the actuators doing? what gets you out of this mode?
- Degrade gracefully by design: sensor timeout → defined safe behavior (slow,
  stop, limp home) decided at design time. The default of "keep using stale
  data" is how robots meet walls.
- Sim-to-real is a gradient, not a leap: sim → bench (wheels up) → tethered/
  slow → supervised free run → autonomous. Each step is a V-level gate.
- Log everything from day one: timestamped inputs, state, outputs — the replay
  file is the only witness when a 20-minute run fails once. Storage is cheap;
  un-reproducible field failures are not.

## Gotchas that burn people
- Clock/frame chaos: every sensor in its own time and frame. Centralize:
  one timebase (monotonic, offsets measured), one TF-style frame convention,
  drawn and filed as an interface doc. Half of "sensor fusion bugs" live here.
- E-stop that stops the software but not the motors (or vice versa). E-stop
  must be tested at every hardware change, cut actuation physically, and be
  reachable at every test.
- Battery sag: behavior tuned at 12.6 V misbehaves at 11.2 V — test across
  charge states, monitor voltage as telemetry.
- WiFi/telemetry dies exactly when the robot is far/fast: the onboard behavior
  on comms loss must be safe WITHOUT the link.
- Integration hell from skipped interface docs: perception says y-up-meters,
  planner assumed y-down-pixels. LAW L8 exists for robots most of all.
- Demo-mode drift: the "one small tweak" for the demo that never gets logged
  and haunts the next month.

## Verification specifics
- Scenario-based: each requirement maps to concrete test scenarios in the ODD
  (nominal, boundary, fault-injected: covered sensor, dropped link, low battery).
- V2 = bench/HIL with real sensors on recorded or synthetic scenes;
  V3 = field runs, N≥3 repeats per scenario, logged; report pass RATE not
  best-run (a 1/5 success is 20%, not "works").
- Field session ritual: charged batteries, e-stop check, log recording ON,
  incident notes → verification/evidence/field-YYYY-MM-DD/.

## Environment (feeds P11)
Middleware if any (ROS2 version pinned — distro changes break everything),
sim (Gazebo/Isaac/CARLA/Webots per platform), replay/plot tooling (bag files,
Foxglove/PlotJuggler), battery charging + storage safety notes in env/setup/.

## Init additions (P01)
Ask: ODD in the human's words, platform inventory (chassis, compute, sensors,
actuators + what's proven working), e-stop existence, test space available
(size, surface, permission), competition/road rules that bind, teleop-first
acceptable (push hard if not — explain why it de-risks).
