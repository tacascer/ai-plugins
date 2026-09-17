---
name: design-logging
description: Use when designing or changing application logging, failure reporting, or diagnostic signals and choosing how operational needs should be observed.
---

# Design Logging

Choose diagnostic signals from the operational question, the consumer, and the
action they enable. Read the shared [principles](../../references/principles.md)
before recommending a mechanism.

## Procedure

1. Inspect relevant requirements, code paths, failure handling, diagnostic
   facilities, deployment constraints, and repository conventions. Establish
   what the system already reports and where each signal can operate.
2. Identify the operational question, signal consumer, expected response, and
   failure significance. Trace the proposed signal from its origin through
   delivery to that consumer before selecting a mechanism.
3. Choose a proportionate mechanism using the principles. Explain why it meets
   the need and what information the consumer requires. Preserve explicit
   failure semantics and distinguish exception reporting from direct monitoring
   of business outcomes.
4. For retained logging, specify the event purpose, structured fields, severity,
   emission boundary, sensitive-data exclusions, and relevant delivery failure
   behavior. When infrastructure changes are proposed, address ownership,
   retention, and operating cost.
5. Report the concrete recommendation, rationale, proposed verification
   scenarios, and unresolved assumptions using
   [reporting](../../references/reporting.md). Distinguish checks proposed from
   checks executed, and ask only for missing decisions that change the result.

Use the project's existing tools and language conventions when suitable. Do not
require a vendor, a new infrastructure stack, or a rewrite around functional
abstractions. This workflow does not authorize implementation beyond the user's
request or override applicable development processes.

Consult the [original examples](../../examples/logging-decisions.md) when a
contrasting case helps. This workflow applies to application logging and failure
reporting decisions, not incidental mentions of logs or general observability
platform architecture.
