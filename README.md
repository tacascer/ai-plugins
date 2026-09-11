# AI Plugins

This repository contains independently installable agent plugins for Codex and
Claude Code. The first plugin, `testing-principles`, provides shared workflows for
writing, classifying, and auditing tests. Each plugin keeps its manifests, skills,
references, examples, and documentation together under `plugins/<name>/`.

The platform-neutral inventory is `catalogs/plugins.json`. The inventory drives
the committed Codex and Claude marketplace catalogs; `scripts/catalogs.py`
renders both files deterministically. Plugin code and curriculum remain shared
between platforms.

## Local development

Use Python 3.11 or newer and work on a dedicated Git worktree branch. Create a
virtual environment and install the development dependency:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

Run the complete local structural check set from the repository root:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
```

The Python validator checks the repository's supported manifest fields, skill
frontmatter, authored local Markdown links, plugin containment, and generated
catalog drift. It is deliberately narrower than each platform's complete schema.
Use native platform validation as an additional packaging check when that tooling
is available.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the plugin layout, catalog regeneration,
versioning, and authored-content rules.
