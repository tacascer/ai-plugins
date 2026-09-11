"""Render reproducible Codex and Claude plugin catalogs from an inventory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CATALOG_NAME = "tacascer-ai-plugins"
PLUGIN_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(
    r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
OUTPUT_PATHS = (
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
)


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"missing required file: {path}") from error
    except UnicodeDecodeError as error:
        raise ValueError(f"invalid UTF-8 in {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {path}: {error.msg}") from error


def _load_inventory(root: Path) -> list[dict[str, str]]:
    inventory_path = root / "catalogs/plugins.json"
    inventory = _load_json(inventory_path)
    if not isinstance(inventory, list):
        raise ValueError(f"inventory must be a JSON array: {inventory_path}")

    plugins: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, entry in enumerate(inventory):
        if not isinstance(entry, dict):
            raise ValueError(f"inventory entry {index} must be an object")
        name = entry.get("name")
        source_path = entry.get("path")
        if not isinstance(name, str) or not PLUGIN_NAME_PATTERN.fullmatch(name):
            raise ValueError(f"invalid plugin name at inventory entry {index}: {name!r}")
        if name in seen:
            raise ValueError(f"duplicate plugin name: {name}")
        expected_path = f"plugins/{name}"
        if source_path != expected_path:
            raise ValueError(
                f"invalid source path for {name}: expected {expected_path}, got {source_path!r}"
            )
        seen.add(name)
        plugins.append({"name": name, "path": source_path})
    return plugins


def _load_manifests(root: Path, plugin: dict[str, str]) -> tuple[dict, dict]:
    name = plugin["name"]
    plugin_root = root / plugin["path"]
    codex = _load_json(plugin_root / ".codex-plugin/plugin.json")
    claude = _load_json(plugin_root / ".claude-plugin/plugin.json")
    if not isinstance(codex, dict) or not isinstance(claude, dict):
        raise ValueError(f"plugin manifests must be JSON objects: {name}")
    if codex.get("name") != name:
        raise ValueError(f"Codex manifest name must match inventory name: {name}")
    if claude.get("name") != name:
        raise ValueError(f"Claude manifest name must match inventory name: {name}")
    codex_version = codex.get("version")
    claude_version = claude.get("version")
    if not isinstance(codex_version, str) or codex_version != claude_version:
        raise ValueError(f"manifest versions must match for plugin: {name}")
    if not SEMVER_PATTERN.fullmatch(codex_version):
        raise ValueError(f"manifest version must be strict SemVer for plugin: {name}")
    description = claude.get("description")
    if not isinstance(description, str) or not description:
        raise ValueError(f"Claude manifest description is required: {name}")
    return codex, claude


def render_catalogs(root: Path) -> dict[str, dict]:
    """Build both marketplace payloads without writing to disk."""
    codex_plugins = []
    claude_plugins = []
    for plugin in _load_inventory(root):
        codex_manifest, claude_manifest = _load_manifests(root, plugin)
        name = plugin["name"]
        source = f"./plugins/{name}"
        codex_plugins.append(
            {
                "name": name,
                "source": {"source": "local", "path": source},
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Productivity",
            }
        )
        claude_plugins.append(
            {
                "name": name,
                "source": source,
                "version": codex_manifest["version"],
                "description": claude_manifest["description"],
            }
        )

    return {
        OUTPUT_PATHS[0]: {
            "name": CATALOG_NAME,
            "interface": {"displayName": "tacascer AI Plugins"},
            "plugins": codex_plugins,
        },
        OUTPUT_PATHS[1]: {
            "name": CATALOG_NAME,
            "owner": {"name": "tacascer"},
            "description": "Independent agent workflow plugins for Codex and Claude Code.",
            "plugins": claude_plugins,
        },
    }


def sync_catalogs(root: Path, check: bool) -> list[str]:
    """Write catalogs, or report missing and stale outputs in check mode."""
    errors = []
    for relative_path, payload in render_catalogs(root).items():
        output_path = root / relative_path
        expected = (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode()
        if check:
            if not output_path.exists():
                errors.append(f"missing generated catalog: {relative_path}")
            elif output_path.read_bytes() != expected:
                errors.append(f"stale generated catalog: {relative_path}")
            continue
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(expected)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    root = args.root if args.root is not None else Path(__file__).resolve().parents[1]
    try:
        errors = sync_catalogs(root.resolve(), check=args.check)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
