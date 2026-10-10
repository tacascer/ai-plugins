# HTTP boundaries

**Problem and fit.** A handler should parse transport input, call application behavior, and map failures to stable public responses. Use the service's existing framework, extractors, state model, and middleware conventions when they meet the need. Middleware suits cross-cutting request behavior such as correlation or authentication; domain decisions belong in application code. [Book principle](sources.md#verified-book-principles).

**Server options.** Actix Web's `web::Data` and application factory can share or instantiate state at different worker scopes. Axum's `Router::with_state` and `State` are a typed alternative for a new or constrained stack. This is a choice about integration, not a migration instruction. Check pinned API and build targets, including Bazel targets and imported dependency metadata when that is how the repository builds. [Primary sources](sources.md#current-primary-sources-and-bounded-alternatives).

**Outgoing calls.** Construct a configured client at service scope for repeated calls; reqwest's `Client` contains a reusable connection pool and its clones share the underlying client. Define connect/request deadlines and map response statuses deliberately. A timeout or lost response leaves remote completion uncertain; retry only with a contract that handles duplicates or supports reconciliation. Keep credentials out of URLs, spans, and error output. [reqwest source](sources.md#current-primary-sources-and-bounded-alternatives); [async consequences](async-state.md).

**Review questions.** Do extractors distinguish parsing from domain validation? Is each status safe and actionable? Are middleware and handlers responsible for the right facts? Is a client recreated for every call? Can a retry duplicate a remote effect?
