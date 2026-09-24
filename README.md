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
