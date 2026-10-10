# Observability decision examples

These authored scenarios illustrate decisions, not executed tests.

## Import outcome with two listeners

Support needs per-import failure diagnosis; operators need outcome counts and
latency. A synchronous service already has a logger and a metrics backend.

Define structured `ImportCompleted(import_id, attempt, duration_ms)` and
`ImportFailed(import_id, attempt, stage, failure_kind, duration_ms)` events.
Application code emits a final event through an injected event interface after
the outcome is known. Completion means successful commit; a rolled-back attempt
must not emit completion. Capture safe values at that boundary.

At composition, register a diagnostic listener and a metrics listener before
accepting imports. The first maps failures to structured records with import ID,
stage, failure class, and documented severity. The second increments the relevant
outcome counter and records a duration histogram, with bounded outcome/stage
labels and no import-ID label. Both consume the same facts. No broker is needed.
An expected rejection may map to a normal outcome rather than an error alert.

Verify the producer's event and returned result for successful commit and commit
failure. Supply event values to the listeners and inspect structured records and
measurements. Exercise real registration so the first import reaches both
listeners. Do not test rendered log strings or JSON output.

**Audit contrast:** Direct logger/counter calls in the import handler couple
business flow to signal policy. Move their mapping into listeners while preserving
support's existing history. A counter increment before commit is a separate,
confirmed accuracy defect; correcting the architecture alone does not fix timing.

## Initialization before observability exists

Configuration validation can fail before listeners are registered. Emit a minimal,
sanitized stderr diagnostic and fail startup. This direct path covers a specific
availability gap. Once listeners are ready, normal operations emit events;
do not keep both paths active for the same occurrence. A tiny service still uses
the normal event boundary after initialization.

## Offline deployment and failed exporter

An on-premise installation has no network, but can register local listeners.
Structured events feed bounded local diagnostic bundles that support can collect.
Offline operation is not itself a reason to bypass the event boundary. If a remote
exporter fails in another deployment, isolate it so a working local listener can
still consume events. Use a minimal nonrecursive fallback only when the diagnostic
infrastructure needed to report its own failure is unavailable.

## Hidden payment failure and silent malfunction

A capture error must remain a failed result; emitting `CaptureFailed` cannot make
returning success correct. A listener routes actionable failure context to the
responder without exposing card data. Separately observe accepted and rejected
checkout outcomes: exception reporting alone misses incorrect rejection of valid
carts. Correlate safely; never replace a log payload dump with an error tracker
that captures the same secrets.

## Duplicate and sampled delivery

A queued event is delivered twice after an acknowledgement is lost. Incrementing
an operations counter for both copies overcounts. Define whether the measure
counts deliveries, attempts, or operations, then use suitable deduplication or
another delivery strategy when complete operation counts are required. Sample
verbose diagnostic output independently of complete outcome measurements.
Do not require durable delivery unless the consumer's needs justify it.

## Required records and uncertain consumers

Access audit records share transport with diagnostics. Preserve their stronger
retention/access/delivery obligations; telemetry sampling must not remove required
records. If a log's consumer is undocumented, report missing evidence and identify
its purpose before removing it. Useful structured logs emitted by listeners need
no architectural rewrite merely because they are logs.
