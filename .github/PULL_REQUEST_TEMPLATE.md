## What & why

<!-- One paragraph. For kernel changes: which lesson/failure drove this?
     (META.md rule: no speculative kernel changes.) -->

## Checklist

- [ ] `python rider-master/ops/validate.py` passes (0 errors)
- [ ] Kernel change? → row added to `rider-master/kernel/CHANGELOG.md` with the driving lesson
- [ ] Ops script change? → stdlib-only, cross-platform (no new dependencies)
- [ ] No kernel file pushed past ~200 lines (anti-bloat rule)
