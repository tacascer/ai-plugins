# Logging Principles evaluations

[cases.json](cases.json) contains 16 semantic probes. Fifteen exercise design or audit behavior across important and expected failures, business outcomes, pure computation, retained diagnostics, sensitive context, startup and disconnected environments, required records, and missing consumer evidence. The unrelated release-note case expects neither workflow to activate. Only the two missing-consumer cases use explicit invocation; the other 14 test implicit selection.

## Submission and isolation

Submit only a case's `prompt` and `context`. Keep `expected_activation`, `required_findings`, and `forbidden_findings` in the evaluator. Do not expose this guide or the case file to the evaluated model.

For explicit prompts, translate the generic workflow name to the platform form: `$logging-principles:design-logging` or `$logging-principles:audit-logging` for Codex, and the corresponding `/` form for Claude. Record the exact submitted input.

Use a fresh disposable workspace under ignored `.eval-runs/`. Expose a runtime copy of only the manifests, skills, references, and examples. Exclude `evals/`, `docs/`, the README, and the original checkout. Permit access only to the disposable workspace and the runtime copy. Use supported isolated loading without installing into user configuration.

An optional baseline uses the same input without plugin instructions. Omit an explicit workflow invocation when that invocation is unavailable in the baseline, and document the changed submission. Do not give baselines access to authored guidance. Keep baseline and plugin observations separate.

## Grading

Grade meaning rather than exact wording. A semantic pass requires every required finding and no forbidden conclusion. Grade semantics independently from activation. A proposed check is not an executed check, and abstract contexts do not require fabricated file or line references.

Record activation as `yes` only when telemetry decisively shows invocation, `no` when sufficient telemetry proves none occurred, and `unknown` when telemetry is insufficient. Listing a workflow or giving similar advice does not prove activation. Record every observed plugin-qualified workflow and compare the observed set with `expected_activation` separately.

Use semantic verdict `pass`, `fail`, or `unverified`. Mark unavailable inference, such as a login failure or unavailable supported loader, `unverified` and explain it; do not turn it into a failed semantic response. Record one attempt per platform, model, and case initially. Repeat only after an identified setup or content correction, preserving earlier evidence.

## Observation record

For every attempted case, record:

| Field | Evidence |
| --- | --- |
| Case and run kind | Case ID and `baseline` or `plugin` |
| Environment | Platform, version, model, and UTC timestamp |
| Submission | Exact prompt, context, and loading/tool-access configuration |
| Transcript | Path within the ignored evaluation workspace |
| Activation | `yes`/`no`/`unknown`, observed workflow identities, and supporting telemetry |
| Selection | Expected-set match or unresolved, including unexpected invocations |
| Semantics | `pass`/`fail`/`unverified` with response-grounded findings |
| Unavailable checks | Missing evidence and why it could not be obtained |

Keep credentials and account identifiers out of records. Raw transcripts remain in `.eval-runs/`. Author review of the 16 cases against the guidance is an artifact consistency check, not a model evaluation.

The [initial verification record](../docs/verification/2026-09-17-initial.md)
records the current artifact and structural evidence. Live activation and
semantic behavior are unverified in this environment.
