# celbridge-docs

User documentation for Celbridge, the free and open source Python and data
pipeline workbench.

Published via GitHub Pages at:
- https://celbridge-org.github.io/celbridge-docs/

Every push to `main` builds the site and force-pushes the output to the `deploy`
branch, which is what Pages serves. That branch is generated: it carries no
source, and the next build overwrites whatever is on it, so nothing there can be
edited by hand. Anything that has to sit beside the site on the branch lives in
`publish/` and is copied in by the workflow.

The site is built with [Zensical](https://zensical.org) and the Material theme.
It replaced the previous Sphinx build; the content is the same Markdown, and
`zensical.toml` now does the job `docs/conf.py` used to.

## Build it locally

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install zensical==0.0.55

zensical serve                     # http://localhost:8000, live reload
zensical build --clean --strict    # -> site/
```

`--strict` fails the build on a broken internal link. Keep it on: it is what
the publish workflow runs, so a broken link fails the run rather than publishing a
site with holes in it.

## This repo is a Celbridge project - you can build the docs in Celbridge :-)

Open `docs.console`. It is a Python console that installs Zensical into its own
environment, and it carries two toolbar shortcuts:

- **Build** runs `build.ipy` - a strict build into `site/`, then the redirect
  stubs.
- **Serve** runs `serve.ipy` - a live preview on http://localhost:8000. Open
  `site_preview.webview` beside it to read the site inside Celbridge.

The dependency and the shortcuts are declared in `docs.console` itself, so there
is nothing to install by hand beyond opening the project.

## Layout

```
zensical.toml            site config, theme and navigation
docs/                    the documentation itself
  index.md               landing page
  01_about/ 02_setup/ 03_getting_started/ 08_use_cases/
  images/                shared screenshots
  _static/css/           stylesheet and self-hosted fonts
redirects.csv            old Sphinx URL -> its replacement
scripts/                 post-build steps (Zensical has no plugin API)
publish/                 files copied to the deploy branch beside the site
docs.console             the Celbridge console: Zensical, and the two shortcuts
site_preview.webview     the built site, read inside Celbridge
site/                    build output, gitignored
.github/workflows/       build and publish to the deploy branch on a push to main
```

## The old URLs

Sphinx published `/page.html` and Zensical publishes `/page/`, so every page URL
changed with the generator. A static host cannot serve a 301, so
`scripts/gen_redirect_stubs.py` writes a small redirecting HTML file at each old
URL after the build - a `<meta http-equiv="refresh">`, a `rel="canonical"` at the
new URL, and a line of script that carries the `#fragment` across. The section
index pages are not in the list: `/section/index.html` is what a directory URL
serves anyway, so those never broke.

`redirects.csv` records what the Sphinx site published. It is history, not a view
of the current docs - do not regenerate it from the docs tree. Renaming a page
adds a row and keeps the old one. The script fails the build if a redirect points
at a page that no longer exists, or if one would shadow a real page.

## Editing

- **Adding a page** - a Markdown file under `docs/`, plus an entry in the `nav`
  array in `zensical.toml`. A page missing from `nav` is built but unreachable.
- **Navigation and section headings** - the `nav` array in `zensical.toml`.
- **Images** - page-relative paths (`../images/x.png`), never docs-root-absolute
  (`/images/x.png`). Zensical resolves a leading `/` against the site root, so
  the absolute form breaks as soon as the docs are served under a subpath.
- **Colour, type, spacing** - `docs/_static/css/celbridge.css`.



