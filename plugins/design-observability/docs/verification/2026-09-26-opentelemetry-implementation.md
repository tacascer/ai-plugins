# OpenTelemetry implementation verification

## Scope

Version 0.3.0 adds `implement-observability`, an implementation reference and worked
example, six implementation evaluation cases, and a dashboard negative-selection
case. The design description now targets architecture choices to distinguish it
from implementation. Both manifests and generated catalogs were refreshed; the
Codex catalog content is unchanged because package identity and path are unchanged.

## Authoring probes

Two fresh read-only subagents received the same scenario: implement portable
metrics and traces for delayed, at-least-once `JobCompleted` events containing IDs,
outcome, wall-clock completion time and elapsed milliseconds, without trace context.
HTTP automatic instrumentation exists, traces are sampled at 10%, export can fail,
and CI has no hosted backend. They were asked for pseudocode and verification.

The baseline had no access to repository skills, memory, or evaluation cases. It
correctly handled OTLP, sampling, replay, propagation, and exporter limits, but its
`execute_job` pseudocode directly called `tracer.start_span`, `completed.add`, and
`duration.record`. It did not preserve the existing application/event/listener
boundary. This is evidence of a plugin-boundary gap, not general OpenTelemetry
incorrectness.

The second probe explicitly read only the new skill and linked runtime guidance.
It used an adapter-owned `JobObservation` scope and local `JobMetrics` listener,
with application-facing events and no OTel imports in `execute_job`. It distinguished
attempts from unique jobs, isolated diagnostic failures, kept metrics independent
of sampling, propagated context across queue boundaries, preserved automatic HTTP
spans, and separated in-memory tests from local OTLP receiver tests. It correctly
reported its verification steps as proposed, not executed.

These are two limited authoring probes, not repeated statistical tests or a native
plugin-loader evaluation. The probes produced pseudocode, not an executed service.
No native activation or full 30-case semantic evaluation was performed.

## Executed checks

- Repository unittest suite: 30 tests passed before and after implementation.
- Catalog regeneration and `scripts.catalogs --check`: passed.
- `scripts.validate`: passed.
- Skill creator `quick_validate.py`: passed for the new implementation skill and
  the modified design skill.
- Evaluation consistency: 30 unique IDs, nine design, thirteen audit, six
  implementation, two negative cases; all expected identities refer to shipped
  skills; three explicit and 27 implicit cases.
- `git diff --check`: passed for tracked changes.

These checks validate repository structure and supported metadata, not exhaustive
platform schemas, automatic activation, or a deployed OpenTelemetry pipeline.
No plugin installation or user configuration was changed.
