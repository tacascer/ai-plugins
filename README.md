# AI Plugins

[Tim skills](plugins/tim-skills/README.md) is one shared plugin for Codex and
Claude Code. It contains 15 workflows covering testing, time modeling,
observability, domain-driven design, Rust patterns, and GraphQL contracts.

The package lives in `plugins/tim-skills/`. Skills, references, examples,
evaluations, and documentation are shared between platforms. The inventory in
`catalogs/plugins.json` drives both committed marketplace catalogs.

## Install or load locally

Use an absolute path to your checkout. Claude Code can load the complete plugin
for one session without installing it:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/tim-skills
```

Inspect that session's package without starting a model turn:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/tim-skills \
  plugin details tim-skills@inline
```

Codex can inspect the local catalog without installing it:

```bash
codex \
  -c 'marketplaces.tacascer-ai-plugins={source_type="local",source="/absolute/path/to/ai-plugins"}' \
  plugin list --json --marketplace tacascer-ai-plugins --available
```

For local installation, these commands update user plugin configuration and
caches:

```bash
codex plugin marketplace add /absolute/path/to/ai-plugins
codex plugin add tim-skills@tacascer-ai-plugins

claude plugin marketplace add /absolute/path/to/ai-plugins
claude plugin install tim-skills@tacascer-ai-plugins
```

After a revision containing Tim skills is published at `tacascer/ai-plugins`,
the remote installation commands are:

```bash
codex plugin marketplace add tacascer/ai-plugins
codex plugin add tim-skills@tacascer-ai-plugins

claude plugin marketplace add tacascer/ai-plugins
claude plugin install tim-skills@tacascer-ai-plugins
```

## Use a workflow

All workflows use the `tim-skills` namespace:

```text
# Codex
$tim-skills:ask-tim which skill fits my task?
$tim-skills:audit-tests review these tests

# Claude Code
/tim-skills:ask-tim which skill fits my task?
/tim-skills:audit-tests review these tests
```

See the [workflow list](plugins/tim-skills/README.md#workflows) for all 15 skill
names. `ask-tim` is explicit-only and recommends without starting another
workflow. The fourteen specialist skills support automatic selection for matching
requests; packaging checks alone do not establish live selection or semantic
correctness.

## Migrate existing installations

Tim skills replaces `testing-principles`, `time-modeling`,
`design-observability`, `domain-driven-design`, `rust-patterns`, and
`graphql-design`. Update the marketplace to a revision containing Tim skills,
install `tim-skills`, and remove or disable the six old packages to avoid loading
duplicate guidance. Use the installation commands above for the new package.

Skill names stay the same; only the plugin prefix changes. For example,
`$testing-principles:audit-tests` becomes `$tim-skills:audit-tests`, and
`/graphql-design:design-graphql` becomes `/tim-skills:design-graphql`.
The old package names and invocation aliases are no longer shipped.

For declarative installations, update the plugin selection and package paths in
the consuming configuration. This repository does not modify NixOS or user
configuration. Start a fresh session after changing installed plugins.

## Local development

Use Python 3.11 or newer in a dedicated pooled worktree and task branch. Create a
virtual environment and install the development dependency:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

After inventory or manifest changes, regenerate both catalogs:

```bash
.venv/bin/python -m scripts.catalogs
```

Run the complete local structural check set:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
```

The Python validator checks supported manifest fields, skill frontmatter, local
Markdown links, plugin containment, and catalog drift. It is narrower than each
platform's complete schema. Use native platform checks as supplemental evidence.
See [CONTRIBUTING.md](CONTRIBUTING.md) for authoring and versioning rules.
