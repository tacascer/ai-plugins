---
name: design-observability
description: Use when designing or changing application observability, structured events, telemetry listeners, metrics, logs, traces, or failure reporting.
---

# Design Observability

Make observability a first-class application boundary:

```text
application -> explicit structured events -> listeners -> signals -> consumers
```

Application code describes what happened; listeners translate those facts into
metrics, logs, traces, or error reports. Read the shared
[principles](../../references/principles.md) before choosing contracts and delivery.

## Procedure

1. Inspect operational needs, existing instrumentation, application outcomes,
   composition, lifecycle, and deployment constraints. Identify each consumer,
   the question they must answer, and their response. Observe business outcomes
   directly; exception reporting alone misses incorrect successful execution.
2. Define explicit event contracts and emission boundaries. Specify the fact,
   typed or schema-defined fields, units, outcome, correlation context, and
   sensitive-data exclusions. Capture facts when they occur; distinguish an
   attempt from a committed result. Emit through an application-facing interface
   instead of calling logging or metrics SDKs throughout application code.
3. Map each event to listeners and useful signals. Assign log severity, metric
   dimensions, trace correlation, and destination policy to listeners. Keep
   high-cardinality identifiers out of metric labels. Reuse suitable existing
   dispatch facilities; an in-process interface and listeners are sufficient.
   Do not require a broker, durable event store, vendor, or infrastructure stack.
4. Design composition and lifecycle: register listeners before observed work,
   define delivery failure behavior, and address buffering, retries, duplicates,
   flushing, and shutdown where relevant. Preserve application failure semantics
   and account for signal ownership, retention, and cost.
5. If the event infrastructure is not guaranteed to be available at the point
   of failure, specify minimal direct diagnostics, such as sanitized startup
   stderr. Identify the availability gap and the handoff to normal event
   emission. Application simplicity alone is not an exception; offline systems
   can use local listeners.
6. Propose verification at the event, listener, and composition boundaries:
   assert structured events and application outcomes, test listener mappings
   through structured records or measurements, and exercise lifecycle and
   delivery failures. Do not assert rendered log strings or diagnostic JSON.
7. Report the concrete design using [reporting](../../references/reporting.md),
   separating facts, assumptions, proposed checks, and executed checks.

Consult the [examples](../../examples/observability-decisions.md) when a contrast
helps. This skill covers application observability architecture, not unrelated
prose edits or standalone vendor/platform administration. It does not authorize
implementation beyond the user's request or override development processes.
