# Example: asynchronous job completion

A service already emits `JobCompleted(job_id, customer_id, outcome, finished_at,
elapsed_ms)` onto a delayed, at-least-once stream. HTTP requests are automatically
traced. Operators want completion counts, latency, and tracing across queued work.

The completion event lacks propagation context, and replay can duplicate metrics.
Instrument the actual execution boundary using an application-facing scope and a
local synchronous event listener. Keep the replayable stream for its existing
consumers. This sketch is language-neutral pseudocode, not a particular SDK API:

```text
composition:
    sdk = configure_otel(resource_identity, configurable_otlp_export)
    metric_listener = JobMetrics(sdk.meter)
    local_events.register(metric_listener)       # before work is accepted
    observation = JobObservation(sdk.tracer, propagator)

queue adapter:
    publish(job, propagation_headers=observation.inject_current_context())

worker adapter:
    parent = observation.extract_context(message.headers)
    with observation.job_scope(parent):         # span active while work runs
        execute_job(job, local_events)

execute_job(job, events):                       # application has no OTel imports
    started = monotonic_clock.now()
    outcome = failure
    try:
        result = perform_and_commit(job)
        outcome = success
        return result
    finally:
        events.emit(JobAttemptFinished(
            outcome, elapsed=monotonic_clock.now() - started))

JobMetrics.on(JobAttemptFinished event):
    attributes = {outcome: bounded(event.outcome)}
    attempt_count.add(1, attributes)
    duration_seconds.record(to_seconds(event.elapsed), attributes)
```

The dispatcher isolates diagnostic listener failures. The observation scope marks
errors according to operation semantics, closes on every exit, and preserves the
original exception. Cancellation receives its own bounded outcome when meaningful.
A job retry is another attempt; these metrics are not unique-job or billing counts.
The span adapter owns OpenTelemetry calls and safe context attachment. The existing
HTTP server span stays owned by automatic instrumentation.

With 10% trace sampling, the metric listener still receives every local completion.
It never keys labels by job/customer IDs. Delayed `JobCompleted` redelivery changes
neither these attempt metrics nor the original execution span. If the producer
cannot be changed, report that missing historical trace context cannot be recovered;
do not manufacture parentage or claim exactly-once completion metrics.

Verify a success and a failure through normal composition, then check typed metric
values and completed spans with local SDK captures. Exercise unsampled execution,
queue propagation, redelivery, and a blocked exporter with bounded shutdown. Change
the OTLP destination to a local receiver to verify wire export separately. No hosted
account is needed, and no production deployment is implied.
