# Ask Tim verification

Date: 2026-10-14. Baseline: `65b4a0da9bb90d8529bf3195d6b4df61db3414c4`.
See the [approved design](ask-tim-design.md) and
[evaluation guide](../evals/ask-tim/README.md).

## Executed checks

- `.venv/bin/python -m unittest discover -s tests -v`: all 30 tests passed.
- `.venv/bin/python -m scripts.catalogs`: regenerated both catalogs; their bytes were unchanged because the changed Codex interface copy is not included in generated entries.
- `.venv/bin/python -m scripts.catalogs --check`: passed.
- `.venv/bin/python -m scripts.validate`: passed repository structural validation, not exhaustive platform-schema validation.
- `git diff --check`: passed.
- Inventory inspection: all 161 prior evaluation cases are semantically unchanged, all 184 case IDs are unique, and the 23 new router contracts include a direct route for each of the fourteen specialist skills.
- Both explicit-invocation settings are present: shared frontmatter disables Claude model invocation; `agents/openai.yaml` disables Codex implicit invocation.
- Claude Code `2.1.295`: strict marketplace and plugin manifest validation passed. Inline plugin details discovered all fifteen skills, including `ask-tim`.
- Codex CLI `0.162.0`: command-local marketplace discovery found the local Tim skills plugin. Its sandbox warning about inability to create PATH aliases did not prevent discovery. No plugin was installed.

The checkout's retained virtual environment initially lacked its declared PyYAML
dependency. Installing `requirements-dev.txt` locally resolved the test import
failure; the checks above ran successfully afterward.

## Independent reasoning probes

A fresh subagent read runtime skill files without the case inventory, design
notes, or expected recommendations. It returned these routes:

| Request | Observed response |
| --- | --- |
| Implement OTLP metrics export with settled contracts | `implement-observability`, with a scoped invocation |
| Rust scheduler with unresolved local recurrence and later ownership questions | `design-time-models`, then `design-rust`, with the dependency explained |
| Unspecified request for a tests skill | Asked whether the goal was design, audit, classification, or ordinary authoring |
| Rustfmt-only task | No Tim skill needed; suggested direct formatting |
| Classification-only request | `classify-tests`, without adding another workflow |

All five matched the intended routing behavior. The subagent read candidate
bodies, performed no specialist procedures, and changed no files. These are
manual reasoning probes, not native platform activation evidence or a live run
of all 23 new evaluation contracts. Raw probe notes are retained in the
checkout's ignored `.eval-runs/ask-tim/` directory.

## Limits

The environment-provided generic helper
`/home/tacascer/.codex/skills/.system/skill-creator/scripts/quick_validate.py`
rejects `disable-model-invocation` because its allowed-key list omits that Claude
field. This supplemental helper did not pass; the field is retained to implement
the approved explicit-only behavior. Repository validation and native Claude
packaging checks passed. The native Claude manifest validator does not accept a
bare skill directory as a plugin, so its packaging result is not a separate
skill-schema certification.

Fresh platform model runs were not performed. Explicit-only activation, candidate
reference-read telemetry, the unavailable-candidate scenario, and full semantic
coverage remain unverified on the native platforms. No installation, publication,
or user configuration changes were performed.
