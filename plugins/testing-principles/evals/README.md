# Testing Principles evaluations

These evaluations check workflow selection and semantic application of the shared
testing curriculum. They are behavioral probes, not platform certification or a
numerical test-conformance score.

## Artifacts and balance

- [cases.json](cases.json) contains model inputs and grader-only expectations.
- [result.schema.json](result.schema.json) defines one recorded observation.
- [python-cart](fixtures/python-cart/README.md) and
  [js-notifier](fixtures/js-notifier/README.md) are deliberately defective,
  executable fixtures.

The first 12 cases are six equally weighted audit/write pairs with identical
context: multi-class pricing, observable account state, an internal-query stub,
an outgoing notification contract, a managed database, and unknown database
ownership. Further cases cover explicit classification, mixed assertions with
unmeasured runtime, shared-state pollution, limited-context unfamiliar-language
reasoning,
unrelated documentation, overlap with an independent fixture plugin, and the two
executable fixtures. The `invocation` field records `implicit` and `explicit`
selection separately.

Additional seam-design cases cover production-only design requests, an already
testable multi-class behavior that needs no new seam, a legacy refactor with no
safe pre-change baseline, and an explicit tests-only constraint. Grade both the
proposed production boundary and its verification path: isolated injected-object
tests alone do not establish that production composition uses the tested logic.

## Keep the oracle hidden

Never send a whole case object or this guide to the model. Construct a reasoning
case's model input from only `prompt` and `context`. Keep `expected_activation`,
`required_findings`, and `forbidden_findings` in the grader process. For an
explicit case, translate the generic invocation phrase into the platform's
supported explicit syntax, preserve the rest of the prompt, and capture the exact
submitted input in the transcript.

For an executable case, expose only its copied fixture source, its fixture README,
and the case's `prompt` and `context`. Do not expose the oracle or refactor probe
below before the response is complete. Grade meaning rather than exact wording:
all required findings must be materially present, no forbidden finding may be
asserted, and execution claims must match transcript evidence.

Record every workflow identity exposed by platform events in
`observed_workflows`, using the plugin-qualified
`plugin-name:workflow-name` form. Record every observed identity absent from the
case's `expected_activation` in `unexpected_activations`.
`observed_activation` records
literal telemetry: use `yes` when at least one workflow is decisively observed,
`no` when decisive telemetry shows that no workflow activated, and `unknown` when
telemetry is insufficient. Similar reasoning alone does not prove activation. If
`expected_activation` is empty and decisive telemetry observes no workflows,
`observed_activation` is `no` and both workflow arrays are empty.

Determine expected-set matching separately by comparing `expected_activation`
with `observed_workflows` and checking `unexpected_activations`. For example, the
independent plugin overlap case can record `observed_activation` as `yes`, both
`fixture-docs:write-release-notes` and `testing-principles:write-tests` in
`observed_workflows`, and `testing-principles:write-tests` in
`unexpected_activations`. The expected-set check then fails even
though activation was literally observed. Explain the literal observation and
workflow identities in `evidence.activation`; no additional activation verdict
field is needed.

Activation is telemetry, separate from response semantics. In the independent
plugin overlap case, record `fixture-docs:write-release-notes` when observed and
record any coactivated `testing-principles:audit-tests`,
`testing-principles:classify-tests`, or `testing-principles:write-tests`
identity as unexpected. Do not require the response itself to announce which
workflows loaded.

Use semantic verdict `pass` when the response meets the independent oracle,
`fail` when observed content or execution contradicts it, and `unverified` when a
required observation cannot be made. Explain the verdict in `evidence.semantic`.
List each unavailable observation and reason in `unavailable_checks`; do not turn
missing evidence into a pass or failure. The result schema requires at least one
such explanation whenever activation is `unknown` or the semantic verdict is
`unverified`.

Store plugin-enabled results and optional no-plugin baselines in separate files
or directories, with the matching `run_kind`. Outcome counts may help account for
completed cases, but they are never a conformance score or reliability estimate.

## Disposable fixture runs

Run fixtures only in ignored `.eval-runs/` workspaces, for example
`.eval-runs/<platform>/<case-id>/<timestamp>/workspace`. Copy the fixture directory
into `workspace`, confirm the copy retains the deliberate defect, and allow edits
only in that copy. Capture the submitted input, activation events when available,
diff, commands, exit codes, and test output. Do not commit `.eval-runs/`.

Check for the existing runtime first. If it is absent, do not install it globally.
Leave the fixture unchanged, record the executable portion as `unverified`, and
name the missing runtime in `unavailable_checks`.

For Python, run the authored standard-library `unittest` against the original
defect first. The grader-only oracle is:

- `total(49) == 54`
- `total(50) == 50`
- `total(51) == 51`

The boundary test must fail with the original `subtotal > 50` implementation.
After correction, the relevant test and all three oracle examples must pass. A
test written only after correction, or one that never failed for the original,
does not demonstrate regression protection.

For JavaScript, run the authored test with `node --test`. It must fail against the
original two-send implementation and pass after correction while observing one
`Welcome` message to the requested address. Then rename the corrected function's
`sender` parameter to `delivery` and use `delivery.send(...)`; this changes an
internal name while preserving behavior. Run the same test again after the model
response and record the result in `evidence.execution`. This evaluator-run probe
is not a required finding in the response. A failure after the rename shows
coupling to an internal name rather than refactoring resistance.

## Review

Run each initial case once per platform and configured model. Compare the captured
response with its independently authored required and forbidden findings and
create one record conforming to `result.schema.json`. An `audit-tests`
cross-review can add evidence for authored tests, but workflow agreement does not
replace the oracle. Repeat a failed or ambiguous case only after recording the
content or setup change that justified the repeat.

| Source-mapped principle | Cases |
| --- | --- |
| Cohesive behavior and isolation | multi-class pricing; shared-state pollution |
| Output, state, communication, and mixed styles | pricing; account; notification; mixed assertions |
| Stub input and internal coupling | stub interaction |
| Observable unmanaged effects | notification pair; JavaScript fixture |
| Managed integration dependencies | managed database pair |
| Conditional ownership and missing evidence | unknown database pair |
| Quality pillars and evidence levels | audit/classify cases; executable fixtures |
| Repository-language adaptation and uncertainty | limited-context unfamiliar-language plan |

Review these against the plugin's [source map](../references/sources.md), preserve
uncertainty, and keep unsupported conclusions visible instead of smoothing them
into a score.
