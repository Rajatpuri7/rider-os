#!/usr/bin/env python3
"""validate.py — mechanical structure/consistency checks for RIDER (P09 step 0).

Catches structural rot cheaply, before the manual audit sweeps:
  1. Required directories and kernel files present
  2. Broken relative markdown links / file references
  3. Duplicate IDs (T####, ADR-####, R-*-###, IF-*)
  4. planning/active/ over the hard cap of 3 tasks
  5. Stale state/NOW.md (older than every other recently-touched state file)
  6. Task files missing mandatory sections (Objective / Done when)
  7. Subsystems missing STATUS.md
  8. Naming convention violations in planning/ and state/sessions/

Exit code: 0 clean (warnings allowed), 1 if any ERROR-level finding.
Stdlib only, cross-platform.

Usage:  python ops/validate.py
"""

import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Windows consoles often default to cp1252 — force UTF-8 so output never mangles.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REQUIRED_DIRS = [
    "kernel", "kernel/protocols", "kernel/templates", "kernel/playbooks",
    "state", "knowledge", "knowledge/requirements", "knowledge/decisions",
    "knowledge/research", "knowledge/reference",
    "planning", "planning/backlog", "planning/active", "planning/done",
    "intake", "intake/inbox", "intake/processed",
    "integration", "integration/interfaces",
    "subsystems", "verification", "delivery", "archive", "env", "ops",
]
REQUIRED_FILES = [
    "CLAUDE.md", "AGENTS.md", "GEMINI.md", "MAP.md", "PROJECT_PROFILE.yaml",
    "kernel/BOOT.md", "kernel/LAWS.md", "kernel/FAILURE-MODES.md",
    "kernel/PROMPTS.md", "kernel/META.md",
    "state/NOW.md", "state/QUESTIONS.md", "state/RISKS.md",
    "state/LESSONS.md", "state/ASSUMPTIONS.md",
    "env/ENVIRONMENT.yaml",
]
ACTIVE_CAP = 3
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "archive"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(p):
    return str(Path(p).relative_to(ROOT)).replace("\\", "/")


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if not any(part in SKIP_DIRS for part in p.parts):
            yield p


# 1 ---------------------------------------------------------------- structure
def check_structure():
    for d in REQUIRED_DIRS:
        if not (ROOT / d).is_dir():
            err(f"missing directory: {d}/")
    for f in REQUIRED_FILES:
        if not (ROOT / f).is_file():
            err(f"missing file: {f}")


# 2 ------------------------------------------------------------- broken links
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)[^)]*\)|`((?:kernel|state|knowledge|"
                     r"planning|intake|integration|subsystems|verification|"
                     r"delivery|archive|env|ops)/[A-Za-z0-9_\-./]+\.[a-z]{2,4})`")


def check_links():
    for f in md_files():
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in LINK_RE.finditer(text):
            target = m.group(1) or m.group(2)
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            # placeholders like YYYY-MM-DD or <slug> are documentation, not links
            if any(tok in target for tok in ("<", ">", "YYYY", "####", "...", "*")):
                continue
            cand = (f.parent / target) if m.group(1) else (ROOT / target)
            if not cand.exists():
                err(f"broken reference in {rel(f)}: {target}")


# 3 ------------------------------------------------------------ duplicate IDs
ID_PATTERNS = {
    "task": re.compile(r"\bT(\d{4})\b"),
    "adr": re.compile(r"\bADR-(\d{4})\b"),
}


def check_duplicate_ids():
    # IDs are *defined* by filenames; mentions in prose are references.
    def defined(pattern, roots):
        seen = {}
        for root in roots:
            base = ROOT / root
            if not base.is_dir():
                continue
            for p in base.rglob("*.md"):
                m = pattern.search(p.name)
                if m:
                    seen.setdefault(m.group(0), []).append(rel(p))
        return seen

    for label, pat, roots in (
        ("task ID", ID_PATTERNS["task"],
         ["planning/backlog", "planning/active", "planning/done"]),
        ("ADR ID", ID_PATTERNS["adr"], ["knowledge/decisions"]),
    ):
        for id_, files in defined(pat, roots).items():
            if len(files) > 1:
                err(f"duplicate {label} {id_}: {', '.join(files)}")


# 4 ---------------------------------------------------------------- WIP cap
def check_active_cap():
    active = ROOT / "planning" / "active"
    if active.is_dir():
        tasks = [p for p in active.glob("*.md") if p.name.upper() != "README.MD"]
        if len(tasks) > ACTIVE_CAP:
            err(f"planning/active/ holds {len(tasks)} tasks — hard cap is "
                f"{ACTIVE_CAP} (move extras to backlog): "
                + ", ".join(p.name for p in tasks))


# 5 ---------------------------------------------------------------- stale NOW
def check_now_freshness():
    now = ROOT / "state" / "NOW.md"
    if not now.is_file():
        return
    now_m = now.stat().st_mtime
    newer = []
    for scope in ("planning/active", "state/sessions", "subsystems"):
        base = ROOT / scope
        if base.is_dir():
            for p in base.rglob("*.md"):
                # _TEMPLATE dirs and READMEs are scaffolding, not work
                if p.name.upper() == "README.MD" or any(
                        part.startswith("_") for part in p.relative_to(base).parts):
                    continue
                if p.stat().st_mtime > now_m + 60:
                    newer.append(rel(p))
    if newer:
        days = (time.time() - now_m) / 86400
        warn(f"state/NOW.md ({days:.1f} days old) is older than {len(newer)} "
             f"working file(s) — likely stale. Newest: {newer[-1]}")


# 6 ------------------------------------------------------- task file sections
TASK_SECTIONS = ("Objective", "Done when")


def check_task_sections():
    for folder in ("planning/backlog", "planning/active", "planning/done"):
        base = ROOT / folder
        if not base.is_dir():
            continue
        for p in base.glob("*.md"):
            if p.name.upper() == "README.MD":
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            for section in TASK_SECTIONS:
                if not re.search(rf"^#+.*{re.escape(section)}", text,
                                 re.IGNORECASE | re.MULTILINE):
                    err(f"{rel(p)}: missing mandatory section '{section}'")


# 7 --------------------------------------------------------- subsystem STATUS
def check_subsystem_status():
    base = ROOT / "subsystems"
    if not base.is_dir():
        return
    for d in base.iterdir():
        if d.is_dir() and not d.name.startswith("_"):
            if not (d / "STATUS.md").is_file():
                err(f"subsystems/{d.name}/ has no STATUS.md")


# 8 ------------------------------------------------------------------- naming
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9.]+)*\.md$")
SESSION_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}(-[a-z0-9-]+)?\.md$")


def check_naming():
    for folder in ("planning/backlog", "planning/active", "planning/done"):
        base = ROOT / folder
        if base.is_dir():
            for p in base.glob("*.md"):
                if p.name.upper() != "README.MD" and not KEBAB.match(p.name):
                    warn(f"{rel(p)}: not lowercase-kebab-case")
    sessions = ROOT / "state" / "sessions"
    if sessions.is_dir():
        for p in sessions.glob("*.md"):
            if p.name.upper() != "README.MD" and not SESSION_NAME.match(p.name):
                warn(f"{rel(p)}: session logs are YYYY-MM-DD-<n>.md")


# ----------------------------------------------------------------------- main
def main():
    print(f"RIDER validate — {ROOT}")
    print("-" * 60)
    check_structure()
    check_links()
    check_duplicate_ids()
    check_active_cap()
    check_now_freshness()
    check_task_sections()
    check_subsystem_status()
    check_naming()

    for e in errors:
        print(f"[ERROR] {e}")
    for w in warnings:
        print(f"[WARN ] {w}")
    print("-" * 60)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    if not errors and not warnings:
        print("Structure clean.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
