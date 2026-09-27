# Domain-Driven Design evaluations

[cases.json](cases.json) defines ten semantic probes for design, audit, and
unrelated-task selection. The prompts and contexts are model-visible; activation
and finding fields are private grading expectations. The cases cover both new
design and existing-system review. They are authored tests, not evidence that a
model has selected a skill or produced the desired result.

## Submission and isolation

Submit only a case's `prompt` and `context`. Keep `expected_activation`,
`required_findings`, and `forbidden_findings` outside the evaluated model's
context. Do not expose this guide or the complete cases file to that model.
For the two explicit cases, render `Use domain-driven-design:...` as
`$domain-driven-design:...` for Codex or `/domain-driven-design:...` for Claude
Code. Record the exact submitted input.

Use a disposable workspace under ignored `.eval-runs/`. Expose only a runtime
copy of the manifests, skills, references, and examples; exclude `evals/`,
`docs/`, and the README. Do not expose the original checkout or grader material.
Use supported isolated loading without installing into user configuration.

An optional no-plugin baseline submits the same prompt and context without
plugin instructions. For explicit cases, remove the unavailable workflow
invocation and document the change. Do not expose plugin guidance to a baseline.
Record an unavailable isolated inference setup as unavailable, not as a model
failure.

## Grading

Grade meaning rather than exact wording. A semantic pass includes every required
finding and no forbidden conclusion. A proposed check is not an executed check.
For a supplied prose scenario, cite its concrete facts; never invent file or
line locations. Record activation independently: `yes` requires decisive skill
invocation telemetry, `no` requires telemetry proving none occurred, and
`unknown` means telemetry is insufficient. Similar advice alone does not prove
activation. Record the full observed plugin-qualified identity set and compare
it to `expected_activation` separately; the negative case expects an empty set.

Use semantic verdicts `pass`, `fail`, or `unverified`. Explain unknown and
unverified results. Make one initial attempt per platform/model/case; repeat
only to examine an identified setup or content correction, retaining the prior
evidence.

## Observation record

For each attempt, capture the case ID and `baseline` or `plugin` run kind;
platform, version, model, and UTC time; exact submission and loading/tool access;
transcript path in the ignored workspace; activation evidence and observed
identities; expected-set selection result; semantic verdict with response
evidence; and unavailable checks. Keep credentials and account identifiers out
of records. Commit a concise verification summary in the plugin, while raw local
transcripts remain ignored. Structural checks and a static case-to-guidance
review do not establish runtime activation or semantic behavior.
