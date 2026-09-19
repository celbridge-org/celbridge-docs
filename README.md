# celbridge-docs

User documentation for Celbridge, the free and open source Python and data
pipeline workbench.

Published at:
- https://learn.celbridge.org/ - the public site
- https://celbridge-org.github.io/celbridge-docs/ - the same build, on Pages

Every push to `main` builds the site and force-pushes the output to the `deploy`
branch, which both hosts serve: GitHub Pages from the branch itself, and a
Cloudflare Worker behind the custom domain (`publish/wrangler.jsonc`). One build
feeds both, so they never differ. `site_url` in `zensical.toml` names
learn.celbridge.org, which is what the canonical links and the sitemap point at
on both copies. That branch is generated: it carries no source, and the next
build overwrites whatever is on it, so nothing there can be edited by hand.
Anything that has to sit beside the site on the branch lives in `publish/` and
is copied in by the workflow.

The site is built with [Zensical](https://zensical.org) and the Material theme.
It replaced the previous Sphinx build; the content is the same Markdown, and
`zensical.toml` now does the job `docs/conf.py` used to.



## Build it locally

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install zensical==0.0.55

python build.py                    # strict build into site/, then redirect stubs
python build.py serve              # http://localhost:8000, live reload
python build.py redirects          # rewrite the redirect stubs only
```

`build.py` is the one build path: the Celbridge console below and the publish
workflow both run this same script. It runs everything with the Python that runs
it, so whichever environment you start it from is the one that builds.

`--strict` fails the build on a broken internal link. Keep it on: it is what
the publish workflow runs, so a broken link fails the run rather than publishing a
site with holes in it.

## This repo is a Celbridge project - you can build the docs in Celbridge :-)

Two buttons on the Utility bar open the documents that drive the local build and
preview, and both open with the project. The console declares its own Zensical
dependency, so there is nothing to install by hand.

1. `site.console` (terminal icon, bottom panel)
   - a Python console that runs `run build.py serve --background` as soon as it
     opens: the server starts, and the console stays free to take commands
   - a **Build** shortcut (hammer icon) runs `run build.py`: a strict build into
     `site/`, then the redirect stubs
   - editing `redirects.csv` rewrites the stubs on its own

2. `celbridge.webview` (window icon, side panel)
   - the preview, at http://localhost:8000/

`claude.console` opens a shell console running Claude Code, for working on the
docs with an agent.

### Typical editing workflow

1. open the project in Celbridge - the console and the preview open with it, and
   the server is already running
2. edit content under `docs/`
3. click the hammer in the console to rebuild
4. read the updated pages in the side panel preview
5. repeat from step 2 for more edits
6. `git add/commit/push` when done - the push to `main` publishes the site
7. check the live site at https://learn.celbridge.org/

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
build.py                 the build: strict build, then the redirect stubs
site.console             Celbridge: the preview server and the Build shortcut
celbridge.webview        Celbridge: the preview, read beside the editor
claude.console           Celbridge: a shell console running Claude Code
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

