# Implementing with OpenTelemetry

This reference applies to implementation, including migrations. The shared
[principles](principles.md) still govern event meaning and delivery. OpenTelemetry
is the instrumentation/export boundary chosen for this workflow; the event/listener
architecture is a plugin convention, not an OpenTelemetry requirement.

## Ownership and migration

| Location | Responsibility |
| --- | --- |
| Producer | Structured fact, outcome, safe occurrence context and elapsed duration |
| Listener/instrumentation adapter | OpenTelemetry API calls, instruments, span scopes and propagation |
| Application composition | SDK providers, readers/processors, resources, exporter configuration and shutdown |
| Optional Collector | Deployment-owned routing, processing and backend export |

Inventory existing automatic instrumentation and vendor hooks first. Reuse a
framework span when it already represents the operation; create child spans only
for distinct work. Assign one owner per measurement to prevent duplicate counts
or spans during migration. Preserve useful fields and required records; remove old
emission only after equivalent mappings and normal startup wiring are verified.
Do not rename established dashboards' instruments without accounting for consumers.

Reusable libraries depend on APIs or the application's emission contract, not on
a particular exporter or global SDK setup. Inject providers into adapters when
practical for independent instances and tests. Bridge an existing language-native
instrumentation facade when it preserves these boundaries; do not force a rewrite.

## Metrics

Choose by meaning: counters accumulate nonnegative occurrences; histograms capture
distributions such as operation latency; gauges represent current measurements;
up/down counters describe additive changes that may be negative. Check language
support for synchronous and asynchronous variants. Create instruments once with
stable names, descriptions and units. Prefer applicable semantic conventions;
document custom business metrics without pretending they are standardized.

Use bounded outcomes and route templates. Customer IDs, job IDs, raw URLs, exception
messages and arbitrary baggage are not metric dimensions. Trace attributes also
need an explicit safe allowlist. Convert elapsed durations deliberately (for example,
milliseconds to seconds); do not derive them by subtracting adjustable wall clocks.

Document whether a measurement counts attempts, unique operations, or deliveries.
At-least-once completion delivery can increment both counters and histograms twice.
Prefer an existing single-emission local boundary for operational metrics; if only
replayable delivery is available, document duplicates or implement a justified
idempotency policy with retention and crash limits. A deduplication marker and an
OTel increment are not an atomic transaction. Billing/audit truth requires its own
durable record. SDK aggregation and OTLP transport do not make counting exactly once.

Emit measurements independently of whether a trace is sampled or recording. Do not
sample a shared event stream used for complete operational outcome metrics.

## Trace lifetime and context

An event's delivery time is not its occurrence time. Carry context at the actual
work boundary; never use a queue consumer's unrelated ambient span as the original
parent. A stored trace ID alone is not full propagation context. Use supported
propagators at transport boundaries and attach/detach context safely across tasks.
Keep baggage bounded and allowlisted; it can cross service trust boundaries.

Let an instrumentation adapter open an operation scope before work, activate its
context during work, and close it on success, error, or cancellation. Structured
start/finish events can also drive a synchronous lifecycle listener when lifetime,
correlation, cleanup, and concurrency are explicit. Keep live span handles local;
do not serialize them in durable events. A completion-only event lacking context
cannot recover parentage: enhance the producer boundary or state the tracing limit.
Use a separate delivery/processing span for later work; use parentage or links
according to causality and the relevant messaging conventions.

Preserve automatic HTTP spans. Configure sampling at SDK composition, respecting
incoming context where appropriate. Set status based on operation semantics;
recording an exception alone does not set error status. Sanitize exception fields,
end spans on all exits, and propagate the original application error unchanged.

## Export and lifecycle

Prefer OTLP with a configurable endpoint, protocol, TLS and authentication. A
Collector is optional; direct export to an OTLP-compatible destination is valid.
Backend-specific transformation belongs at the export/deployment boundary. Keep
secrets out of checked-in examples and telemetry. Inspect the SDK's actual support
for standard settings such as `OTEL_SERVICE_NAME`, `OTEL_RESOURCE_ATTRIBUTES`, and
`OTEL_EXPORTER_OTLP_ENDPOINT`; do not assume all languages implement every variable.
Verify signal-specific overrides and HTTP path versus gRPC endpoint semantics.

Initialize resource identity, providers, metric readers, span processors, and
listeners before observed work. Check required early bootstrap order for automatic
instrumentation. Use SDK batching and periodic metric collection rather than
synchronous network calls for every event. Configure bounded queues, timeouts and
supported retry behavior; document drop behavior during outages. Telemetry remains
best effort unless an explicitly stronger contract is implemented separately.

Drain application work before telemetry shutdown. Flush metrics and traces with
a deadline, then release resources; SDK shutdown/flush ordering is language-specific.
Test short-lived processes and cancellation where applicable. Do not recursively
report exporter failure through the failing exporter. Retain a minimal sanitized
local diagnostic path for startup and telemetry-infrastructure failures.

## Verification

| Boundary | Useful evidence |
| --- | --- |
| Producer | Typed events and business results; commit failure does not emit success |
| Listener | Real SDK measurements and completed spans; units, bounded attributes, status and parentage |
| Sampling/replay | Unsampled work still records metrics; duplicate delivery follows the declared counting contract |
| Composition | First accepted operation reaches registered listeners; task context survives transport |
| Export/lifecycle | Local OTLP receiver observes both signals; unavailable receiver cannot hang work or shutdown |

Use SDK in-memory exporters/readers or structured capture facilities supported by
the chosen version. Explicitly collect/flush when tests require it, avoid real-time
sleeps, and isolate global providers between tests. Inspect typed data rather than
rendered logs or diagnostic JSON. An in-memory span test does not prove OTLP delivery,
and a local receiver test does not prove the configured hosted backend accepts data.

## Official references

Consult the chosen language's current API and SDK documentation before coding:

- [Language APIs and SDKs](https://opentelemetry.io/docs/languages/)
- [Components and export boundaries](https://opentelemetry.io/docs/concepts/components/)
- [Metrics API](https://opentelemetry.io/docs/specs/otel/metrics/api/)
- [Tracing API](https://opentelemetry.io/docs/specs/otel/trace/api/)
- [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- [SDK environment variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/)
- [OTLP exporter configuration](https://opentelemetry.io/docs/specs/otel/protocol/exporter/)
- [Semantic conventions](https://opentelemetry.io/docs/specs/semconv/)
