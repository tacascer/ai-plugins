"""Validate repository-owned plugin packaging and authored resources."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

from scripts.catalogs import render_catalogs, sync_catalogs


INLINE_LINK_PATTERN = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
REFERENCE_DEFINITION_PATTERN = re.compile(
    r"^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*(?:\n[ \t]+)?(\S+)", re.MULTILINE
)
QUALIFIED_WORKFLOW_PATTERN = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*:[a-z0-9]+(?:-[a-z0-9]+)*$"
)


def _display_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _is_within(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
    except ValueError:
        return False
    return True


def _read_json_mapping(path: Path, root: Path, errors: list[str]) -> dict | None:
    label = _display_path(path, root)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{label}: missing required file")
        return None
    except UnicodeDecodeError:
        errors.append(f"{label}: invalid UTF-8")
        return None
    except json.JSONDecodeError as error:
        errors.append(f"{label}: invalid JSON: {error.msg}")
        return None
    if not isinstance(payload, dict):
        errors.append(f"{label}: JSON value must be an object")
        return None
    return payload


def _validate_manifest_metadata(plugin_root: Path, root: Path) -> list[str]:
    errors: list[str] = []
    for platform in ("codex", "claude"):
        path = plugin_root / f".{platform}-plugin/plugin.json"
        manifest = _read_json_mapping(path, root, errors)
        if manifest is None:
            continue
        for field in ("name", "version", "description"):
            value = manifest.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{_display_path(path, root)}: required metadata {field!r} "
                    "must be a nonempty string"
                )
    readme = plugin_root / "README.md"
    if not readme.is_file():
        errors.append(f"{_display_path(readme, root)}: missing plugin documentation")
    return errors


def _frontmatter(document: str) -> str | None:
    lines = document.splitlines()
    if not lines or lines[0] != "---":
        return None
    for index, line in enumerate(lines[1:], start=1):
        if line == "---":
            return "\n".join(lines[1:index])
    return None


def _validate_skill(skill_path: Path, plugin_root: Path, root: Path) -> list[str]:
    errors: list[str] = []
    label = _display_path(skill_path, root)
    if not _is_within(skill_path.resolve(), plugin_root.resolve()):
        return [f"{label}: skill file escapes plugin directory through a symlink"]
    try:
        document = skill_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"{label}: missing SKILL.md"]
    except UnicodeDecodeError:
        return [f"{label}: invalid UTF-8"]
    source = _frontmatter(document)
    if source is None:
        return [f"{label}: missing or unterminated YAML frontmatter"]
    try:
        metadata = yaml.safe_load(source)
    except yaml.YAMLError as error:
        problem = getattr(error, "problem", None) or "could not parse YAML"
        return [f"{label}: invalid YAML frontmatter: {problem}"]
    if not isinstance(metadata, dict):
        return [f"{label}: YAML frontmatter must be a mapping"]
    for field in ("name", "description"):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: expected nonempty frontmatter {field}")
    name = metadata.get("name")
    if isinstance(name, str) and name.strip() and name != skill_path.parent.name:
        errors.append(
            f"{label}: skill name must match directory {skill_path.parent.name!r}"
        )
    return errors


def _link_destination(raw_destination: str) -> str:
    destination = raw_destination.strip()
    if destination.startswith("<") and ">" in destination:
        return destination[1 : destination.index(">")]
    return destination.split(maxsplit=1)[0]


def _is_remote_https(destination: str) -> bool:
    return urlsplit(destination).scheme.lower() == "https"


def _validate_local_destination(
    raw_destination: str,
    document_path: Path,
    plugin_root: Path,
    root: Path,
) -> str | None:
    destination = _link_destination(raw_destination)
    if not destination or destination.startswith("#") or _is_remote_https(destination):
        return None
    decoded = unquote(destination)
    parsed = urlsplit(decoded)
    label = _display_path(document_path, root)
    if parsed.scheme or parsed.netloc:
        return f"{label}: unsupported non-HTTPS link: {destination}"
    local_path = Path(parsed.path)
    if local_path.is_absolute():
        return f"{label}: absolute local link is not allowed: {destination}"
    target = document_path.parent / local_path
    resolved_plugin = plugin_root.resolve()
    resolved_target = target.resolve()
    if not _is_within(resolved_target, resolved_plugin):
        return f"{label}: link escapes plugin directory: {destination}"
    if not target.exists():
        return f"{label}: missing linked resource: {destination}"
    return None


def _validate_markdown(document_path: Path, plugin_root: Path, root: Path) -> list[str]:
    label = _display_path(document_path, root)
    if not _is_within(document_path.resolve(), plugin_root.resolve()):
        return [f"{label}: Markdown file escapes plugin directory through a symlink"]
    try:
        document = document_path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return [f"{label}: could not read Markdown file"]
    except UnicodeDecodeError:
        return [f"{label}: invalid UTF-8"]

    errors: list[str] = []
    for match in INLINE_LINK_PATTERN.finditer(document):
        error = _validate_local_destination(
            match.group(1), document_path, plugin_root, root
        )
        if error is not None:
            errors.append(error)
    for match in REFERENCE_DEFINITION_PATTERN.finditer(document):
        destination = _link_destination(match.group(1))
        if (
            destination
            and not destination.startswith("#")
            and not _is_remote_https(destination)
        ):
            error = _validate_local_destination(
                destination, document_path, plugin_root, root
            )
            if error is not None:
                errors.append(error)
            else:
                errors.append(
                    f"{label}: reference-style local link is not supported: "
                    f"{destination}"
                )
    return errors


def _validate_bundle_containment(plugin_root: Path, root: Path) -> list[str]:
    label = _display_path(plugin_root, root)
    try:
        resolved_plugin = plugin_root.resolve()
    except (OSError, RuntimeError) as error:
        return [f"{label}: could not resolve plugin directory: {error}"]
    if not _is_within(resolved_plugin, root):
        return [f"{label}: plugin directory escapes collection root through a symlink"]

    errors: list[str] = []
    pending = [plugin_root]
    while pending:
        directory = pending.pop()
        try:
            entries = list(directory.iterdir())
        except (FileNotFoundError, NotADirectoryError):
            continue
        except OSError as error:
            errors.append(
                f"{_display_path(directory, root)}: could not inspect plugin directory: "
                f"{error}"
            )
            continue
        for entry in entries:
            if entry.is_symlink():
                try:
                    resolved_target = entry.resolve()
                except (OSError, RuntimeError) as error:
                    errors.append(
                        f"{_display_path(entry, root)}: could not resolve symlink: {error}"
                    )
                    continue
                if not _is_within(resolved_target, resolved_plugin):
                    errors.append(
                        f"{_display_path(entry, root)}: symlink target escapes plugin "
                        "directory"
                    )
                continue
            if entry.is_dir():
                pending.append(entry)
    return errors


def _inventory_plugin_roots(root: Path) -> list[Path]:
    inventory_path = root / "catalogs/plugins.json"
    try:
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, UnicodeDecodeError, json.JSONDecodeError):
        return []
    if not isinstance(inventory, list):
        return []
    return [
        root / entry["path"]
        for entry in inventory
        if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    ]


def _validate_eval_activation_identities(
    plugin_root: Path, root: Path
) -> list[str]:
    cases_path = plugin_root / "evals/cases.json"
    if not cases_path.is_file():
        return []
    try:
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return []
    if not isinstance(cases, list):
        return []

    errors: list[str] = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            continue
        expected = case.get("expected_activation")
        if not isinstance(expected, list):
            continue
        case_id = case.get("id", f"case at index {index}")
        for identity in expected:
            if (
                not isinstance(identity, str)
                or QUALIFIED_WORKFLOW_PATTERN.fullmatch(identity) is None
            ):
                errors.append(
                    f"{_display_path(cases_path, root)}: {case_id}: "
                    "expected_activation identity must be plugin-qualified: "
                    f"{identity!r}"
                )
    return errors


def _validate_plugin(plugin_root: Path, root: Path) -> list[str]:
    errors = _validate_manifest_metadata(plugin_root, root)
    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        errors.append(
            f"{_display_path(skills_root, root)}: missing plugin skills directory"
        )
    else:
        skill_directories = sorted(path for path in skills_root.iterdir() if path.is_dir())
        if not skill_directories:
            errors.append(f"{_display_path(skills_root, root)}: no skills found")
        for skill_directory in skill_directories:
            errors.extend(
                _validate_skill(skill_directory / "SKILL.md", plugin_root, root)
            )
    for document_path in sorted(plugin_root.rglob("*.md")):
        errors.extend(_validate_markdown(document_path, plugin_root, root))
    errors.extend(_validate_eval_activation_identities(plugin_root, root))
    return errors


def validate_repository(root: Path) -> list[str]:
    """Return path-specific errors for repository plugin packaging."""
    root = root.resolve()
    containment_errors: list[str] = []
    for plugin_root in _inventory_plugin_roots(root):
        containment_errors.extend(_validate_bundle_containment(plugin_root, root))
    if containment_errors:
        return containment_errors
    try:
        catalogs = render_catalogs(root)
    except ValueError as error:
        return [f"catalogs/plugins.json: {error}"]

    errors: list[str] = []
    codex_catalog = catalogs[".agents/plugins/marketplace.json"]
    for plugin in codex_catalog["plugins"]:
        plugin_root = root / plugin["source"]["path"]
        errors.extend(_validate_plugin(plugin_root, root))
    try:
        errors.extend(sync_catalogs(root, check=True))
    except (OSError, ValueError) as error:
        errors.append(str(error))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args(argv)
    root = args.root if args.root is not None else Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
