# Security Policy

RIDER is a directory template plus three stdlib-only Python scripts. It has no
server, no network calls, no runtime, and no dependencies — the attack surface
is intentionally near zero.

## Scope

Report a vulnerability if you find:
- Code execution or path traversal in `ops/validate.py`, `ops/doctor.py`, or
  `ops/bundle.py` (e.g., a malicious `ENVIRONMENT.yaml` executing unintended
  commands — note `doctor.py` deliberately runs the `check:` commands listed in
  the manifest; the manifest is trusted input owned by the project).
- Prompt-injection vectors *in the kernel files themselves* that would cause an
  agent to violate the LAWS (e.g., wording that a model reliably misreads as
  permission to delete or exfiltrate).

## Reporting

Use GitHub's **private vulnerability reporting** (Security tab → Report a
vulnerability). Please do not open public issues for security reports. You'll
get a response within 7 days.

## Non-goals

RIDER cannot make an AI agent safe against a malicious *user* or malicious
*project files placed in `intake/`* — treat files you drop into a project with
the same trust you'd give them in any working directory.
