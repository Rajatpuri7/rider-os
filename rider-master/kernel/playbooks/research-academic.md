# PLAYBOOK — research-academic

> Thesis/course/publication projects, literature-heavy work, novel-method
> development. Adds scholarly discipline on top of P07-RESEARCH.

## Judgment rules
- The research question is the product: one falsifiable question, written,
  frozen-ish. Every task either serves it or is scope creep — the #1 killer
  of theses is a question that quietly became four questions.
- Contribution ≠ effort: state explicitly what is NEW (method? evidence?
  benchmark? negative result?) versus what is reproduction/plumbing. Advisors
  and reviewers grade the delta, not the sweat.
- Reproduce the baseline first: before improving on Paper X, reproduce Paper X.
  If you can't, that's a finding (and a common one — document the gap).
  Improvements over an unreproduced baseline are unpublishable vapor.
- Negative results are results: an experiment that kills an approach saved you
  a month — write it up (EXPERIMENT → research note), don't bury it. The
  archive of dead ends is half a thesis's related-work section.
- Write as you go: bullet-point findings into delivery/docs/ the day they
  happen. A thesis written from session logs takes weeks; from memory, months.
- Citation hygiene from day one: every claim that will appear in writing keeps
  its source pinned (P07 grades). Retro-fitting citations is agony and where
  accidental plagiarism is born.

## Gotchas that burn people
- Deadline physics: experiments always overrun; freeze new experiments at
  T-minus-⅓ of remaining time and pivot to writing/analysis. Put this date in
  planning/ROADMAP.md at init.
- Comparing against strawmen: your method with tuned hyperparams vs baselines
  at defaults is self-deception reviewers smell instantly (fair-comparison
  rules → same budget, same data, same metric).
- p-hacking by iteration: rerunning until significant, then reporting the last
  run. Pre-register the metric and n in the EXPERIMENT file (the template's
  prediction-before-running field IS the pre-registration).
- Advisor drift: monthly one-page status against the frozen question keeps
  scope negotiations explicit instead of ambient.
- Data/ethics/approval lead times (IRB, datasets with licenses, lab access)
  are long-lead items → RISKS at init.

## Verification specifics
- Claims in the write-up trace to: experiment file + evidence + code commit.
  A results table nobody can regenerate is a liability at defense time —
  scripts that rebuild every figure from raw data live in delivery/docs/figures/.
- Related-work coverage check at audit (P09): any new SOTA on your question
  published since last check? (Schedule a literature re-sweep every ~6 weeks.)

## Environment (feeds P11)
Reference manager (Zotero + Better BibTeX default), LaTeX/typst toolchain or
required template from the institution, plotting stack with a house style file
(consistent figures from day one), word/page limits recorded as constraints.

## Init additions (P01)
Ask: the research question in one sentence, what's graded/reviewed and by whom
(rubric → requirements), hard dates (defense, submission, conference
deadlines → constraints + the freeze date), advisor cadence, prior work by the
group to build on (get the repos/theses into intake).
