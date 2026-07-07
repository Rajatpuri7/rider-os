# PLAYBOOK — machine-learning

> Model training, datasets, evaluation, deployment of learned components.

## Judgment rules
- Baseline before learning: the dumb solution (mean predictor, threshold,
  classical algorithm, lookup table) is mandatory task #1. It sets the bar and
  sometimes wins — an ML model that can't beat a threshold is negative value.
- Data > architecture: an hour on data quality (label errors, leakage, class
  balance, distribution match to deployment) beats a day of model tweaking.
  LOOK at raw samples — 30 minutes of eyeballing finds what stats hide.
- The split is sacred: test set decided before training, touched once at the
  end, never used to pick anything. Split by GROUP (per-session, per-device,
  per-day) not by row when correlated — random row splits on time-series is
  leakage in disguise.
- Overfit a single batch first: a model that can't memorize 32 samples has a
  bug, not a capacity problem. Cheapest sanity check in the field.
- One change per experiment, everything versioned: data hash, code commit,
  hyperparams, seed, metrics — or you're generating anecdotes (EXPERIMENT
  template applies).
- Deployment distribution rules everything: train/eval on data from the real
  sensor/environment or document the gap as a top-3 risk.

## Gotchas that burn people
- Leakage: normalization fit on all data, augmentation before split, duplicate
  near-identical frames across splits, target hiding in a feature. If results
  look too good, hunt leakage FIRST.
- Metric mismatch: accuracy on 95/5 imbalance is a lie — pick the metric that
  matches the cost of each error type, get the human to confirm it.
- Silent preprocessing drift between train and deploy (resize interpolation,
  color space, normalization constants) — checksum the preprocessing.
- Nondeterminism blamed on "ML being ML": set seeds, pin versions; remaining
  variance measured across ≥3 runs, reported as a range not a point.
- Eval on the happy path only: report per-slice metrics (per-class, per-
  condition, worst-case), not just the average.

## Verification specifics
- V1 = metrics on the held-out set (per-slice, with the versioning block).
  V2 = model in the real pipeline on recorded real data, latency measured on
  target hardware. V3 = live in the field. Benchmarks ≠ your camera at dusk.
- Every trained artifact gets a card: data version, code commit, metrics,
  intended domain, KNOWN FAILURE MODES — filed with the model file.

## Environment (feeds P11)
Pinned framework (torch/tf/sklearn), GPU/driver/CUDA stack recorded exactly,
experiment tracking (even a CSV + EXPERIMENT files), dataset storage location
+ gitignore (data never in git; hashes/manifests are).

## Init additions (P01)
Ask: what data exists TODAY (amount, labels, quality, licensing), what the
deployment target is (latency/memory/compute ceiling), cost of each error type
(sets the metric), is more data collectable (by whom, how fast), baseline
candidates.
