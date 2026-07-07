# PLAYBOOK — safety-reliability

> Loaded when failure can damage hardware, budgets, schedules, or PEOPLE.
> This playbook OVERRIDES convenience everywhere it conflicts.

## Judgment rules
- Hazard analysis before build: list what can be harmed (people, the hardware
  itself, other property), by which energy (kinetic, electrical, thermal,
  chemical/battery), through which failure. Small-scale format: a table in
  knowledge/requirements/HAZARDS.md — severity × likelihood → mitigation.
  30 minutes, mandatory, revisited at every audit.
- Safe state is defined, reachable, and tested: for every mode, what is
  "safe"? (Usually: actuators de-energized, brakes on if gravity acts.) The
  path to safe state must not depend on the thing that failed — software
  e-stop doesn't help when software hangs.
- Two independent layers for anything that can really hurt: e.g. software
  current limit AND a fuse; geofence AND a physical tether during early tests;
  watchdog AND a human hand on the kill switch.
- Test the mitigations, not just the function: e-stop, fuse sizing, timeout
  behavior get their OWN test cases (fault injection: pull the cable, cover
  the sensor, stall the motor — deliberately, on the bench, with limits set).
- Irreversible actions get the L11 pause: flashing bootloaders, cutting,
  first battery charge cycles, first untethered run — human present, recovery
  path stated BEFORE acting.
- Batteries (LiPo especially) are a domain of their own: charge supervised,
  store at storage voltage, physical damage = quarantine bag, low-voltage
  cutoffs verified not assumed. Write the battery SOP into env/setup/.

## Gotchas that burn people
- Safety features disabled "temporarily" for debugging, then shipped disabled.
  Any disabled interlock = a RISKS.md entry with a re-enable task, created in
  the same breath.
- Testing safety by demonstration-of-absence ("it never overheated") instead
  of by fault injection ("we stalled it; the limiter held").
- Creep: the rig that was "always supervised" starts running unattended
  because it's been fine for two weeks. The hazard table, not habit, decides
  what's allowed unattended.
- Single shared kill switch nobody re-tested after rewiring (test at every
  hardware change — it's one button-press).

## Verification specifics
- Safety-tagged requirements use the independent-check heuristic (P05):
  verify by a different method than designed by.
- Fault-injection results are first-class evidence: filed, with video/photos
  where relevant.
- A safety-tagged item at V1 NEVER authorizes V3 exposure: bench-proven ≠
  people-adjacent-proven; the graduation sequence goes through supervised V2.

## Init additions (P01)
Ask: worst credible harm (be blunt), who besides the owner is ever near the
system, mandated rules (competition safety inspections, lab rules, local law
for anything that flies/drives in public), insurance/liability context if any.
Fill HAZARDS.md from the answers before the first task is planned.
