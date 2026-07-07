# PLAYBOOK — embedded-firmware

> MCUs, RTOS, bare metal, Arduino-class boards, drivers, comms buses.

## Judgment rules
- Read the datasheet AND the errata sheet. The errata is where the truth lives;
  silicon bugs are real and vendor forums know them.
- Blocking delays in loops are debt from day one; structure around a
  non-blocking main loop / scheduler / RTOS tasks early — retrofitting is 10×.
- Everything shared with an ISR: volatile + atomic access story, ISRs do
  minimum work (set flag, copy byte, leave).
- Watchdog on by default in anything that runs unattended. Brownout detection
  configured consciously, not left at default.
- Budget RAM/flash/CPU from the start; check headroom at every milestone —
  the last 10% of features meeting the last 10% of memory is a classic death.
- Power-on state is a design decision: what do pins do during boot? (Motors
  twitching at reset has broken real robots.)

## Gotchas that burn people
- 5V vs 3.3V logic mismatch — check EVERY pin pair, "it worked for a while" is
  the classic symptom of slow damage.
- Shared ground missing between boards → ghost behavior, "possessed" sensors.
- Serial: TX→RX crossed (not TX→TX), baud mismatch, missing common ground —
  the holy trinity of "no data".
- I2C: pull-ups (missing, or doubled by every breakout board on the bus),
  address conflicts, bus capacitance on long wires.
- printf/Serial.print in ISRs or tight loops: changes timing, hides/creates bugs.
- Float printf disabled by default on some toolchains (prints blank — not a bug
  in your math).
- Stack overflow on small MCUs presents as random corruption, not a clean crash.
- Flashing over a UART the application also uses: boot-mode pin states matter.

## Debug order for "it doesn't work" (extends P08 hardware addendum)
1. Power rails under load, measured with a meter — not assumed.
2. Grounds common? Connectors seated? (Reseat anyway.)
3. Is the code even running? (Heartbeat LED first, always.)
4. Is the peripheral alive? (I2C scanner / loopback / known-good example sketch.)
5. Only THEN suspect your logic.

## Verification specifics
- V1 = module on bench with fake inputs; V2 = integrated on the real bus/rig;
  V3 = on the vehicle/device, battery-powered (USB power hides brownout bugs!).
- Test power-cycle recovery and disconnect-mid-operation explicitly.
- Log timing headroom (loop time, ISR duration), not just correctness.

## Environment (feeds P11)
Toolchain (per-MCU), flasher/debugger drivers, serial terminal, build system
(PlatformIO/CMake/IDF/arduino-cli), and a documented "flash + see output"
smoke procedure in env/setup/.

## Init additions (P01)
Ask: exact board(s) + revisions, voltage domains present, debugger available
(or serial-only?), can bricking occur and what's the recovery path (LAW L11),
battery vs bench power, which buses are already committed.
