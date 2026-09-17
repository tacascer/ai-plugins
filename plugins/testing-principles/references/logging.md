# Testing logging behavior

Treat logging according to its consumer and contract. The presence of a logger, a log level, or a file sink does not establish that a call deserves an assertion.

## Direct advice from the author’s articles

Khorikov’s [dependency guide](https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/) explicitly includes loggers in the advice to inject dependencies. His [code pollution example](https://enterprisecraftsmanship.com/posts/code-pollution/) substitutes a logger to avoid incidental file writes during a test, instead of adding a production test-environment switch. [When to Mock](https://enterprisecraftsmanship.com/posts/when-to-mock/) distinguishes externally observable contracts from internal communications.

## Applying those principles to logging

The following decision procedure is this plugin’s application of those articles, not a verified summary of the book’s section 8.6. Here, “diagnostic” means incidental developer diagnostics and “support” means a demonstrated consumer requirement; names and severity alone do not decide which applies.

| Evidence | Test decision |
| --- | --- |
| A debug message only describes internal execution; no consumer contract depends on it | Assert the operation’s result or observable state. Supply a no-op logger if needed to avoid incidental I/O; do not verify its wording or call count. |
| Support tooling or another consumer relies on an event and specified fields or emission conditions | Preserve tests for that contract. At an unmanaged boundary, a recorder or mock can verify the outgoing event. Verify exact text, severity, count, or order only when each is part of the demonstrated contract. |
| Storage is owned and hidden behind the application | Apply the managed-dependency rule: use real storage in integration checks when practical and inspect observable results. A mock does not establish persistence or delivery. |
| Consumers or requirements are unknown | Keep the conclusion conditional. Inspect readers, parsers, support workflows, and compatibility promises before removing coverage or requiring logger assertions. |

Use existing injection or composition seams. A static or internally constructed logger can hide I/O; introduce the smallest useful explicit boundary within the authorized scope. Preserve production wiring and failure behavior. Do not add an `isTestEnvironment` branch to skip logging. A substitute alone does not verify the real adapter or delivery path.

Classify assertions independently of their value: a spy verifying emissions is communication-based; reading a resulting record is state-based; combining either with a returned-value assertion is mixed. Scope still depends on the exercised boundary and isolation. Neither a mock logger nor a real file determines scope by itself.

See [logging examples](../examples/logging.md), [test seams](test-seams.md), and [sources](sources.md). Retaining or removing a test assertion is a separate decision from changing production logging.
