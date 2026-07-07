# ops/ — mechanical tooling

Three stdlib-only, cross-platform Python scripts. They are the *mechanical*
half of the system's discipline: protocols reference them by name, so they
must stay runnable. All run from the project root.

| Script | What it does | Called by | Exit 1 when |
|---|---|---|---|
| `validate.py` | Structure/consistency check: required dirs+files, broken references, duplicate T####/ADR-#### IDs, `planning/active/` > 3 tasks, stale NOW.md, tasks missing Objective/Done-when, subsystems missing STATUS.md, naming conventions | P09-AUDIT step 0; run any time things feel messy | any ERROR-level finding |
| `doctor.py` | Reads `env/ENVIRONMENT.yaml`, runs every tool's check command, compares versions, prints PASS / MISS / VER / HUMAN-VERIFY with per-OS install hints | P11-ENVIRONMENT step 3; on any new machine; after "works on my machine" claims | a **required** item is missing or wrong-version |
| `bundle.py` | Generates a context pack for chat-only models (web ChatGPT/Gemini): core state + mode-specific files, size-capped, file-delimited | `kernel/PROMPTS.md` workflow | — |

```
python ops/validate.py
python ops/doctor.py [--verbose]
python ops/bundle.py {task|plan|decide|research|debug|review|core} [--out FILE] [--max-kb N]
```

Notes:
- `doctor.py` uses PyYAML if installed, else a built-in parser covering the
  manifest's YAML subset (block lists, inline `{...}`/`[...]`, quoted strings).
  Keep `env/ENVIRONMENT.yaml` within that subset (no anchors, no multiline).
- `validate.py` warnings don't fail the run; errors do. Fix errors before
  claiming an audit passed.
- `bundle.py --max-kb` truncates oversized files head+tail with a visible
  marker so a pack always fits in one chat paste.
