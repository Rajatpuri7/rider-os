# PLAYBOOK — control-systems

> Feedback control, PID, state estimation, motion control, stability.

## Judgment rules
- You cannot control what you cannot measure: sensor quality, latency, and
  sample rate bound achievable performance BEFORE any tuning cleverness.
  Characterize the sensor first (noise floor, drift, latency) — it's a
  half-session experiment that saves weeks.
- Get the plant model even roughly: a step-response test tells you gain,
  delay, and time constant — tune against THAT, not against vibes.
- Units and signs first: half of all "unstable controller" reports are a sign
  flip or degrees-vs-radians. Write the sign convention in the interface doc.
- Timing is part of the controller: fixed sample rate, measured (not assumed)
  loop time, dt from a monotonic clock. Jittery dt = mystery oscillation.
- Saturation is where real controllers live: anti-windup on any integrator
  whose actuator can saturate (it can). Slew-rate limits on outputs that can
  break things.
- Start conservative: P-only, low gain, add I for steady-state error, D (with
  filtering — raw D amplifies noise) only if the response demands it.

## Gotchas that burn people
- Integrator windup during startup/e-stop → violent lurch on resume. Reset/
  clamp integrators on mode transitions.
- Derivative-on-error kicks on setpoint steps → derivative-on-measurement.
- Tuning at one operating point: gains great at low speed oscillate at high
  speed (plant is nonlinear). Test across the envelope.
- Encoder rollover / angle wrap (±180°) discontinuities feeding the error term.
- Filtering added for "noise" adds phase lag → instability. Filter cutoffs are
  part of the loop design, not decoration.
- Testing a new controller at full authority: use gain scheduling of COURAGE —
  output clamped to 20% until behavior is proven (safety-reliability overlap).

## Verification specifics
- V1 = simulation against the identified plant model (step, disturbance,
  saturation cases). V2 = on hardware, low authority, hand-on-kill-switch.
  V3 = full envelope. Skipping V1 when a model exists is negligence.
- Evidence = logged time-series (setpoint, measurement, output) plotted;
  report rise time / overshoot / steady-state error vs the requirement numbers.
- Repeat-run rule: same step test 3×; divergent traces = investigate before tuning further.

## Environment (feeds P11)
Plotting/analysis stack (Python+matplotlib/Jupyter or MATLAB), simulation tool
if modeled, high-rate logging path (serial budget: log binary or decimate —
printf at 1 kHz lies about timing).

## Init additions (P01)
Ask: what's actuated, what can it damage at full authority (kill switch?),
required performance numbers (rise/settle/overshoot — get NUMBERS into
requirements), sensor+actuator inventory with rates, is a plant model feasible.
