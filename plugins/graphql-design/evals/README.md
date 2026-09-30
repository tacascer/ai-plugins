# GraphQL Design evaluations

[cases.json](cases.json) contains twenty authored probes: three design, fifteen
audit, and two unrelated tasks. `design-missing-order`, `audit-schema-only`,
`audit-identity-collision`, and `audit-backward-order` use explicit invocation;
the rest test implicit selection. Six audit cases supply the static library
fixture; other behavioral cases include self-contained traces in `context`.
The cases are grader expectations, not evidence of live agent behavior. Grade
meaning and evidence, not exact prose.

## Submission and isolation

Submit only each case's `prompt` and `context` to the model. If a case later has
`fixture_paths`, copy precisely those designated files into the disposable
workspace; make their paths available without exposing the grader field. Keep
`expected_activation`, `required_findings`, and `forbidden_findings` outside the
model's context. Do not expose this README or the complete cases file.

Render explicit `Use graphql-design:...` as `$graphql-design:...` for Codex or
`/graphql-design:...` for Claude Code, and record the exact submitted input.
Use an ignored `.eval-runs/` disposable workspace. The plugin run may read a
runtime copy of only manifests, skills, references, and
`examples/design-decisions.md`, plus selected fixture copies. Explicitly
exclude the worked answer `examples/audit-findings.md`, as well as `evals/`,
`docs/`, the plugin README, and the original checkout from runtime access.
Selected fixture files are the sole exception to excluding `evals/`. Use
supported isolated loading without changing user plugin configuration.

A no-plugin baseline submits the same prompt/context without plugin guidance.
For explicit invocation, remove the unavailable workflow invocation and
record that difference. Attempt the `design-no-relay-client` and
`audit-valid-options` baselines only when an isolated inference harness is
available. An unavailable harness or login is unavailable inference, not a
semantic failure.

## Grading and record

Semantic `pass` requires every required finding and no forbidden conclusion;
otherwise record `fail` or `unverified` with response evidence. A proposed
check is not an executed check. Scope claims to supplied SDL and traces; never
invent code locations or test execution.

Record activation separately as `yes` with decisive skill telemetry, `no` with
sufficient telemetry proving none occurred, or `unknown` when telemetry is
insufficient. Record all observed plugin-qualified identities and compare them
to `expected_activation`; similar advice alone does not prove activation. A
negative case passes selection only with an empty observed set and sufficient
telemetry. Unknown activation remains unknown even with a sound answer.

For each attempt capture case ID and run kind, platform/version/model/UTC time,
exact input and loading/tool configuration, transcript path in `.eval-runs/`,
activation evidence and observed identities, selection match or uncertainty,
semantic verdict with supporting response, and unavailable checks. Keep
credentials and account identifiers out of records. One initial attempt per
platform/model/case is enough; repeat only after an identified setup or content
correction and preserve earlier evidence. Commit only concise verification
summaries; raw transcripts stay ignored. Static case-to-guidance mapping and
repository checks do not establish activation or semantic quality.
