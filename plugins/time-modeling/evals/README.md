# Time Modeling evaluations

[cases.json](cases.json) contains 16 semantic probes. Six design/audit pairs
share scenarios: recorded instants, local commitments, rule updates, gaps and
overlaps, recurrence, and missing requirements. Four additional cases cover an
offset-only record, location-defined intent, recent-past import, and an unrelated
release-note request. Both missing-requirements cases use explicit invocation;
the other 14 test implicit selection. Synthetic rules do not depend on the host's
tzdb release.

## Submission and isolation

Submit only a case's `prompt` and `context`. Keep `expected_activation`,
`required_findings`, and `forbidden_findings` in the evaluator. Do not expose this
guide or the entire case file to the evaluated model.

For explicit prompts, replace the generic workflow name with the supported
platform form: `$time-modeling:design-time-models` or
`$time-modeling:audit-time-models` for Codex, and the corresponding `/` form for
Claude. Record the exact submitted input.

Use a disposable workspace under ignored `.eval-runs/`. Expose a runtime copy of
only the manifests, skills, references, and examples; exclude `evals/`, `docs/`,
and the README, which links evaluator material. Permit reading the runtime copy
and references. Do not allow access to the original checkout or grader material.
Use supported isolated loading without installing into user configuration.

An optional baseline uses the same input without plugin instructions; an explicit
invocation baseline must omit the unavailable workflow invocation and document
that difference. Do not give baselines access to authored guidance. Keep baseline
and plugin observations separate.

## Grading

Grade meaning, not wording. A semantic pass requires every required finding and
no forbidden conclusion. A proposed test is not an executed test. With abstract
context and no source files, absence of file/line references is appropriate; do
not encourage fabricated code citations.

Record activation independently: `yes` means telemetry decisively shows a skill
invocation; `no` means sufficient telemetry proves none occurred; `unknown` means
telemetry is insufficient. Listing available skills or producing similar advice
does not prove activation. Record every observed plugin-qualified workflow,
including unexpected ones. Compare that set with `expected_activation` separately;
an unrelated case succeeds on selection only when no workflow activated.

Use semantic verdict `pass`, `fail`, or `unverified`. Explain each unknown or
unverified outcome. A login failure is unavailable inference, not a failed
semantic response. Record one attempt per platform/model/case initially; repeat
only for an identified setup or content correction, preserving earlier evidence.

## Observation record

Record these fields for every attempted case, using JSON or Markdown:

| Field | Evidence |
| --- | --- |
| Case and run kind | Case ID and `baseline` or `plugin` |
| Environment | Platform, version, model, UTC timestamp |
| Submission | Exact prompt/context and loading/tool-access configuration |
| Transcript | Path within the ignored evaluation workspace |
| Activation | `yes`/`no`/`unknown`, exact observed workflow identities, and supporting telemetry |
| Selection | Expected-set match or unresolved; identify unexpected invocations |
| Semantics | `pass`/`fail`/`unverified` and findings grounded in the response |
| Unavailable checks | Missing evidence and why it could not be obtained |

Keep credentials and account identifiers out of records. Commit a concise
verification summary inside the plugin; raw local transcripts stay ignored.
Authored cases and structural validation alone do not establish model behavior.
See the [initial verification record](../docs/verification/2026-09-17-initial.md)
for the actual checks performed.
