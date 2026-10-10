# Reporting observability decisions

Separate inspected facts, recommendations, assumptions, and checks actually
executed. Scale the report to the request; do not turn every small change into
an infrastructure proposal.

## Design

Include the operational question, consumer and response, then the concrete path:

| Event and emission boundary | Contract/fields | Listener and signal | Consumer/action |
| --- | --- | --- | --- |
| Meaningful fact and when it becomes true | Outcome, units, safe correlation context | Mapping and destination | Who uses it and why |

Explain composition and relevant delivery guarantees, failure behavior, retention,
and cost. Name each infrastructure-availability exception, its fallback, and the
handoff to normal emission. State verification at producer, listener, and
composition boundaries, followed by unresolved assumptions. A proposed check is
not an executed check.

## Audit

For each prioritized finding, give inspected evidence, concrete trigger and
consequence, proportionate correction, confidence, and verification. Use file and
line references when available; for abstract scenarios cite the supplied facts.
Distinguish confirmed defects from architectural gaps, conditional risks, and
missing evidence. Direct SDK calls can establish coupling without proving lost
telemetry; undocumented consumers do not prove a signal is useless.

Identify useful signals and justified direct diagnostics to preserve. State the
examined scope and say when no material issue is established. Keep audit output
read-only unless implementation is also requested.
