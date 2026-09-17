#!/usr/bin/env python3
"""Local build for the Celbridge docs, mirroring what the publish workflow runs.

Order matters: the redirect stubs are written into the build output, so the
build has to run first.

    python build.py          build once into site/
    python build.py serve    serve on http://localhost:8000 with live reload

The interpreter and the zensical binary are resolved in this order: the PY and
ZENSICAL environment variables, then the repo's .venv (the local flow the README
documents), then PATH (which is what a Celbridge Python console provides, since
site-server.console and site-re-builder.console declare zensical as a
dependency). The resolved pair is printed, so which one ran is never a guess.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_BIN = ROOT / ".venv" / ("Scripts" if os.name == "nt" else "bin")
EXE = ".exe" if os.name == "nt" else ""


def resolve(env_name: str, command: str) -> str:
    """The executable to run for a step, by the order documented above."""
    override = os.environ.get(env_name)
    if override:
        return override

    in_venv = VENV_BIN / f"{command}{EXE}"
    if in_venv.is_file():
        return str(in_venv)

    on_path = shutil.which(command)
    if on_path:
        return on_path

    raise SystemExit(
        f"error: {command} not found. Either create the venv the README describes, "
        f"or set {env_name} to its path."
    )


# Unflushed, Python holds a banner behind the subprocess output it introduces and the
# console log reads out of order.
def say(line: str = "") -> None:
    print(line, flush=True)


def run_step(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    python = resolve("PY", "python")
    zensical = resolve("ZENSICAL", "zensical")
    say(f"==> python:   {python}")
    say(f"==> zensical: {zensical}")

    if sys.argv[1:2] == ["serve"]:
        say("==> serving on http://localhost:8000")
        return subprocess.run([zensical, "serve"], cwd=ROOT).returncode

    # --strict is what the publish workflow runs, so a broken internal link
    # fails here rather than shipping a site with holes in it.
    say("==> building (strict)")
    run_step(zensical, "build", "--clean", "--strict")

    say("==> writing redirect stubs for the old Sphinx URLs")
    run_step(python, "scripts/gen_redirect_stubs.py")

    say()
    say("Done. Output in site/ — preview it with site_preview.webview")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode)
