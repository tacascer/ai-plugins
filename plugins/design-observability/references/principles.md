# Observability principles

## Core architecture

Design a first-class observability boundary: application code emits explicit,
structured facts; listeners translate those events into signals used by named
consumers. Start with the operational question and expected response, then define
this complete path. Do not create events for every intermediate value without a
purpose. Business-outcome monitoring and exception reporting answer different
questions; a malfunction need not throw an exception.

| Boundary | Owns | Does not own |
| --- | --- | --- |
| Application/event producer | Meaningful fact, occurrence context, outcome, emission placement | Log formatting, metric SDK calls, exporter selection |
| Event contract | Typed or schema-defined data with documented meaning and units | Preformatted messages or vendor-specific payloads |
| Listener/adapter | Signal mapping, severity, bounded metric dimensions, destination policy | Business decisions or changing the operation's result |
| Composition/delivery | Registration, lifecycle, transport behavior, delivery guarantees | Inventing facts absent from the event |

Use existing tools when they support these boundaries. An in-process emitter
interface with synchronous listeners is a valid pipeline, including for a small
application. No broker, event-sourcing rewrite, durable store, vendor, or new
hosted service is implied. The architecture is the default; small size alone
is not a reason to scatter direct logger or metrics calls through the application.

## Structured event contracts

Describe what happened, not how to print it. Prefer meaningful names such as
`ImportCompleted` and `ImportFailed` over a generic message string. Define required
and optional fields, outcome vocabulary, units, correlation context, and the
state transition that makes the event true. Capture an immutable snapshot at
that point rather than letting listeners reread changing business state.
Use language-native types or an explicit schema; do not impose one language.

Separate attempts, retries, and final outcomes. Emit committed success only after
commit succeeds. If losing an event across a commit/crash boundary is unacceptable,
choose delivery guarantees to match that requirement; post-commit emission alone
is not durable delivery. Observability events are not automatically domain events
or authoritative audit records. Reuse such events only when meaning, timing,
data exposure, and delivery guarantees match the consumer's needs.

Include only necessary, safe context. Correlation IDs may belong in events, logs,
and traces without becoming metric labels. Exclude credentials, raw bodies, and
unnecessary personal data before fan-out; apply destination-specific minimization
as well. Document compatible evolution when independent listeners or persisted
messages can outlive a schema change; versioning every in-process object is not
mandatory.

## Listener mappings and delivery

Map each event to the signals the consumer needs; not every event needs every
signal. Listeners own log severity and structured fields, metric names and units,
low-cardinality dimensions, trace/span association, and error-report routing.
Do not parse rendered logs to reconstruct event facts. Trace context and duration
must be captured at the relevant operation boundary; a late listener cannot
reconstruct missing span lifetimes. Measure elapsed duration with an appropriate
monotonic clock rather than subtracting adjustable wall-clock timestamps.

Register required listeners before accepting observed work. Define the behavior
when a listener throws, an exporter is unavailable, or one destination fails:
which listeners still run, whether work is affected, and how the failure is
reported without recursively re-emitting through the failed path. Preserve the
application's real outcome. There is no universal fail-open or fail-closed rule;
required audit delivery may have stronger obligations than diagnostic telemetry.

For asynchronous delivery, bound queues and state overflow, ordering, retry,
duplicate, and shutdown/flush behavior. Do not claim exactly-once counting from
at-least-once delivery. Define whether measurements count attempts or operations,
and how retries or replay affect them. Sample signals deliberately: sampling a
shared event stream can invalidate complete outcome counters. Choose stronger
transport only for demonstrated needs. Retention, access, cost, and response
ownership are part of a working signal path.

## Availability exception

When event infrastructure is not guaranteed to be available at the point of
failure, retain minimal direct diagnostics. Invalid startup configuration before
listener setup is the typical case: write sanitized, actionable stderr output
and preserve startup failure. Describe the exact unavailable component, the
fallback's scope, and the handoff once listeners are ready. If initialization
fails permanently, the fallback remains the available path through exit.
Avoid duplicate fallback and normal emission for the same occurrence.

An offline deployment can still run local listeners and produce bounded local
bundles. Remote-export failure alone does not make an available local event path
unusable. Apply direct fallback only where the needed infrastructure actually
cannot be relied on, including a failure of that infrastructure itself.

## Verification boundaries

- Producers: assert structured event identity and fields alongside externally
  observable application outcomes; cover attempted versus committed results and
  retries where applicable.
- Listeners: supply real event values and inspect structured records, metric
  values, or trace data at the adapter boundary. Verify mappings, cardinality,
  context exclusions, and error behavior without asserting rendered log strings
  or diagnostic JSON.
- Composition: exercise actual registration and delivery with the project's
  normal composition. Verify the first accepted operation, relevant exporter
  failures, flushing, and fallback before initialization. Unit-level event capture
  is not evidence of deployed end-to-end delivery.

Keep checks proportional to the delivery contract. Distinguish proposed checks
from those actually run and avoid expanding into unrelated testing refactors.

## Source-derived foundations and extensions

The original logging guidance draws on Nikita Sobolev's 2020 article
[Do not log](https://sobolevn.me/2020/03/do-not-log): prevent invalid states where
practical, preserve explicit failure handling, observe business outcomes,
recognize diagnostic emission as a fallible side effect, and retain useful,
structured, safe diagnostics with justified operating costs.

The event/listener architecture, availability exception, event contracts,
cardinality and lifecycle rules, and verification boundaries are this plugin's
design choices. They are not claims about that article. See
[sources](sources.md) for attribution.
