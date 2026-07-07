# PLAYBOOK — computer-vision

> Cameras, image pipelines, detection/tracking/segmentation, calibration,
> classical CV and learned CV at the pipeline level (training → machine-learning playbook).

## Judgment rules
- The camera is the algorithm: exposure, focus, mounting rigidity, and lighting
  determine more performance than any downstream cleverness. Fix optics before
  code. Auto-exposure/auto-white-balance are nondeterminism generators — lock
  them for anything that must be repeatable.
- Calibrate early, store forever: intrinsics (+ extrinsics if multi-sensor)
  are project artifacts → knowledge/reference/ with date + rig photos.
  A moved camera = a new calibration; mount rigidly, then don't touch.
- Build the pipeline as inspectable stages: every stage dumps its intermediate
  image/values on demand. Debugging CV without seeing intermediates is
  astrology.
- Define accuracy operationally BEFORE building: what counts as a hit? at what
  IoU/pixel error? measured on which frames? Otherwise "works" means "worked
  on the three frames I looked at" (G6 with pictures).
- Collect an evaluation set on day one: 50–200 labeled frames from the REAL
  camera in the REAL environment beats any benchmark number.

## Gotchas that burn people
- BGR vs RGB (OpenCV is BGR), row-major vs (x,y) indexing, integer overflow in
  accumulations, uint8 wraparound on arithmetic.
- Coordinate frames: image (y-down!) vs camera vs world; publish the convention
  in an interface doc, with a drawing.
- It worked in the afternoon: sunlight shifted. Test across lighting conditions
  or control the lighting; log illumination with every eval run.
- Rolling shutter + motion = geometry lies (wobble, skew) — matters for
  measurement tasks, choose global shutter or slow down.
- Latency vs throughput confusion: 30 fps ≠ 33 ms latency; pipelines buffer.
  Measure glass-to-decision latency explicitly if control consumes the output.
- USB bandwidth: two cameras on one hub silently drop to lower modes/frames.

## Verification specifics
- V1 = offline on recorded data (record raw video EARLY — replayability is
  gold); V2 = live camera, controlled scene; V3 = target environment, target
  lighting, target motion.
- Metrics per the operational definition, on the eval set, versioned: eval-set
  hash/date + code version in every report (P05 reproducibility).
- Regression check: keep a small "golden frames" set; any pipeline change
  re-runs it.

## Environment (feeds P11)
OpenCV (+ contrib as needed), NumPy, camera SDK/drivers, calibration tooling
(chessboard/ChArUco printed and MEASURED — paper scales lie), storage plan for
video (it's big, decide where it lives, gitignore it).

## Init additions (P01)
Ask: camera(s) exact model + interface, lighting controllable?, targets/
markers allowed (AprilTag/ArUco make many problems trivial — say so), frame
rate + latency the consumer needs, compute budget (Pi? Jetson? laptop?).
