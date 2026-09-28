# Rust Patterns behavioral evaluations

[cases.json](cases.json) contains 20 authored probes: 8 design, 11 audit, and
1 unrelated-task case. These are contracts for selection and reasoning, not
evidence that either platform's model has passed. The original
[document-processing fixture](fixtures/rust-review/README.md) supplies code and
business facts for traceable audits. Prompts and contexts are model-visible;
activation and finding fields are private grading expectations.

## Submission and isolation

Submit only one case's `prompt` and `context`. For a case with `fixture_paths`,
copy precisely those files to the disposable audit workspace and make their
relative paths available. Do not submit `fixture_paths` as a grader instruction.
Keep `expected_activation`, `required_findings`, and `forbidden_findings`
outside the evaluated model's context. Do not expose this README or the complete
cases file to that model. For the two explicit cases, render `Use
rust-patterns:...` as `$rust-patterns:...` on Codex or `/rust-patterns:...`
on Claude Code, and record the exact submitted text.

Use a disposable workspace under ignored `.eval-runs/` or another isolated
temporary directory. For a plugin run, expose only a runtime copy of the
manifests, skills, references, and examples, plus selected fixture files under
a separate workspace path. Exclude `evals/`, `docs/`, the package README, the
original checkout, and grader material. Use a supported isolated loading
mechanism; do not install into user configuration. Check the exact plugin
snapshot loaded and record platform, version, model, UTC time, and available
tools. A source-only inspection or a CLI session without decisive skill
telemetry cannot prove automatic activation.

An optional no-plugin baseline submits the same prompt and context in an
isolated runtime with no plugin guidance. If an explicit case is baselined,
remove its unavailable workflow invocation and record that change. No baseline
should receive the source notes, skill files, complete case set, or private
rubrics. If isolated inference is unavailable, record it as unavailable rather
than a model failure.

## Grading and evidence

Grade semantic meaning, not exact wording. A semantic pass includes every
required finding and no forbidden conclusion. An answer that merely proposes a
check has not run it. For prose scenarios, tie claims to supplied facts without
inventing file or line locations. For fixture audits, count a finding only if
it traces the relevant code symbol, explains the contract consequence, and
offers a proportionate correction. A no-change conclusion passes
`audit-sound-simple` when supported by the supplied facts.

Record activation independently from semantic quality. `yes` requires decisive
skill invocation telemetry; `no` requires telemetry proving no invocation; and
`unknown` means the trace cannot decide. Similar advice alone does not prove
activation. Preserve the full observed plugin-qualified identity set and
compare it separately to `expected_activation`; the negative case expects an
empty set. Use semantic verdicts `pass`, `fail`, or `unverified` and explain
unknown and unverified results.

Make one initial attempt per platform/model/case. Repeat only to examine a
known setup issue or a content correction, retaining earlier evidence. For
each attempt record case ID, `baseline` or `plugin` run kind, platform, version,
model, UTC time, exact submission and loading/tool access, transcript path,
activation evidence, observed identity set, expected-set comparison, semantic
verdict with response evidence, and unavailable checks. Keep credentials and
account identifiers out of records. Raw transcripts stay in the ignored
workspace; a concise verification summary may be committed under `docs/`.
Structural validation and static rubric review do not establish runtime
activation or model behavior.
