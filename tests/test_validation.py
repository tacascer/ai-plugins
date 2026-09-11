import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.catalogs import sync_catalogs
from scripts.validate import validate_repository


SOURCE_ROOT = Path(__file__).resolve().parents[1]
COPY_IGNORES = shutil.ignore_patterns(
    ".git",
    ".venv",
    ".worktrees",
    ".superpowers",
    "__pycache__",
    ".eval-runs",
)


class ValidationTests(unittest.TestCase):
    def copy_repository(self, directory: str) -> Path:
        root = Path(directory) / "repo"
        shutil.copytree(SOURCE_ROOT, root, ignore=COPY_IGNORES)
        return root

    def read_json(self, path: Path) -> object:
        return json.loads(path.read_text(encoding="utf-8"))

    def write_json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def assert_error_contains(self, errors: list[str], text: str) -> None:
        self.assertTrue(any(text in error for error in errors), errors)

    def test_repository_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)

            self.assertEqual(validate_repository(root), [])

    def test_missing_manifest_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            missing = root / "plugins/testing-principles/.codex-plugin/plugin.json"
            missing.unlink()

            errors = validate_repository(root)

            self.assert_error_contains(errors, ".codex-plugin/plugin.json")

    def test_mismatched_manifest_versions_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            manifest_path = root / "plugins/testing-principles/.claude-plugin/plugin.json"
            manifest = self.read_json(manifest_path)
            self.assertIsInstance(manifest, dict)
            manifest["version"] = "0.2.0"
            self.write_json(manifest_path, manifest)

            errors = validate_repository(root)

            self.assert_error_contains(errors, "manifest versions must match")
            self.assert_error_contains(errors, "catalogs/plugins.json")

    def test_required_manifest_metadata_must_be_nonempty(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            manifest_path = root / "plugins/testing-principles/.codex-plugin/plugin.json"
            manifest = self.read_json(manifest_path)
            self.assertIsInstance(manifest, dict)
            manifest["description"] = "   "
            self.write_json(manifest_path, manifest)

            errors = validate_repository(root)

            self.assert_error_contains(errors, "required metadata 'description'")
            self.assert_error_contains(errors, ".codex-plugin/plugin.json")

    def test_duplicate_inventory_entry_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            inventory_path = root / "catalogs/plugins.json"
            inventory = self.read_json(inventory_path)
            self.assertIsInstance(inventory, list)
            inventory.append(inventory[0])
            self.write_json(inventory_path, inventory)

            errors = validate_repository(root)

            self.assert_error_contains(errors, "duplicate plugin name: testing-principles")

    def test_missing_referenced_markdown_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            missing = root / "plugins/testing-principles/references/quality.md"
            missing.unlink()

            errors = validate_repository(root)

            self.assert_error_contains(errors, "references/quality.md")

    def test_decoded_resource_symlink_escape_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            outside = root / "outside.md"
            outside.write_text("outside\n", encoding="utf-8")
            link = root / "plugins/testing-principles/references/escaped resource.md"
            link.symlink_to(outside)
            readme = root / "plugins/testing-principles/README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n[escaped](references/escaped%20resource.md)\n",
                encoding="utf-8",
            )

            errors = validate_repository(root)

            self.assert_error_contains(errors, "escapes plugin directory")
            self.assert_error_contains(errors, "escaped%20resource.md")

    def test_missing_frontmatter_field_is_reported(self) -> None:
        for field in ("name", "description"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root = self.copy_repository(directory)
                skill_path = root / "plugins/testing-principles/skills/audit-tests/SKILL.md"
                lines = skill_path.read_text(encoding="utf-8").splitlines()
                skill_path.write_text(
                    "\n".join(line for line in lines if not line.startswith(f"{field}:"))
                    + "\n",
                    encoding="utf-8",
                )

                errors = validate_repository(root)

                self.assert_error_contains(errors, f"nonempty frontmatter {field}")
                self.assert_error_contains(errors, "skills/audit-tests/SKILL.md")

    def test_malformed_yaml_frontmatter_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            skill_path = root / "plugins/testing-principles/skills/audit-tests/SKILL.md"
            skill_path.write_text(
                "---\nname: [unterminated\ndescription: broken\n---\n",
                encoding="utf-8",
            )

            errors = validate_repository(root)

            self.assert_error_contains(errors, "invalid YAML frontmatter")
            self.assert_error_contains(errors, "skills/audit-tests/SKILL.md")

    def test_stale_catalog_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            catalog = root / ".agents/plugins/marketplace.json"
            catalog.write_text("{}\n", encoding="utf-8")

            errors = validate_repository(root)

            self.assert_error_contains(errors, "stale generated catalog")
            self.assertEqual(catalog.read_text(encoding="utf-8"), "{}\n")

    def test_second_independent_plugin_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            plugin_root = root / "plugins/release-notes"
            shared_manifest = {
                "name": "release-notes",
                "version": "1.2.3-alpha.1",
                "description": "Help write clear release notes.",
                "author": {"name": "Fixture Author"},
                "skills": "./skills/",
            }
            codex_manifest = {
                **shared_manifest,
                "interface": {
                    "displayName": "Release Notes",
                    "shortDescription": "Write release notes.",
                    "longDescription": "Help write clear release notes for a project.",
                    "developerName": "Fixture Author",
                    "category": "Productivity",
                    "capabilities": ["Interactive"],
                    "defaultPrompt": ["Write release notes."],
                },
            }
            self.write_json(plugin_root / ".codex-plugin/plugin.json", codex_manifest)
            self.write_json(plugin_root / ".claude-plugin/plugin.json", shared_manifest)
            (plugin_root / "skills/write-release-notes").mkdir(parents=True)
            (plugin_root / "README.md").write_text(
                "# Release notes\n\nSee [guidance](references/guidance.md).\n",
                encoding="utf-8",
            )
            (plugin_root / "references").mkdir()
            (plugin_root / "references/guidance.md").write_text(
                "# Guidance\n", encoding="utf-8"
            )
            (plugin_root / "skills/write-release-notes/SKILL.md").write_text(
                "---\n"
                "name: write-release-notes\n"
                "description: Use when writing release notes.\n"
                "---\n\n"
                "# Write release notes\n",
                encoding="utf-8",
            )
            inventory_path = root / "catalogs/plugins.json"
            inventory = self.read_json(inventory_path)
            self.assertIsInstance(inventory, list)
            inventory.append(
                {"name": "release-notes", "path": "plugins/release-notes"}
            )
            self.write_json(inventory_path, inventory)
            sync_catalogs(root, check=False)

            self.assertEqual(validate_repository(root), [])

    def test_absolute_local_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            readme = root / "plugins/testing-principles/README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n[absolute](/tmp/resource.md)\n",
                encoding="utf-8",
            )

            errors = validate_repository(root)

            self.assert_error_contains(errors, "absolute local link")

    def test_reference_style_local_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            readme = root / "plugins/testing-principles/README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n[reference][local]\n\n[local]: references/quality.md\n",
                encoding="utf-8",
            )

            errors = validate_repository(root)

            self.assert_error_contains(errors, "reference-style local link")

    def test_multiline_reference_style_local_targets_are_reported(self) -> None:
        cases = (
            ("references/quality.md", "reference-style local link"),
            ("references/missing.md", "missing linked resource"),
            ("/tmp/resource.md", "absolute local link"),
            ("../../outside.md", "escapes plugin directory"),
        )
        for destination, expected in cases:
            with (
                self.subTest(destination=destination),
                tempfile.TemporaryDirectory() as directory,
            ):
                root = self.copy_repository(directory)
                readme = root / "plugins/testing-principles/README.md"
                readme.write_text(
                    readme.read_text(encoding="utf-8")
                    + f"\n[guide]:\n  {destination}\n",
                    encoding="utf-8",
                )

                errors = validate_repository(root)

                self.assert_error_contains(errors, expected)
                self.assert_error_contains(errors, destination)

    def test_skill_name_must_match_its_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            skill_path = root / "plugins/testing-principles/skills/audit-tests/SKILL.md"
            contents = skill_path.read_text(encoding="utf-8")
            skill_path.write_text(
                contents.replace("name: audit-tests", "name: other-name", 1),
                encoding="utf-8",
            )

            errors = validate_repository(root)

            self.assert_error_contains(errors, "skill name must match directory")

    def test_cli_prints_path_specific_errors_and_exits_one(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_repository(directory)
            missing = root / "plugins/testing-principles/references/quality.md"
            missing.unlink()

            result = subprocess.run(
                [sys.executable, "-m", "scripts.validate", "--root", str(root)],
                cwd=SOURCE_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("plugins/testing-principles", result.stderr)
            self.assertIn("references/quality.md", result.stderr)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
