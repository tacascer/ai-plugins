---
name: implement-observability
description: Use when implementing application metrics or traces, wiring OpenTelemetry instrumentation and export, or replacing provider-coupled telemetry in application code.
---

# Implement Observability

Implement backend-portable metrics and traces through the existing boundary:

```text
application -> structured events -> OpenTelemetry listeners -> SDK -> OTLP -> destination
```

Read the shared [principles](../../references/principles.md) and the
[OpenTelemetry implementation reference](../../references/opentelemetry.md).
Keep application facts independent of both vendor SDKs and OpenTelemetry types;
listeners and instrumentation adapters own OpenTelemetry calls. Provider choice
belongs in composition/export configuration. This implements a scoped request;
it does not authorize deployment, plugin installation, or unrelated rewrites.

## Procedure

1. Inspect the language, pinned dependencies, entrypoints, existing event contracts,
   automatic instrumentation, and telemetry consumers. Confirm which outcomes,
   durations, and operations need signals. Consult current official documentation
   for the chosen language/version; SDK capabilities and environment-variable
   support differ. Reuse existing instrumentation rather than duplicating it.
2. Preserve or introduce the smallest application-facing event interface needed.
   Capture safe fields, monotonic elapsed duration, and correlation context at the
   operation boundary. Emit success only when the promised result is true. For
   tracing, use an adapter-owned operation scope or synchronous lifecycle listener
   so a span exists while work runs; a late completion listener cannot reconstruct
   missing context or a real parent-child execution lifetime.
3. Implement listener mappings: choose counters, histograms, or current-value
   instruments by meaning; define units, bounded attributes, and counting semantics.
   Distinguish attempts, completions, and replay. Record metrics independently of
   trace sampling. Use explicit context across asynchronous work, close spans on
   every exit, and preserve the application's result and error behavior.
4. Wire SDK providers, readers/processors, resource identity, and listeners in
   application composition before accepting work. Use configurable OTLP export by
   default, directly to a compatible destination or through an optional Collector.
   Keep credentials, endpoints, protocols, and backend routing out of producers.
   Reusable libraries do not install global providers or exporters.
5. Bound buffering, export timeouts, and shutdown. Stop accepting work, drain
   observed work, then flush/shut down telemetry within a deadline. Keep diagnostic
   export failures from changing business outcomes; preserve stronger required
   audit guarantees separately. Use sanitized nonrecursive diagnostics for broken
   telemetry and startup availability gaps.
6. Verify structured events, listener measurements/spans, and normal composition.
   Use local SDK readers/exporters or structured captures without a hosted account;
   check context propagation, unsampled metrics, replay behavior, and exporter
   failure/shutdown. Verify actual OTLP wiring with a local receiver when changing
   export configuration. Distinguish that evidence from in-memory mapping tests.
7. Report changed boundaries, configuration, checks actually executed, and remaining
   delivery limits. Provider portability means no application-instrumentation
   rewrite to change backend; it does not promise identical backend features.

See the [worked implementation example](../../examples/opentelemetry-implementation.md)
for delayed events, trace scopes, and migration. Architecture-only requests belong
to `design-observability`; read-only reviews belong to `audit-observability`.
Standalone dashboards, backend administration, and incidental telemetry mentions
are outside this implementation workflow.
