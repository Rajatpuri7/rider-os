# PLAYBOOK — mechanical-cad

> CAD design, 3D printing, machining, chassis/mounts/enclosures, fasteners.

## Judgment rules
- Design around what exists: measure the REAL parts (calipers, not datasheet
  renders) before modeling mounts for them. Vendor STEP files lie by ±0.5 mm.
- Tolerances are the design: nothing mates at nominal. Decide fit class
  (clearance/transition/press) per joint, explicitly. 3D printing: holes come
  out ~0.2–0.4 mm undersize; test-print a tolerance coupon per printer+material
  before committing a big part.
- Design for the tool: FDM likes flat bases, hates unsupported overhangs >45°,
  is weak across layer lines (orient load along layers). Machining likes
  reachable features. Lasercut likes 2D + tabs.
- Fasteners: standardize on 2–3 sizes project-wide; heat-set inserts beat
  threading plastic; nyloc or threadlocker anywhere with vibration (a robot IS
  vibration).
- Cable routing and hand access are design features: if a connector can't be
  reached, the design isn't done. Model the cables' bend radius space.
- Mass and CG budgets from day one for anything that moves.

## Gotchas that burn people
- Printing a 9-hour part before checking hole positions against the real PCB
  — paper-print the face 1:1 and hole-check first, every time.
- No datum discipline: dimensions from random faces → unbuildable drawings.
- Forgetting assembly ORDER: parts that can't physically be installed in any
  sequence (screwdriver has no line of approach).
- Ignoring thermal: enclosed electronics need vents/airflow math, PLA creeps
  near warm motors/regulators — pick material per temperature.
- Interference only checked visually: run the CAD interference/section tools,
  moving mechanisms through their FULL travel.

## Verification specifics
- V0 = interference check + section views through full range of motion.
- V1 = test coupon / critical-feature test print measured with calipers, logged.
- V2 = fit check against real mating hardware; V3 = assembled, under real loads.
- Evidence: photos with calipers in frame, measured-vs-nominal table.

## File discipline
- Native CAD in the owning subsystem's `design/`; export STEP alongside at
  every released rev (rev suffix `-rA`, `-rB`; never overwrite a rev — LAW L9).
- Print settings that produced a good part = engineering data: filed next to
  the STL (material, layer height, walls, infill, orientation).

## Environment (feeds P11)
CAD seat (Fusion/FreeCAD/SolidWorks/Onshape), slicer + printer profiles,
calipers. License/account status recorded in env/ENVIRONMENT.yaml.

## Init additions (P01)
Ask: manufacturing methods available (printer models, materials on hand, shop
access), envelope/mass constraints, vibration/impact environment, target
operating temperature, are there COTS parts to design around (get them
physically before finalizing mounts?).
