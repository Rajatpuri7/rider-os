# P07 — RESEARCH (question-driven, source-graded)

Research answers a question. Browsing fills a session. This protocol prevents
the second from wearing the first's clothes.

## Step 1 — Anchor to a question

Every research effort starts from an entry in `state/QUESTIONS.md` (create one
if missing). Write: what an ANSWER would look like, what decision/task it
unblocks, and how much confidence is enough. Time-box: default 1 session;
extending requires writing down what was learned so far and why more is needed.

## Step 2 — Source hierarchy (grade every claim)

| Grade | Sources | Trust |
|---|---|---|
| A | Datasheets, standards, official docs, measured data, primary papers | Cite and rely |
| B | Peer-reviewed secondary, vendor app notes, established textbooks | Rely, verify units/versions |
| C | Engineering blogs, conference talks, high-quality forum answers | Lead worth verifying |
| D | Random forums, AI model output (yours included), marketing pages | Hypothesis only — must upgrade before load-bearing use |

A load-bearing claim (one a design decision rests on) needs **two independent
B+ sources or one A source**. Grade-D claims never enter REQUIREMENTS.md or an
ADR's rationale ungraded-up.

## Step 3 — Version and date discipline

Check WHEN each source was written and WHICH version it covers. An answer true
for firmware v2 / ROS1 / the 2019 silicon revision may be false today. Record
version/date next to the claim.

## Step 4 — Capture as a research note

Use `kernel/templates/RESEARCH-NOTE.md` → `knowledge/research/`, add a row to
`knowledge/research/INDEX.md`. The core is the claims table: claim | source |
grade | date/version | implication FOR THIS PROJECT. A claim whose implication
you cannot state is decoration — either derive the implication or drop it.

## Step 5 — Contradictions

Two credible sources disagree → do NOT average or silently pick one. Record
both, note the discrepancy, and either (a) design the experiment that settles
it, or (b) escalate to `state/QUESTIONS.md` flagged for the human.

## Step 6 — Close the loop

1. Answer the Q-entry (status: answered, link to note) — or split it into
   sharper sub-questions if the research revealed the question was wrong.
2. Spawn what the answer implies: ADR needed? task? new risk? glossary terms?
3. Anything ordered/downloaded (papers, datasheets) → `knowledge/reference/`
   per P02 naming.

## Anti-patterns

- **Rabbit hole**: interesting ≠ relevant. Park tangents as new Q-entries.
- **Copy-paste comprehension**: if you can't restate the mechanism in two
  sentences, you don't have the fact yet.
- **Authority laundering**: "many sources say" without names = grade D.
- **Answering the askable instead of the asked**: re-read the Q-entry before
  writing the TL;DR.
