# Repository instructions

Work in a dedicated Git worktree branch. Do not edit the main checkout directly.
Use conventional commit messages and keep changes scoped to the requested plugin
or repository tooling.

Plugins are independent packages under `plugins/<name>/`. Keep a plugin's skills,
references, examples, evaluations, and documentation inside that directory. Do
not create platform-specific copies of shared skill or curriculum content. A new
plugin must be registered in `catalogs/plugins.json`; Blueprint, NixOS, or user
configuration is outside this repository's contribution flow.

After changing inventory or plugin manifest metadata, regenerate both catalogs:

```bash
.venv/bin/python -m scripts.catalogs
```

Before committing, run:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
```

Treat native Codex and Claude validators as supplemental platform checks. Do not
describe the repository's Python validator as exhaustive platform-schema
validation.
