# PLAYBOOK — electronics

> Circuits, PCBs, wiring harnesses, power distribution, sensors/actuators
> at the electrical level.

## Judgment rules
- Power budget first: worst-case current per rail, with 30%+ margin, written
  down BEFORE choosing regulators/batteries. Motors: stall current, not rated.
- Every rail that can hurt something gets protection: fuse/polyfuse, reverse
  polarity protection, TVS where cables leave the board.
- Connectors are the #1 field failure: strain relief, keyed/polarized parts,
  label both ends of every cable the day you make it.
- Separate noisy (motors, servos) and quiet (analog, radio) power domains;
  join grounds at one point. Decoupling caps at every IC, physically close.
- Heat: linear regulators dropping >2–3V at real current need thermal math,
  not vibes.

## Gotchas that burn people
- Servo/motor transients browning out the MCU sharing the rail (symptom:
  "random resets when it moves") — bulk capacitance + separate rails.
- Breadboards: unreliable above tens of mA and any real vibration; contact
  resistance creates fake sensor noise. Solder before concluding "noisy sensor".
- USB power: current-limited and sag-prone — verify on battery too.
- ADC readings drift: reference voltage isn't what you assumed; measure Vref.
- Ground loops via USB + external supply simultaneously connected.
- "It smoked once but works now" — it is damaged; replace it (LESSONS.md it).

## Pre-power checklist (every first power-up, no exceptions)
1. Visual: solder bridges, reversed polarized parts, correct IC orientation.
2. Meter: continuity rails-to-ground (should NOT beep), rail-to-rail shorts.
3. Current-limited bench supply at expected-draw + 20%, watch the meter as
   you power up. No bench supply → smallest fuse you have.
4. Rails at correct voltage BEFORE inserting expensive parts (socket them
   or connectorize them where possible).

## Verification specifics
- Evidence = measurements: photos of meter/scope with the test point named,
  filed per P05. "Looks right" is not a measurement.
- V2 includes: under real load, with motors actually running (EMI now exists).
- Thermal check at sustained load for anything passing >0.5 A or dropping >2 V.

## Environment (feeds P11)
Multimeter (minimum), current-limited supply (strongly urged — say so to the
human if absent), soldering setup; EDA tool (KiCad default) if boards are made;
scope/logic analyzer for bus-level debugging (note as gap if absent).

## Init additions (P01)
Ask: voltage domains and battery chemistry, total current ceiling, what
hardware is irreplaceable/long-lead (→ RISKS), is there a kill switch /
current limit on the bench, fusing present?
