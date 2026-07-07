# POSTMORTEM — <incident / failed milestone / burned week>

> Blameless, mechanism-focused. The output is prevention, not a confession.
> Trigger: hardware damaged, deadline badly missed, work lost, demo failed,
> or any surprise expensive enough that you'd pay a session to not repeat it.

- **Date of incident / of writing**: … / …
- **Cost**: <time lost, money, hardware, credibility>

## Timeline (facts only, timestamped, no interpretation yet)
| When | What happened / what was known |
|---|---|

## Contributing causes (usually several — "root cause" singular is a myth)
1. <mechanism, not person: "no current limit set on the bench supply", not "I was careless">
2. …

## What worked (keep doing)
<Detection, containment, recovery steps that went well.>

## Five whys on the dominant cause
Why? … → Why? … → Why? … <stop when you hit process/system, not person>

## Prevention actions (each gets an owner-artifact, or it's a wish)
| Action | Lands where |
|---|---|
| <e.g. add pre-power checklist to electronics playbook> | kernel change proposal (META.md) |
| <e.g. always fuse the 12V rail> | LESSONS.md + subsystem STATUS |

## Detection improvement
If the same thing starts happening again, what will now catch it earlier?
