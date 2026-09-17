# Testing Principles evaluations

These evaluations check workflow selection and semantic application of the shared
testing curriculum. They are behavioral probes, not platform certification or a
numerical test-conformance score.

## Artifacts and balance

- [cases.json](cases.json) contains model inputs and grader-only expectations.
- [result.schema.json](result.schema.json) defines one recorded observation.
- [python-cart](fixtures/python-cart/README.md) and
  [js-notifier](fixtures/js-notifier/README.md) are deliberately defective source
  fixtures for distinguishing behavior defects from testability obstacles.

The first 12 cases are six audit/design pairs with identical context: multi-class
pricing, observable account state, an internal-query stub, an outgoing notification
contract, a managed database, and unknown database ownership. Design cases ask for
production boundaries and a verification approach, without requiring test code.
Further cases cover classification, shared-state pollution, missing language
context, unrelated requests, plugin overlap, and explicit fixture-based design.
The `invocation` field records implicit and explicit selection separately.

Seam cases cover design before tests exist, sufficient existing boundaries,
legacy refactors without a safe baseline, logging contracts, and clock acquisition
timing. The tests-only improvement case may activate `audit-tests`; the ordinary
unit-test-authoring case should activate no testing-principles workflow. Neither
should activate `design-for-testing` merely because tests were requested.

Grade the proposed production boundary, preserved semantics, and verification
path. Isolated injected-object checks alone do not establish production wiring.
Existing historical results for the former `write-tests` workflow do not establish
activation or semantic correctness for these revised cases.

## Keep the oracle hidden

Never send a whole case object or this guide to the model. Construct a reasoning
case's model input from only `prompt` and `context`. Keep `expected_activation`,
`required_findings`, and `forbidden_findings` in the grader process. For an
explicit case, translate the generic invocation phrase into the platform's
supported explicit syntax, preserve the rest of the prompt, and capture the exact
submitted input in the transcript.

For a fixture case, expose only the copied source, fixture README, and the case's
`prompt` and `context`. Keep grader expectations hidden. Grade meaning rather than
exact wording: all required findings must be materially present, no forbidden
finding may be asserted, and execution claims must match transcript evidence.

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
`fixture-docs:write-release-notes` and `testing-principles:design-for-testing` in
`observed_workflows`, and `testing-principles:design-for-testing` in
`unexpected_activations`. The expected-set check then fails even
though activation was literally observed. Explain the literal observation and
workflow identities in `evidence.activation`; no additional activation verdict
field is needed.

Activation is telemetry, separate from response semantics. In the independent
plugin overlap case, record `fixture-docs:write-release-notes` when observed and
record any coactivated `testing-principles:audit-tests`,
`testing-principles:classify-tests`, or `testing-principles:design-for-testing`
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

## Disposable fixture assessments

Copy fixtures into ignored `.eval-runs/` workspaces, for example
`.eval-runs/<platform>/<case-id>/<timestamp>/workspace`. Capture the submitted
input, activation events when available, response, commands, and final diff.
The design cases require unchanged source and no authored test files.

For Python, the existing pure function already has controllable input and an
observable output. The grader checks that the response identifies the threshold
defect separately and proposes totals 54 at 49, 50 at 50, and 51 at 51. No new seam
is needed. Proposed examples are not evidence of an executed regression.

For JavaScript, the existing sender parameter already supplies the needed seam.
The grader checks that the response identifies the duplicate send separately,
proposes observing one `Welcome` message to the address, and explains that sender
substitution does not verify real delivery or production composition. Parameter
names and function source text are not observable contracts.

These are design assessments; test execution is not a required observation.
Record a missing runtime only if an execution claim actually depends on it.
Do not install runtimes or fix the deliberate defects for these cases.

## Review

Run each initial case once per platform and configured model. Compare the captured
response with its independently authored required and forbidden findings and
create one record conforming to `result.schema.json`. Workflow agreement does not
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
| Quality pillars and evidence levels | audit/classify cases; design evidence limits |
| Logging consumers, explicit seams, and conditional observability | diagnostic logging; support logging; hidden logger; unknown logger |
| Repository-language adaptation and uncertainty | limited-context unfamiliar-language design |

Review these against the plugin's [source map](../references/sources.md), preserve
uncertainty, and keep unsupported conclusions visible instead of smoothing them
into a score.
