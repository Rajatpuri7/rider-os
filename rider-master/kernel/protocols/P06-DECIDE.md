# P06 — DECIDE (choices that stick)

Use when choosing between alternatives: architecture, parts, algorithms,
libraries, tools, build-vs-buy, topology. The output is a decision that a
future session can trust without re-litigating.

## Step 0 — Is it already decided?

Check `knowledge/decisions/INDEX.md`. If an accepted ADR covers this: follow it.
Disagree with it? That's a NEW ADR proposing supersession (LAW L6) — never a
silent deviation.

## Step 1 — Classify the stakes

| Class | Test | Process |
|---|---|---|
| Trivial | Reversible in <1 hour, no money, no interfaces touched | Decide inline; one line in the task Work Log. Don't ADR-spam. |
| Consequential | Hard to reverse, or costs money/schedule, or others build on it | ADR (template `kernel/templates/ADR.md`) |
| Contested / high-stakes | Consequential AND options genuinely compete, or safety-tagged | TRADE-STUDY + ADR + human sign-off |

## Step 2 — Frame before comparing

Write these BEFORE listing options (options chosen first contaminate criteria):
- Decision statement: "We need to choose X so that Y, by Z."
- Constraints that disqualify (from PROJECT_PROFILE, requirements, physics, budget).
- Criteria that rank the survivors, weighted. Typical: fitness for requirement,
  simplicity, cost, availability/lead time, ecosystem/docs, reversibility,
  team/toolchain familiarity.

## Step 3 — Generate real options (minimum 3)

Must include where sane: **do nothing / defer**, **buy/reuse instead of build**,
and one option you didn't start out favoring. Two options = a coin flip dressed
up; the third option is where thinking happens.

## Step 4 — Steelman and attack

For each option, one paragraph arguing FOR it as its best advocate would.
Then explicitly attack your leading candidate: "the strongest reason this is
wrong is ___". If you cannot produce a real attack, you haven't understood the
alternatives (FAILURE-MODES: sycophancy-to-own-first-idea).

## Step 5 — Score and sanity-check (contested class)

Fill `kernel/templates/TRADE-STUDY.md`. Every cell gets a number AND a sentence
— numbers without rationale are theater. Then the sensitivity check: "which
single weight or score change flips the winner?" If the answer is "a small,
plausible one", say so — the decision is weak and the human should know.

## Step 6 — Decision smells (stop if you catch yourself)

- Choosing what the first search result / vendor page recommends.
- Choosing the shiny thing to learn it (resume-driven engineering).
- Sticking with a sunk cost ("we already wrote half of it").
- Averaging two options into a hybrid nobody would design from scratch.
- Deciding under a fact-gap a 30-minute experiment would close → run the
  experiment first (`kernel/templates/EXPERIMENT.md`).

## Step 7 — Record and propagate

1. Write the ADR: status `proposed`; `accepted` only after human confirmation
   when money/safety/schedule is involved (LAW L11).
2. Add row to `knowledge/decisions/INDEX.md`.
3. Spawn consequences: tasks to backlog, new risks to `state/RISKS.md`,
   interface updates if the decision changes any contract (LAW L8).
4. Link the ADR from the task that triggered it.
