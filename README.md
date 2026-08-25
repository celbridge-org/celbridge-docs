# celbridge-docs

User documentation for Celbridge, the free and open source Python and data
pipeline workbench.

Published via GitHub Pages at:
- https://celbridge-org.github.io/celbridge-docs/

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
the GitHub Actions workflow runs, so a broken link fails the run rather than
publishing a site with holes in it.

## This repo is a Celbridge project - you can build the docs in Celbridge :-)

The two console shortcuts in `celbridge-docs.celbridge` do the same two things:

- **serve** runs `serve.ipy` - a live preview on http://localhost:8000. Open
  `web_view.webapp` beside it to read the site inside Celbridge.
- **build** runs `build.ipy` - a one-off strict build into `site/`.

Both use the project's own Python environment, so there is nothing to install
by hand beyond opening the project.

## Layout

```
zensical.toml            site config, theme and navigation
docs/                    the documentation itself
  index.md               landing page
  01_about/ 02_setup/ 03_getting_started/ 08_use_cases/ 09_community/
  images/                shared screenshots
  _static/css/           stylesheet and self-hosted fonts
site/                    build output, gitignored
.github/workflows/       build and deploy to GitHub Pages on a push to main
```

## Editing

- **Adding a page** - a Markdown file under `docs/`, plus an entry in the `nav`
  array in `zensical.toml`. A page missing from `nav` is built but unreachable.
- **Navigation and section headings** - the `nav` array in `zensical.toml`.
- **Images** - page-relative paths (`../images/x.png`), never docs-root-absolute
  (`/images/x.png`). Zensical resolves a leading `/` against the site root, so
  the absolute form breaks as soon as the docs are served under a subpath.
- **Colour, type, spacing** - `docs/_static/css/celbridge.css`.
