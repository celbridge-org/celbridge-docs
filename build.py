#!/usr/bin/env python3
"""Build the Celbridge docs. Celbridge's site console and CI both run this.

Order matters: the redirect stubs are written into the build output, so the
build has to run first.

Runs everything with the Python that runs this script. In Celbridge that is
`site.console`'s own environment; in CI it is the runner's Python.

    python build.py                     build (strict), then write the redirect stubs
    python build.py redirects           rewrite the redirect stubs only
    python build.py serve               serve on http://localhost:8000
    python build.py serve --background  the same, but return once the server has started
"""

from __future__ import annotations

import argparse
import socket
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = sys.executable

# Line-buffered, so the banners this script prints stay in order with the output of
# the subprocesses they introduce. Piped into a console rather than a terminal,
# stdout is block-buffered and the log reads back to front.
sys.stdout.reconfigure(line_buffering=True)

# Run as a module rather than through the `zensical` launcher script: Celbridge's
# environments live under "Application Support", and a launcher's shebang line
# cannot hold a path with a space in it.
ZENSICAL = (PY, "-m", "zensical")

# Zensical's default server port. zensical.toml does not set `dev_addr`; if it ever
# does, change this to match, or the checks below look at the wrong port.
PORT = 8000

# How long `serve --background` waits for the server to answer before giving up.
STARTUP_TIMEOUT = 30


def run_step(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("127.0.0.1", port)) == 0


def redirects() -> None:
    print("==> writing redirect stubs for the old Sphinx URLs")
    run_step(PY, "scripts/gen_redirect_stubs.py")


def wait_for_server(server: subprocess.Popen) -> bool:
    deadline = time.monotonic() + STARTUP_TIMEOUT
    while time.monotonic() < deadline:
        if server.poll() is not None:
            return False
        if port_in_use(PORT):
            return True
        time.sleep(0.25)
    return False


def serve(background: bool) -> int:
    if port_in_use(PORT):
        print(f"Something is already serving on port {PORT}, so not starting another server.")
        print("If it is a leftover server, stop it and run this again.")
        return 1

    if not background:
        print("==> serving")
        return subprocess.run([*ZENSICAL, "serve"], cwd=ROOT).returncode

    # Left in this process's group, so the server stops when the console that
    # started it closes. Do not give it a session of its own.
    print("==> starting the server in the background")
    server = subprocess.Popen([*ZENSICAL, "serve"], cwd=ROOT)

    if not wait_for_server(server):
        if server.poll() is None:
            server.terminate()
            print(f"The server did not start answering on port {PORT} within {STARTUP_TIMEOUT}s.")
        else:
            print(f"The server exited with code {server.returncode}. See the output above.")
        return 1

    print(f"==> serving on http://localhost:{PORT} (pid {server.pid})")
    return 0


def build() -> int:
    # --strict fails the build on a broken internal link, rather than
    # publishing a site with holes in it.
    print("==> building (strict)")
    run_step(*ZENSICAL, "build", "--clean", "--strict")

    redirects()

    print()
    print("Done. Output in site/")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    commands = parser.add_subparsers(dest="command", metavar="command")

    commands.add_parser("build", help="build (strict), then write the redirect stubs (default)")
    commands.add_parser("redirects", help="rewrite the redirect stubs only")

    serve_parser = commands.add_parser("serve", help=f"serve on port {PORT}")
    serve_parser.add_argument(
        "--background",
        action="store_true",
        help="return once the server has started, leaving it running",
    )

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if args.command == "redirects":
        redirects()
        return 0

    if args.command == "serve":
        return serve(background=args.background)

    return build()


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode)
