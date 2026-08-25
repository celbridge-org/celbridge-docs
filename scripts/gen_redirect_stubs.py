"""Write redirect stubs into the built site for the old Sphinx URLs.

Sphinx published /page.html and Zensical publishes /page/, so every page URL
changed when the generator did. GitHub Pages cannot serve a 301, so each old
URL gets a small HTML file that redirects to its replacement and names it as
the canonical one. Run after `zensical build`, before the output is deployed.
"""

import csv
import json
import posixpath
import sys
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "zensical.toml"
REDIRECTS_FILE = REPO_ROOT / "redirects.csv"
SITE_FOLDER = REPO_ROOT / "site"

STUB_MARKER = "<!-- celbridge-redirect-stub -->"

STUB_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    """ + STUB_MARKER + """
    <meta charset="utf-8">
    <title>Redirecting - Celbridge Docs</title>
    <link rel="canonical" href="{canonical_url}">
    <meta http-equiv="refresh" content="0; url={relative_url}">
    <script>
      // Carries the fragment across, which the meta refresh on its own drops.
      location.replace({relative_url_literal} + location.hash);
    </script>
  </head>
  <body>
    <p>This page has moved to <a href="{relative_url}">{canonical_url}</a>.</p>
  </body>
</html>
"""


def read_site_url() -> str:
    with CONFIG_FILE.open("rb") as config_file:
        config = tomllib.load(config_file)

    site_url = config["project"]["site_url"]

    return site_url.rstrip("/")


def read_redirects() -> list[tuple[str, str]]:
    redirects = []

    with REDIRECTS_FILE.open(newline="", encoding="utf-8") as redirects_file:
        rows = (line for line in redirects_file if not line.startswith("#"))
        for row in csv.DictReader(rows):
            redirects.append((row["old_url"].strip(), row["new_url"].strip()))

    return redirects


def resolve_target(new_url: str) -> Path:
    """The file in the built site that a redirect destination resolves to."""
    relative_path = new_url.lstrip("/")
    if new_url.endswith("/"):
        return SITE_FOLDER / relative_path / "index.html"

    return SITE_FOLDER / relative_path


def relative_url(old_url: str, new_url: str) -> str:
    """The destination as an href from the stub's own location.

    Site-root-relative would break: the site is served from a subpath.
    """
    start_folder = posixpath.dirname(old_url)
    relative = posixpath.relpath(new_url, start_folder)
    if new_url.endswith("/"):
        relative += "/"

    return relative


def main() -> int:
    if not SITE_FOLDER.is_dir():
        print(f"error: {SITE_FOLDER} does not exist - run zensical build first")
        return 1

    site_url = read_site_url()
    redirects = read_redirects()
    errors = []

    for old_url, new_url in redirects:
        if not old_url.endswith(".html"):
            errors.append(f"{old_url}: an old URL must be a .html page")
            continue

        stub_path = SITE_FOLDER / old_url.lstrip("/")
        if stub_path.exists():
            # A stub from an earlier run is ours to replace; anything else is a
            # real page, and redirecting away from it would lose it.
            existing = stub_path.read_text(encoding="utf-8")
            if STUB_MARKER not in existing:
                errors.append(f"{old_url}: the build already publishes this page")
                continue

        target_path = resolve_target(new_url)
        if not target_path.exists():
            errors.append(f"{old_url} -> {new_url}: the destination does not exist")
            continue

        stub = STUB_TEMPLATE.format(
            canonical_url=site_url + new_url,
            relative_url=relative_url(old_url, new_url),
            relative_url_literal=json.dumps(relative_url(old_url, new_url)),
        )

        stub_path.parent.mkdir(parents=True, exist_ok=True)
        stub_path.write_text(stub, encoding="utf-8")

    if errors:
        print(f"{len(errors)} redirect(s) could not be written:")
        for error in errors:
            print(f"  {error}")
        return 1

    print(f"Wrote {len(redirects)} redirect stubs into {SITE_FOLDER.name}/")

    return 0


if __name__ == "__main__":
    sys.exit(main())
