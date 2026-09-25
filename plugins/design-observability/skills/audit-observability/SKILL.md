---
name: audit-observability
description: Use when reviewing or investigating application observability, event contracts, telemetry listeners, missing or duplicate signals, misleading metrics, logging, traces, or diagnostic delivery failures.
---

# Audit Observability

Assess the complete path from application facts through structured events and
listeners to signals and consumers. Read the shared
[principles](../../references/principles.md). A useful log is worth preserving;
its existence alone does not prove either a defect or sound architecture.

## Procedure

1. Trace representative operations and failures through event production,
   listener registration, signal mapping, delivery, storage, and consumers.
   Inspect contracts, composition, readiness, shutdown, and relevant tests.
2. Check event meaning, fields, units, correlation, and emission placement.
   Distinguish attempted from committed outcomes, retries from new operations,
   and missing coverage from intentional omissions. Identify unsafe context,
   mutable snapshots, and schema changes that break consumers.
3. Review listener mappings for useful logs, accurate counters and durations,
   bounded metric labels, trace correlation, and actionable error reports.
   Establish whether sampling or duplicate delivery distorts measurements.
   A configured dependency alone does not prove that signals reach consumers.
4. Examine registration before work, listener failure isolation, bounded buffers,
   retry policy, and flush/shutdown behavior where relevant. Identify direct SDK
   calls in application code as a departure from the event/listener boundary;
   explain the concrete coupling or inconsistent-policy risk and recommend a
   proportionate migration that preserves useful signals. Do not invent an
   incident or demand a broker.
5. Check every direct-diagnostic exception against infrastructure availability.
   Preserve minimal startup or initialization output when the event path is
   unavailable, and identify when normal emission takes over. A small application
   or disconnected destination alone does not justify bypassing available local
   listeners. Preserve required audit records and application failure semantics.
6. Review tests for structured event and application-outcome assertions,
   listener mapping checks through structured records or measurements, and
   actual composition coverage. Replace rendered log-string or diagnostic-JSON
   assertions with these boundaries; do not infer delivery from unit tests alone.
7. Report prioritized findings using [reporting](../../references/reporting.md):
   evidence, trigger, consequence, proportionate correction, and verification.
   Separate confirmed defects, architectural gaps, conditional risks, and missing
   evidence. Identify useful signals and justified fallback diagnostics to retain.

Consult the [examples](../../examples/observability-decisions.md) as needed.
Keep the audit read-only unless edits are requested. With abstract scenarios,
cite supplied facts without inventing source locations or runtime results.
Do not equate undocumented consumers with useless signals. State examined scope
and say when no material issue is established. Incidental telemetry mentions and
standalone vendor/platform administration are outside this workflow.
