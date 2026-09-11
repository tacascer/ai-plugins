# Contributing

Create a dedicated Git worktree and branch for each change. Keep commits focused
and use conventional commit messages such as `feat: add release-notes plugin` or
`fix: repair testing-principles resource link`.

## Add a plugin

1. Create `plugins/<name>/`, where `<name>` uses lowercase ASCII letters, digits,
   and single hyphens between segments.
2. Add `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`. Both manifests
   must use the directory name as `name`, carry the same strict semantic version,
   and provide a nonempty description.
3. Add the plugin's `README.md`, skills, references, examples, and evaluations
   inside its own directory. Every `skills/<skill-name>/SKILL.md` needs YAML
   frontmatter whose nonempty `name` matches `<skill-name>` and whose `description`
   explains when the skill applies.
4. Append `{"name": "<name>", "path": "plugins/<name>"}` to
   `catalogs/plugins.json`. Inventory order is marketplace display order.
5. Regenerate the platform catalogs and run all checks:

   ```bash
   .venv/bin/python -m scripts.catalogs
   .venv/bin/python -m unittest discover -s tests -v
   .venv/bin/python -m scripts.catalogs --check
   .venv/bin/python -m scripts.validate
   ```

Add or update the plugin's own evaluation cases when a workflow's selection or
behavior changes. Keep grader-only expectations out of model-visible prompts and
store raw local transcripts under ignored `.eval-runs/`.

The repository validator supports inline Markdown links with relative local paths,
fragment-only links, and `https://` links. Percent-encoded local paths are decoded
before resolution. Local targets must exist and resolve inside the containing
plugin; absolute local paths and symlinks that escape the plugin are rejected.
Use inline syntax for local resources, for example
`[quality](references/quality.md)`. Reference-style local links are currently
rejected because the validator does not parse that syntax. Remote availability and
arbitrary Markdown correctness are outside this structural check.

## Version and catalog changes

Plugins version independently. A release of one plugin changes that plugin's two
manifest `version` fields together:

- `plugins/<name>/.codex-plugin/plugin.json`
- `plugins/<name>/.claude-plugin/plugin.json`

Then regenerate both catalogs with `.venv/bin/python -m scripts.catalogs`. Do
not bump unrelated plugins. Keep the manifest identity equal to the plugin
directory and inventory name.

A change to the catalog format or renderer affects the collection contract. Review
every generated entry on both platforms, regenerate both files, and run the full
check set. Native platform validators should supplement these repository checks
when available.

For the current first plugin, the supplemental Claude packaging checks are:

```bash
claude plugin validate --strict .
claude plugin validate --strict plugins/testing-principles
```

The Codex plugin-creator validator is an environment-provided development tool,
not a repository dependency. Use it when available, and record its exact path and
version or source revision in verification evidence. Model activation and
workflow behavior require fresh model runs; structural validators cannot
establish either result.
