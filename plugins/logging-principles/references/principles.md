# Logging principles

## Source-derived principles

This section is a concise synthesis of Nikita Sobolev's 2020 article [Do not log](https://sobolevn.me/2020/03/do-not-log). See [sources.md](sources.md) for attribution and the boundary between the article and this plugin's extensions.

- Prevent invalid states where practical, and represent expected failures explicitly so callers can recover intentionally.
- Route important failures to actionable error reporting. Monitor business outcomes directly because a malfunction need not throw an exception.
- Treat each log emission as a fallible side effect and logging infrastructure as a subsystem that needs configuration, delivery, storage, retention, and maintenance.
- Retain logs only when their consumer and purpose justify the cost. Make retained events structured, consistently formatted and severe, safe for their destination, and useful for reconstructing relevant state history.
- Keep justified local diagnostics for constraints such as startup failures and disconnected on-premise operation. The argument against habitual overlogging is not a ban on logs.

## Decision procedure

Start with an operational question, not a logger call. Trace the signal from the event that emits it, through delivery and storage, to a named consumer and action. A mechanism is suitable only when that complete path works in the deployment environment.

| Operational need | Existing mechanism | Proposed signal | Consumer/action | Evidence still needed |
| --- | --- | --- | --- | --- |
| Expected failure with a defined recovery | Explicit result or recovery branch | Preserve the result; add aggregate measurement only if a consumer needs it | Caller performs fallback; owner investigates a sustained rate if defined | Normal rate, escalation threshold, and whether aggregate coverage already exists |
| Important failure | Exception, error result, or incomplete propagation | Actionable error report while preserving the failed outcome | Caller or responder retries, repairs, or surfaces failure | Ownership, delivery coverage, and retry or escalation contract |
| Business outcome can fail without an exception | Business counters, traces, or no signal | Outcome-level metric or check tied to a response | Product or operations owner detects and corrects malfunction | Healthy baseline, decision threshold, and response owner |
| Existing logs have a demonstrated diagnostic use | Structured local or remote events | Retain the smallest useful event history at consistent severity | Support reconstructs the affected operation | Required fields, retention, access, and delivery failure behavior |
| Requirements or consumers are unknown | Undocumented log sites or telemetry | No mechanism choice yet; record the uncertainty | Decision owner identifies the question and expected action | Consumer, environment, current coverage, failure significance, and operating constraints |

For a retained event, define its purpose, emission boundary, structured fields, severity, sensitive-data exclusions, and the surrounding state transitions needed to answer the operational question. Correlation identifiers and stage names often provide more value than large payload snapshots. Keep formatting and severity consistent enough for the consumer to find and interpret the event.

Account for the costs introduced by the signal path: emission can fail or add latency; pipelines can drop, duplicate, or delay events; storage and retention require capacity and ownership; and alerts require tuning and response. More infrastructure is justified only when it improves a demonstrated decision or investigation.

## Practical extensions

The following safeguards are plugin design choices rather than claims from the source article:

- Preserve failure semantics. Removing a log must not turn a caught failure into silent success; retain propagation, recovery, retry, or an explicit failed result.
- Preserve required audit records. They may share a transport with diagnostics, but their purpose, access, retention, and obligations differ.
- Minimize context in every destination, including logs, error trackers, traces, and local bundles. Exclude credentials, secrets, and unnecessary payload data; filtering alone does not establish legal compliance.
- Check environment coverage. A replacement must work during startup and in disconnected deployments before it can displace local diagnostics.
- Handle diagnostic delivery failures according to the application's contract and the signal's importance. Choose behavior from the actual consequence; there is no universal fail-open or fail-closed rule.

Do not prescribe a vendor, a monadic rewrite, or a single mechanism for every failure. When evidence is missing, state what is unknown and ask only for the decision that would change the recommendation.
