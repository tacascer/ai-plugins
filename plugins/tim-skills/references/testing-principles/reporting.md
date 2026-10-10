# Reporting tests

Report facts in a form that lets a reader reproduce the classification or quality judgment. Keep scope and value separate.

## Test record

Use one record per test or coherent test group:

```text
Test: <identifier and file:line>
Behavior: <client-visible rule or outcome>
Boundary: <named system under test and client>

Classification:
- Scope: <unit | integration | end-to-end integration | conditional>
  Evidence: <behavior size, measured/unverified speed, test isolation>
- Assertion style: <output | state | communication | mixed>
  Evidence: <assertion targets>
- Dependencies: <dependency: shared/private, in/out of process,
  managed/unmanaged/unknown>
  Evidence: <fixture lifecycle, process, ownership, observers>
- Assertion target: <observable behavior | implementation detail | mixed>
  Evidence: <connection to the client goal at this boundary>

Quality:
- Regression protection: <finding and evidence level>
- Refactoring resistance: <finding and evidence level>
- Feedback speed: <finding and measurement, or unverified>
- Maintainability: <finding and evidence level>

Confidence: <supported | conditional | unresolved>
Missing facts: <none, or the exact facts needed>
Recommended action: <retain | improve | relocate | consolidate | remove>
Execution evidence: <commands actually run and observed results, or not run>
```

`Supported` means the available evidence establishes the conclusion. `Conditional` means the conclusion changes with a named unknown. `Unresolved` means current evidence cannot sustain a useful conclusion.

## Findings

For an audit, lead with material risks in descending impact. Give a precise change and preserve useful coverage. Recommend removal only when evidence shows that the test adds no distinct protection or that replacement coverage retains the behavior.

State whether a quality result is demonstrated or inferred. A code review may support the inference that an internal call assertion is brittle; it does not demonstrate refactor survival. A command listed in documentation is proposed until it is actually run. A test is observed passing only when its result was seen in the current work; otherwise say `not run` or `expected`, as appropriate.

For authoring work, also report the selected behavior, scope, dependency choices, and the regression demonstration when applicable. Include the failure before the fix and pass after the fix only if both were observed.

Do not invent requirements when code, tests, and user intent conflict. Describe the conflict, identify the evidence sources, and ask for or locate the missing authority.
