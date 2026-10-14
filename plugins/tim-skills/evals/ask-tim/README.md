# Ask Tim evaluations

Select the `ask-tim-` cases from [cases.json](../cases.json). These contracts
cover every specialist route, short flows, uncertainty, no-match requests,
unavailable candidate guidance, and explicit-only selection.

## Inputs and isolation

Send only each case's `prompt` and `context` to the evaluated model, together
with a runtime copy of the plugin manifests, skills, references, and examples.
Keep this guide, the case inventory, expected activation, required findings, and
forbidden findings in the grader process. For `runtime_exclusions`, remove the
listed plugin-relative directories from the runtime copy before the run; this
simulates incomplete packaging without changing the source checkout.

Translate the explicit phrase `Use ask-tim:` to `$tim-skills:ask-tim` for Codex
or `/tim-skills:ask-tim` for Claude Code, preserving the task. Submit implicit
cases as written with normal plugin discovery; never preload the router for an
implicit-selection check. Capture exact inputs, tool events, responses, and any
filesystem effects under ignored `.eval-runs/` directories.

## Grade routing separately from activation

A passing explicit routing case reads the relevant candidate bodies as reference,
returns a justified route or focused question, and stops before specialist work.
A mention, file read, or proposed invocation is not itself evidence that a
specialist workflow started. Use platform events where available to distinguish
reference reads from activation. The expected activation is only `ask-tim` for
explicit cases; candidate recommendations are semantic findings.

For no-match cases, a clear explanation and direct handling suggestion is enough;
the router should not perform the underlying task. For an unavailable candidate,
expect a named evidence limit, not a fabricated read or automatic installation.
Grade flow order by the dependency in the supplied context rather than a universal
ordering of topics. Classification alone need not become an audit or redesign.

Use the shared [result schema](../testing-principles/result.schema.json), keeping
activation telemetry separate from semantic quality. Record missing telemetry as
unknown, and distinguish manual reasoning probes from native platform discovery.
For the implicit case, check policy on both platforms: Claude's
`disable-model-invocation: true` and Codex's `allow_implicit_invocation: false`.
Configuration inspection is structural evidence; activation behavior requires
fresh platform runs. No case inventory or structural pass establishes live model
reliability.
