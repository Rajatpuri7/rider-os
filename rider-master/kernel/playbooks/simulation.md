# PLAYBOOK — simulation

> Physics sims, plant models, SIL/HIL, digital twins, Monte Carlo.

## Judgment rules
- A simulation is a claim generator, not a truth generator: every sim result
  is [ASSUMPTION]-grade until validated against at least one real measurement.
  The validation experiment is part of building the sim, not optional.
- Fidelity is a budget: model ONLY what the question needs. A friction-perfect
  world answers logic questions fine; it answers traction questions falsely.
  Write down what the sim intentionally ignores — that list IS the sim's spec.
- Same interface as reality: sim plugs in behind the SAME interface contract
  (LAW L8) the real sensors/actuators use, so swapping sim↔real is a config
  change, not a refactor. This one decision buys the whole hardware-
  unavailable workflow.
- Determinism by default: fixed seeds, fixed timestep, versioned scenario
  files. A sim you can't replay exactly is a slot machine with graphics.
- Watch the solver: timestep too large = fake instability (or fake stability);
  energy drift, interpenetration, jitter at rest are solver-lying symptoms —
  tune dt/solver before believing any downstream result.

## Gotchas that burn people
- Sim-only success: parameters tuned in sim transplant badly (sim-to-real
  gap); treat sim-tuned values as initial guesses, plan a re-tune on hardware.
- Perfect sensors: real sensors have noise, latency, dropout, bias — inject
  measured (not guessed) noise models or the perception stack gets a free ride
  it must repay on hardware, with interest.
- Time abstraction leaks: sim runs faster/slower than real time; code that
  reads wall clock instead of sim clock works in one and fails in the other.
- Units/gravity/axis conventions differ per simulator (Z-up vs Y-up) —
  check against the project frame convention doc on day one.

## Verification specifics
- The sim itself gets verified: conservation/sanity checks (energy, momentum,
  rest stability), then correlation runs — same input to sim and real plant,
  overlay the traces, quantify the gap, file as EXPERIMENT.
- Results reported WITH the fidelity caveat list attached. "Works in sim
  (frictionless, perfect IMU)" is the honest phrasing.

## Environment (feeds P11)
Simulator + exact version, GPU needs, scenario/world file locations (versioned
with the project), headless-run capability for batch experiments.

## Init additions (P01)
Ask: what questions must the sim answer (sets fidelity budget), what real data
exists for validation, real-time or batch, does sim need to outlive the
project (digital twin) or is it scaffolding.
