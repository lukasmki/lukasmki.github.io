"""Emit the GitHub Actions matrix for hosted project docs.

Reads hosted-docs.toml and prints ``matrix=<json>`` for $GITHUB_OUTPUT.
"""

import json
import sys
import tomllib
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[2] / "hosted-docs.toml"
DEFAULTS = {
    "ref": "",
    "workdir": "docs",
    "build": 'uv run --frozen sphinx-build -b html source "$OUT"',
}
# Paths the main Sphinx site already uses at its root.
RESERVED = {"genindex", "search", "index", "searchindex", "objects"}


def main() -> None:
    config = tomllib.loads(CONFIG.read_text())
    entries = []
    seen = set()
    for repo in config.get("repo", []):
        entry = DEFAULTS | repo
        name = entry["repo"].split("/")[-1]
        if name in seen:
            sys.exit(f"duplicate repo name: {name}")
        if name.startswith("_") or name.lower() in RESERVED:
            sys.exit(f"repo name clashes with a site path: {name}")
        seen.add(name)
        entries.append({"name": name, **entry})
    print(f"matrix={json.dumps(entries)}")


if __name__ == "__main__":
    main()
