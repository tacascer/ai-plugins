# AI Plugins

This repository contains independently installable agent plugins for Codex and
Claude Code. Available packages are:

- [Testing Principles](plugins/testing-principles/README.md): design testable code, classify tests, and audit tests.
- [Time Modeling](plugins/time-modeling/README.md): design and audit temporal data models.
- [Logging Principles](plugins/logging-principles/README.md): design and audit purposeful logging and failure reporting.

Each plugin keeps its manifests, skills, references, examples, and documentation
together under `plugins/<name>/`.

The platform-neutral inventory is `catalogs/plugins.json`. The inventory drives
the committed Codex and Claude marketplace catalogs; `scripts/catalogs.py`
renders both files deterministically. Plugin code and curriculum remain shared
between platforms.

## Install or load locally

Before publication, use an absolute path to a local checkout. Claude Code can
load the plugin for one session without installing it:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/testing-principles
```

The session-only loader was verified with Claude Code 2.1.267. To inspect what it
loaded without starting a model turn:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/testing-principles \
  plugin details testing-principles@inline
```

Codex 0.154.0 can inspect the local catalog without installing it:

```bash
codex \
  -c 'marketplaces.tacascer-ai-plugins={source_type="local",source="/absolute/path/to/ai-plugins"}' \
  plugin list --json --marketplace tacascer-ai-plugins --available
```

Codex does not expose a session-only raw plugin-directory loader in that version.
Local activation therefore uses the normal marketplace and installation commands,
which update Codex's user plugin configuration and cache:

```bash
codex plugin marketplace add /absolute/path/to/ai-plugins
codex plugin add testing-principles@tacascer-ai-plugins
```

These remote commands are for use only after this repository has been published
at `tacascer/ai-plugins`:

```bash
codex plugin marketplace add tacascer/ai-plugins
codex plugin add testing-principles@tacascer-ai-plugins

claude plugin marketplace add tacascer/ai-plugins
claude plugin install testing-principles@tacascer-ai-plugins
```

The commands above document the supported flows. This repository's verification
did not install or publish the plugin.

## Use a workflow

The platforms use each installed or session-loaded skill's description for
automatic selection when a request matches. Live automatic-selection behavior is
still awaiting the model checks recorded below. To request a specific workflow
explicitly, use the platform-qualified name:

```text
# Codex
$testing-principles:classify-tests classify these tests

# Claude Code
/testing-principles:classify-tests classify these tests
```

Replace `classify-tests` with `audit-tests` or `design-for-testing` as needed. For Time
Modeling, use `$time-modeling:design-time-models` or
`$time-modeling:audit-time-models` in Codex, and the corresponding `/` forms in
Claude Code. For Logging Principles, use `$logging-principles:design-logging` or
`$logging-principles:audit-logging` in Codex, and
`/logging-principles:design-logging` or `/logging-principles:audit-logging` in
Claude Code. Load or install the selected plugin using its own directory or
package name in the commands above.

Start a fresh session after installing or updating a plugin so the platform
reloads its skills. See the [Testing Principles verification record](docs/verification/2026-09-11-initial.md)
and [Time Modeling verification record](plugins/time-modeling/docs/verification/2026-09-17-initial.md)
for the exact checks, versions, and outstanding model-behavior validation.

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
