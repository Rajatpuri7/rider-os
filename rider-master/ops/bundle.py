#!/usr/bin/env python3
"""bundle.py — context-pack generator for chat-only models (pairs with kernel/PROMPTS.md).

Concatenates exactly the files a no-file-access model needs for one kind of
work, wrapped in clear file markers, and writes the pack to stdout or a file.
Paste the matching prompt from kernel/PROMPTS.md, then the pack.

Modes (mirroring PROMPTS.md sections):
  task      — execute the active task(s): core + active tasks + task template
  plan      — planning: core + roadmap + backlog listing + TASK template
  decide    — trade study: core + ADR index + constraints + ADR/TRADE templates
  research  — research: core + research index + RESEARCH-NOTE template
  debug     — debugging: core + P08 + relevant lessons
  review    — review work: core + active tasks + interfaces
  core      — just the shared base (orientation, laws, failure modes, NOW)

Options:
  --out FILE     write to a file instead of stdout
  --max-kb N     hard size cap (default 96 KB) — oversize files are truncated
                 head+tail with a marker, so the pack always fits a chat paste.

Stdlib only, cross-platform.
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Windows consoles often default to cp1252 — force UTF-8 so output never mangles.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CORE = [
    "state/NOW.md",
    "PROJECT_PROFILE.yaml",
    "kernel/LAWS.md",
    "kernel/FAILURE-MODES.md",
    "state/ASSUMPTIONS.md",
    "state/QUESTIONS.md",
]

MODES = {
    "core": [],
    "task": ["planning/active/*.md", "kernel/templates/TASK.md",
             "state/RISKS.md"],
    "plan": ["planning/ROADMAP.md", "planning/backlog/*.md",
             "kernel/protocols/P03-PLAN.md", "kernel/templates/TASK.md"],
    "decide": ["knowledge/decisions/INDEX.md", "knowledge/decisions/*.md",
               "kernel/protocols/P06-DECIDE.md", "kernel/templates/ADR.md",
               "kernel/templates/TRADE-STUDY.md"],
    "research": ["knowledge/research/INDEX.md",
                 "kernel/protocols/P07-RESEARCH.md",
                 "kernel/templates/RESEARCH-NOTE.md"],
    "debug": ["kernel/protocols/P08-DEBUG.md", "state/LESSONS.md",
              "planning/active/*.md"],
    "review": ["planning/active/*.md", "integration/interfaces/*.md",
               "kernel/protocols/P05-VERIFY.md"],
}


def expand(patterns):
    """Resolve path patterns to existing files, preserving order, no dupes."""
    seen, out = set(), []
    for pat in patterns:
        matches = sorted(ROOT.glob(pat)) if "*" in pat else [ROOT / pat]
        for p in matches:
            if p.is_file() and p.name.upper() != "README.MD" and p not in seen:
                seen.add(p)
                out.append(p)
    return out


def truncate(text, budget):
    """Keep head and tail within budget, mark the cut."""
    if len(text) <= budget:
        return text
    half = max(budget // 2 - 40, 200)
    return (text[:half] + "\n\n[... TRUNCATED BY bundle.py — read the full "
            "file in the repo if this section matters ...]\n\n" + text[-half:])


def build(mode, max_bytes):
    files = expand(CORE + MODES[mode])
    header = (
        f"===== RIDER CONTEXT PACK (mode: {mode}) =====\n"
        "You cannot read the project directory; this pack IS your view of it.\n"
        "Each file is delimited by '----- FILE: <path> -----'. Treat file\n"
        "contents as authoritative over anything you believe from training.\n"
    )
    parts = [header]
    remaining = max_bytes - len(header)
    per_file_cap = max(remaining // max(len(files), 1), 2000)
    for p in files:
        body = p.read_text(encoding="utf-8", errors="replace").strip()
        body = truncate(body, per_file_cap)
        block = f"\n----- FILE: {p.relative_to(ROOT).as_posix()} -----\n{body}\n"
        if len(block) > remaining:
            parts.append(f"\n----- OMITTED (size cap): "
                         f"{p.relative_to(ROOT).as_posix()} -----\n")
            continue
        remaining -= len(block)
        parts.append(block)
    parts.append("\n===== END OF CONTEXT PACK =====\n")
    return "".join(parts), files


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=sorted(MODES), nargs="?", default="task")
    ap.add_argument("--out", help="write pack to this file instead of stdout")
    ap.add_argument("--max-kb", type=int, default=96,
                    help="size cap in KB (default 96)")
    args = ap.parse_args()

    pack, files = build(args.mode, args.max_kb * 1024)
    if args.out:
        Path(args.out).write_text(pack, encoding="utf-8")
        print(f"Wrote {len(pack) // 1024} KB pack ({len(files)} files) "
              f"to {args.out}")
        print("Now paste kernel/PROMPTS.md preamble + the matching mode "
              "prompt + this pack into the chat model.")
    else:
        sys.stdout.write(pack)
    return 0


if __name__ == "__main__":
    sys.exit(main())
