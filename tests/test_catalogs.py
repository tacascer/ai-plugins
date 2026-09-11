import json
import tempfile
import unittest
from pathlib import Path

from scripts.catalogs import render_catalogs, sync_catalogs


class CatalogTests(unittest.TestCase):
    def write_plugin(
        self,
        root: Path,
        name: str,
        *,
        codex_name: str | None = None,
        claude_name: str | None = None,
        codex_version: str = "0.1.0",
        claude_version: str = "0.1.0",
    ) -> None:
        manifests = {
            "codex": {
                "name": codex_name or name,
                "version": codex_version,
                "description": f"{name} fixture",
                "author": {"name": "tacascer"},
            },
            "claude": {
                "name": claude_name or name,
                "version": claude_version,
                "description": f"{name} fixture",
                "author": {"name": "tacascer"},
            },
        }
        for platform, manifest in manifests.items():
            path = root / f"plugins/{name}/.{platform}-plugin/plugin.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(manifest), encoding="utf-8")

    def write_inventory(self, root: Path, inventory: list[dict[str, str]]) -> None:
        path = root / "catalogs/plugins.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(inventory), encoding="utf-8")

    def test_two_plugins_keep_order_and_platform_source_shapes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inventory = []
            for name in ("alpha", "beta"):
                inventory.append({"name": name, "path": f"plugins/{name}"})
                self.write_plugin(root, name)
            self.write_inventory(root, inventory)

            catalogs = render_catalogs(root)

            self.assertEqual(
                list(catalogs),
                [
                    ".agents/plugins/marketplace.json",
                    ".claude-plugin/marketplace.json",
                ],
            )
            codex = catalogs[".agents/plugins/marketplace.json"]
            claude = catalogs[".claude-plugin/marketplace.json"]
            self.assertEqual(codex["name"], "tacascer-ai-plugins")
            self.assertEqual(codex["interface"], {"displayName": "tacascer AI Plugins"})
            self.assertEqual([plugin["name"] for plugin in codex["plugins"]], ["alpha", "beta"])
            self.assertEqual(
                codex["plugins"][1],
                {
                    "name": "beta",
                    "source": {"source": "local", "path": "./plugins/beta"},
                    "policy": {
                        "installation": "AVAILABLE",
                        "authentication": "ON_INSTALL",
                    },
                    "category": "Productivity",
                },
            )
            self.assertEqual(
                claude,
                {
                    "name": "tacascer-ai-plugins",
                    "owner": {"name": "tacascer"},
                    "description": "Independent agent workflow plugins for Codex and Claude Code.",
                    "plugins": [
                        {
                            "name": "alpha",
                            "source": "./plugins/alpha",
                            "version": "0.1.0",
                            "description": "alpha fixture",
                        },
                        {
                            "name": "beta",
                            "source": "./plugins/beta",
                            "version": "0.1.0",
                            "description": "beta fixture",
                        },
                    ],
                },
            )

            stale_errors = sync_catalogs(root, check=True)
            self.assertEqual(len(stale_errors), 2)
            self.assertFalse((root / ".agents").exists())
            self.assertFalse((root / ".claude-plugin").exists())
            self.assertEqual(sync_catalogs(root, check=False), [])
            self.assertEqual(sync_catalogs(root, check=True), [])
            for relative_path, payload in catalogs.items():
                expected = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
                self.assertEqual(
                    (root / relative_path).read_text(encoding="utf-8"), expected
                )

    def test_duplicate_names_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_plugin(root, "alpha")
            self.write_inventory(
                root,
                [
                    {"name": "alpha", "path": "plugins/alpha"},
                    {"name": "alpha", "path": "plugins/alpha"},
                ],
            )

            with self.assertRaisesRegex(ValueError, "duplicate plugin name: alpha"):
                render_catalogs(root)

    def test_source_paths_cannot_escape_or_disagree_with_name(self) -> None:
        invalid_paths = ("../alpha", "plugins/../alpha", "plugins/beta")
        for invalid_path in invalid_paths:
            with self.subTest(path=invalid_path), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_plugin(root, "alpha")
                self.write_inventory(
                    root, [{"name": "alpha", "path": invalid_path}]
                )

                with self.assertRaisesRegex(ValueError, "expected plugins/alpha"):
                    render_catalogs(root)

    def test_names_must_be_lowercase_hyphenated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_inventory(
                root, [{"name": "Alpha_Plugin", "path": "plugins/Alpha_Plugin"}]
            )

            with self.assertRaisesRegex(ValueError, "invalid plugin name"):
                render_catalogs(root)

    def test_manifest_identity_and_versions_must_match(self) -> None:
        cases = (
            ({"codex_name": "other"}, "Codex manifest name"),
            ({"claude_name": "other"}, "Claude manifest name"),
            ({"claude_version": "0.2.0"}, "manifest versions"),
        )
        for overrides, message in cases:
            with self.subTest(overrides=overrides), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_plugin(root, "alpha", **overrides)
                self.write_inventory(
                    root, [{"name": "alpha", "path": "plugins/alpha"}]
                )

                with self.assertRaisesRegex(ValueError, message):
                    render_catalogs(root)

    def test_check_mode_does_not_replace_stale_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_plugin(root, "alpha")
            self.write_inventory(root, [{"name": "alpha", "path": "plugins/alpha"}])
            output = root / ".agents/plugins/marketplace.json"
            output.parent.mkdir(parents=True)
            output.write_text("stale\n", encoding="utf-8")

            errors = sync_catalogs(root, check=True)

            self.assertTrue(any("stale" in error for error in errors))
            self.assertEqual(output.read_text(encoding="utf-8"), "stale\n")
            self.assertFalse((root / ".claude-plugin").exists())


if __name__ == "__main__":
    unittest.main()
