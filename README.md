# lukasmki.github.io

Personal site built with [Sphinx](https://www.sphinx-doc.org/) and the [Furo](https://github.com/pradyunsg/furo) theme, published at <https://lukasmki.github.io/>.

## Local development

```sh
uv sync
uv run make html        # output in build/html
open build/html/index.html
```

Pages live in `source/` as reStructuredText; add new pages to the `toctree` in `source/index.rst`.

## Deployment

Pushing to `main` runs `.github/workflows/pages.yml`, which builds the site and deploys it to GitHub Pages.

## Hosting project docs

Repos listed in `hosted-docs.toml` are cloned, built, and published at `https://lukasmki.github.io/<repo name>/`. To add one:

```toml
[[repo]]
repo = "lukasmki/some-project"
# Optional (defaults shown):
# ref     = ""        # branch, tag, or sha; empty = default branch
# workdir = "docs"    # directory the build runs in
# build   = 'uv run --frozen sphinx-build -b html source "$OUT"'
```

The build command runs in `workdir` and must write HTML to `$OUT`. If any project build fails, nothing is deployed and the last good site stays live.

Docs are rebuilt on every push here, nightly, and on demand from the Actions tab.

**Private repos** need a fine-grained personal access token with read access to *Contents* on those repos, saved in this repo as the `DOCS_TOKEN` Actions secret. Their built docs are public.

**Rebuild on push to a project repo (optional).** Add a token that can trigger workflows here (fine-grained PAT on `lukasmki.github.io` with *Contents: read and write*) to the project repo as `PAGES_DISPATCH_TOKEN`, then add this workflow to the project repo:

```yaml
name: Rebuild hosted docs
on:
  push:
    branches: [main]
    paths: [docs/**, src/**]
jobs:
  dispatch:
    runs-on: ubuntu-latest
    steps:
      - run: gh api repos/lukasmki/lukasmki.github.io/dispatches -f event_type=docs-updated
        env:
          GH_TOKEN: ${{ secrets.PAGES_DISPATCH_TOKEN }}
```
