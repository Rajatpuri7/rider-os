#!/usr/bin/env python3
"""doctor.py — environment health check for RIDER (P11-ENVIRONMENT step 3).

Reads env/ENVIRONMENT.yaml, runs each tool's check command, compares versions,
and reports PASS / WRONG-VERSION / MISSING / HUMAN-VERIFY with per-OS install
hints. Exit code 1 if any *required* item is missing or wrong-version, else 0.

Stdlib only. Uses PyYAML if installed, otherwise a built-in parser that
handles the manifest's YAML subset (top-level keys, block lists of flat dicts,
inline {…} dicts, quoted strings, booleans, comments).

Usage:  python ops/doctor.py            (from the project root)
        python ops/doctor.py --verbose  (show command output on failures)
"""

import argparse
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "env" / "ENVIRONMENT.yaml"

# Windows consoles often default to cp1252 — force UTF-8 so output never mangles.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------- YAML subset
def _strip_comment(line):
    """Remove a trailing # comment, respecting single/double quotes."""
    out, quote = [], None
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
            out.append(ch)
        elif ch == "#":
            break
        else:
            out.append(ch)
    return "".join(out).rstrip()


def _parse_scalar(s):
    s = s.strip()
    if s in ("", "~", "null"):
        return None
    if s == "[]":
        return []
    if s == "{}":
        return {}
    if s.startswith("[") and s.endswith("]"):
        parts, buf, quote = [], [], None
        for ch in s[1:-1]:
            if quote:
                buf.append(ch)
                if ch == quote:
                    quote = None
            elif ch in ("'", '"'):
                quote = ch
                buf.append(ch)
            elif ch == ",":
                parts.append("".join(buf))
                buf = []
            else:
                buf.append(ch)
        parts.append("".join(buf))
        return [_parse_scalar(p) for p in parts if p.strip()]
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    if s.startswith("{") and s.endswith("}"):
        d = {}
        # split on commas not inside quotes
        parts, buf, quote = [], [], None
        for ch in s[1:-1]:
            if quote:
                buf.append(ch)
                if ch == quote:
                    quote = None
            elif ch in ("'", '"'):
                quote = ch
                buf.append(ch)
            elif ch == ",":
                parts.append("".join(buf))
                buf = []
            else:
                buf.append(ch)
        parts.append("".join(buf))
        for p in parts:
            if ":" in p:
                k, _, v = p.partition(":")
                d[k.strip()] = _parse_scalar(v)
        return d
    return s


def parse_manifest(text):
    """Parse the ENVIRONMENT.yaml subset into a dict. Not a general YAML parser."""
    data = {}
    key = None            # current top-level key
    item = None           # current list-item dict being built
    for raw in text.splitlines():
        line = _strip_comment(raw)
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()
        if indent == 0:
            k, _, rest = stripped.partition(":")
            key, item = k.strip(), None
            data[key] = _parse_scalar(rest) if rest.strip() else []
        elif stripped.startswith("- "):
            body = stripped[2:].strip()
            if not isinstance(data.get(key), list):
                data[key] = []
            if body.startswith("{"):             # inline dict item
                item = None
                data[key].append(_parse_scalar(body))
            elif ":" in body:                    # block dict item (first field)
                item = {}
                k, _, v = body.partition(":")
                item[k.strip()] = _parse_scalar(v)
                data[key].append(item)
            else:                                # plain string item
                item = None
                data[key].append(_parse_scalar(body))
        else:                                    # continuation of current dict
            if item is not None and ":" in stripped:
                k, _, v = stripped.partition(":")
                item[k.strip()] = _parse_scalar(v)
    return data


def load_manifest():
    if not MANIFEST.exists():
        print(f"FATAL: {MANIFEST} not found. Run from the project root.")
        sys.exit(2)
    text = MANIFEST.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text) or {}
    except ImportError:
        return parse_manifest(text)


# ------------------------------------------------------------------- checking
def current_os():
    return {"Windows": "windows", "Darwin": "macos", "Linux": "linux"}.get(
        platform.system(), "linux")


def version_tuple(s):
    m = re.search(r"(\d+(?:\.\d+)+|\d+)", s or "")
    return tuple(int(p) for p in m.group(1).split(".")) if m else None


def run(cmd, verbose=False):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           timeout=60)
        out = (r.stdout or "") + (r.stderr or "")
        if verbose and r.returncode != 0:
            print(f"        $ {cmd}\n        -> exit {r.returncode}: {out.strip()[:200]}")
        return r.returncode == 0, out
    except Exception as e:                       # timeout, not-found, etc.
        if verbose:
            print(f"        $ {cmd}\n        -> {e}")
        return False, str(e)


def install_hint(entry, osname):
    inst = entry.get("install") or {}
    if isinstance(inst, dict):
        return inst.get(osname) or " / ".join(f"{k}: {v}" for k, v in inst.items())
    return str(inst)


def check_tool(entry, osname, verbose):
    """Return (status, message). status in PASS/MISSING/WRONG-VERSION/SKIP."""
    name = entry.get("name", "<unnamed>")
    check = entry.get("check")
    if not check:
        return "SKIP", f"{name}: no check command in manifest"
    ok, _ = run(check, verbose)
    if not ok:
        hint = install_hint(entry, osname)
        return "MISSING", f"{name} — install ({osname}): {hint or 'no hint recorded'}"
    minv = entry.get("min_version")
    vcmd = entry.get("version_cmd") or check
    if minv:
        _, out = run(vcmd, verbose)
        have, want = version_tuple(out), version_tuple(str(minv))
        if have and want and have < want:
            return "WRONG-VERSION", f"{name} {'.'.join(map(str, have))} < required {minv}"
        if not have:
            return "PASS", f"{name} (present; version unparseable — wanted >= {minv})"
        return "PASS", f"{name} {'.'.join(map(str, have))} (>= {minv})"
    return "PASS", name


def check_package(entry, verbose):
    name = entry.get("name", "<unnamed>")
    code = (f"import importlib.metadata as m, importlib; "
            f"importlib.import_module('{entry.get('import_name', name)}'); "
            f"print(m.version('{name}'))")
    ok, out = run(f'{sys.executable} -c "{code}"', verbose)
    if not ok:
        return "MISSING", f"python package {name} — pip install {name}"
    minv = entry.get("min_version")
    if minv:
        have, want = version_tuple(out), version_tuple(str(minv))
        if have and want and have < want:
            return "WRONG-VERSION", f"{name} {'.'.join(map(str, have))} < required {minv}"
    return "PASS", f"python package {name} {out.strip()}"


# ----------------------------------------------------------------------- main
BADGE = {"PASS": "[PASS] ", "MISSING": "[MISS] ", "WRONG-VERSION": "[VER ] ",
         "HUMAN": "[HUMAN]", "SKIP": "[SKIP] "}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verbose", action="store_true",
                    help="show command output for failed checks")
    args = ap.parse_args()

    m = load_manifest()
    osname = current_os()
    print(f"RIDER doctor — {MANIFEST.relative_to(ROOT)} on {osname}")
    print("-" * 60)

    counts = {"PASS": 0, "MISSING": 0, "WRONG-VERSION": 0, "HUMAN": 0, "SKIP": 0}
    required_failed = []

    tools = m.get("tools") or []
    pkgs = m.get("python_packages") or []
    if not any([tools, pkgs, m.get("ide_extensions"), m.get("mcp_servers"),
                m.get("manual_items")]):
        print("Manifest is empty — environment not yet derived.")
        print("Run P11-ENVIRONMENT (kernel/protocols/P11-ENVIRONMENT.md) to fill it.")
        return 0

    for entry in tools:
        status, msg = check_tool(entry, osname, args.verbose)
        counts[status] += 1
        print(f"{BADGE[status]} {msg}")
        if status in ("MISSING", "WRONG-VERSION") and entry.get("required", True):
            required_failed.append(entry.get("name", "<unnamed>"))

    for entry in pkgs:
        status, msg = check_package(entry, args.verbose)
        counts[status] += 1
        print(f"{BADGE[status]} {msg}")
        if status in ("MISSING", "WRONG-VERSION") and entry.get("required", True):
            required_failed.append(entry.get("name", "<unnamed>"))

    # Items no command can verify — print as reminders for the human.
    for kind, key in (("IDE extension", "ide_extensions"),
                      ("MCP server", "mcp_servers"),
                      ("manual item", "manual_items")):
        for entry in (m.get(key) or []):
            if isinstance(entry, dict):
                name = entry.get("id") or entry.get("name", "<unnamed>")
                how = entry.get("how_to_verify") or entry.get("config_hint") or ""
                extra = f" — {how}" if how else ""
            else:
                name, extra = str(entry), ""
            counts["HUMAN"] += 1
            print(f"{BADGE['HUMAN']} {kind}: {name}{extra}")

    for note in (m.get("setup_notes") or []):
        print(f"[NOTE]  read env/{note}")

    print("-" * 60)
    print(f"Summary: {counts['PASS']} pass, {counts['MISSING']} missing, "
          f"{counts['WRONG-VERSION']} wrong-version, {counts['HUMAN']} human-verify")
    if required_failed:
        print(f"REQUIRED items failing: {', '.join(required_failed)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
