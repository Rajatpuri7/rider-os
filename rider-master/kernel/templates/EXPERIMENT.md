# EXP-YYYY-MM-DD — <question being tested>

> An experiment buys a fact. If no decision changes based on the outcome,
> don't run it.

- **Question**: <from state/QUESTIONS.md — link the Q entry>
- **Decision it unblocks**: <ADR / task / plan step>
- **Hypothesis**: <falsifiable statement — "X will achieve Y under Z">
- **Prediction BEFORE running**: <expected numbers/behavior. Committing before
  running is the whole point — it exposes wrong mental models.>

## Method
- Setup: <hardware rev, wiring, software versions, config, dataset —
  enough for someone else to reproduce>
- Procedure: <numbered steps>
- Measured variables: <what, with what instrument/tool, at what precision>
- Trials: <n — one run is an anecdote>

## Results (raw first — evidence before narrative)
- Evidence: `verification/evidence/EXP-.../`
- Data summary: <table/numbers>

## Analysis
- Prediction vs observed: <match / deviation and by how much>
- Surprises: <anything unexpected — each surprise is either explained here or
  becomes a QUESTIONS.md entry>

## Conclusion
- Hypothesis: supported / refuted / inconclusive (n too small, confound found)
- Confidence: <high/medium/low + why>
- **Fact bought**: <one sentence — goes to knowledge/research/ as a note if
  load-bearing>
- Spawned: <ADR now unblocked, new questions, new risks>
