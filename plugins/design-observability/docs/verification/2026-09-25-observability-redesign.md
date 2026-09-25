# Observability redesign verification

## Scope

Version 0.2.0 renames the plugin to `design-observability` and the workflows to
`design-observability` and `audit-observability`. The default is explicit structured
application events with listener-owned signal mappings. Direct diagnostics are
reserved for infrastructure-availability gaps, including startup. Both manifests,
inventory, catalogs, documentation, examples, and evaluation cases were updated.
Historical version 0.1.0 documents were moved unchanged with the package.

## Authoring probes

Two fresh read-only subagents explicitly read skill files and shared references.
The first read the old skills before edits; the second read the new skills without
accessing evaluation expectations. Both received the same two scenarios:

1. Design a small synchronous import service with existing direct logging/metrics
   SDK calls, support failure diagnosis, outcome counts and duration metrics,
   pre-telemetry startup configuration failures, and no desired broker or hosted
   service. Give boundaries and verification.
2. Audit handlers that call logger/counter SDKs directly, increment success before
   commit, register listeners after traffic acceptance, print startup errors on
   stderr, and assert JSON log strings in tests.

The old guidance allowed direct SDK calls and did not prescribe structured-event
verification. The revised design response used an in-process event interface,
separate diagnostic and metric listeners, registration before work, post-commit
success events, bounded metric labels, and a startup availability fallback.
The revised audit identified premature success, registration timing, SDK coupling,
and rendered-JSON test coupling while preserving justified startup stderr and
separating architectural gaps from proven data loss.

These are limited authoring probes, not native plugin-loader tests, an isolated
23-case evaluation run, or repeated statistical validation. No automatic selection
claim is made. Full semantic-suite results and native activation remain unverified.

## Executed checks

- `.venv/bin/python -m unittest discover -s tests -v`: 30 tests passed.
- `.venv/bin/python -m scripts.catalogs --check`: passed.
- `.venv/bin/python -m scripts.validate`: passed.
- Skill creator `quick_validate.py` for each renamed skill: passed.
- Evaluation artifact consistency: 23 unique cases, nine design, thirteen audit,
  one negative case, all expected workflow identities matching renamed skills.
- `git diff --check`: passed for tracked changes.

Repository and skill validators check supported structure and metadata; they do
not provide exhaustive platform-schema validation or establish deployed behavior.
No plugin installation or user configuration change was performed.
