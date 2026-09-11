# Test quality

Assess each pillar with a question and concrete evidence. Do not collapse the result into a numerical conformance score.

| Pillar | Question | Strong evidence | Limits to report |
| --- | --- | --- | --- |
| Protection against regressions | What meaningful fault would this test detect? | The test failed for the intended reason before a bug fix; a targeted mutation was detected; or the exercised behavior and fault are traced through production code. | Coverage percentage, executed lines, or a passing test alone does not show that an important fault is detectable. |
| Resistance to refactoring | Does the test survive a behavior-preserving internal change? | It was observed through a relevant refactor, or its assertions target a stable result with no coupling to replaceable steps. | A review can infer brittleness from internal calls or leaked state, but survival is not demonstrated until a refactor is run. |
| Fast feedback | How long does the test take in its real execution context? | Recorded command, duration, and relevant environment or suite context. | `Unit`, `in process`, or `uses fakes` does not establish measured speed. Mark absent timing evidence unverified. |
| Maintainability | Can a reader understand and update the test and its fixtures at reasonable cost? | Direct setup and assertions, clear behavior naming, localized fixtures, and observed upkeep or churn when available. | Line count is only a clue. Hidden fixture mutation, broad shared setup, and duplicated domain rules raise maintenance cost. |

## Evidence discipline

Name the evidence level for each conclusion:

- **Demonstrated:** an observed execution, failure, mutation, or refactor directly supports the result.
- **Inferred:** code structure or repository evidence supports the conclusion, but the behavior was not exercised.
- **Unresolved:** the necessary code, runtime result, boundary, or requirement is missing.

A useful test normally protects behavior that matters to a client or domain rule. Prefer significance over raw code volume. A getter assertion can be valuable when it observes a meaningful state transition; the same assertion adds little when it merely repeats a trivial assignment.

## Test doubles and value

Neither `mock everything` nor `never mock` is a sound rule. A mock that verifies collaboration inside the chosen boundary usually reduces refactoring resistance. A mock that verifies a promised notification to an unmanaged external system can protect observable behavior. A stub can make input deterministic, but verifying how often it was queried adds coupling without protecting a separate outcome.

Assess the role and boundary first, then judge the double. See [dependencies](dependencies.md) and [test-double examples](../examples/test-doubles.md).

## Coverage adequacy

Use coverage data to find unexamined areas, not to declare adequacy. Ask which important behaviors and failure modes are protected, whether redundant tests add distinct fault detection, and whether missing coverage sits in meaningful logic. Do not mandate a percentage or one test per method.
