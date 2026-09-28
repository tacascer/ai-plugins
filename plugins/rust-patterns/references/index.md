# Choose a Rust decision reference

Read only the reference matching the decision at hand. These are patterns and library decision criteria, not a required stack. Check the repository's pinned versions, features, build targets, tests, and explicit architecture before suggesting an API or migration. See [source evidence and limits](sources.md) for book attribution and current primary documentation.

| Decision | Read |
| --- | --- |
| Invariants, newtypes, construction, ownership | [Types and boundaries](types.md) |
| Caller recovery, context, HTTP failure mapping | [Errors](errors.md) |
| Task lifetime, blocking, deadlines, shared state | [Async and state](async-state.md) |
| Startup settings, deserialization, secrets | [Configuration](configuration.md) |
| SQL interfaces, pools, transactions, migrations | [Persistence](persistence.md) |
| Handlers, middleware, outgoing clients | [HTTP](http.md) |
| Spans, safe diagnostics, reporting ownership | [Observability](observability.md) |
| Password verification and browser sessions | [Authentication](authentication.md) |
| Test scope, dependencies, property generation | [Testing](testing.md) |
| Design or audit answer shape | [Reporting](reporting.md) |

The [type and error example](../examples/type-and-error-boundaries.md) and [async and I/O example](../examples/async-and-io-decisions.md) connect several decisions in one original document-processing setting. Load them only when a concrete shape would help. If evidence is partial, state the visible failure mechanism and the missing call site; do not promote a possibility to a confirmed defect. A simple standard-library solution that satisfies the contract needs no pattern upgrade.
