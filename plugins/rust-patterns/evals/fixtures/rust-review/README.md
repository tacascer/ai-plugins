# Document-processing service excerpts

These independent excerpts describe part of an existing Rust service that
accepts documents, generates previews, stores document metadata and a delivery
receipt, and notifies a remote indexing service. They are audit inputs, not a
buildable crate. There is no `Cargo.toml`, module graph, database schema,
startup wiring, network implementation, or test suite here. Compilation and
behavior of omitted code are unverified.

The service's contracts are:

- A `DocumentName` must be nonempty after trimming whitespace, regardless of
  whether it comes from HTTP, stored JSON, or an internal call.
- A preview request may run concurrently with other requests. Its local cache
  protects only short metadata updates; a slow indexing call must not hold up
  unrelated cache updates.
- Once a document is accepted, its indexing notification is service-owned:
  the service must observe a failed notification for retry or operator action,
  and graceful shutdown must drain accepted notifications before returning.
- The remote indexing service may accept a publication before its response
  arrives. A local timeout does not tell the service whether that happened.
  Retries must account for that uncertainty.
- The service sends many notifications to the same remote HTTP origin.
- The document row and its delivery receipt must become visible together, or
  neither may become visible.
- Request correlation is useful in diagnostics, but authorization credentials
  must not be recorded in spans or logs.

Snippet dependency context: the code sketches APIs from `serde` 1,
`serde_json` 1, `tokio` 1, `reqwest` 0.13, `sqlx` with PostgreSQL support,
and `tracing` 0.1. A project's
exact pinned versions and features would need checking before API-level fixes.
Symbols such as `RemoteIndexer` and `DocumentId` stand for omitted service
interfaces. The excerpts intentionally leave retry storage, deployment, and
authentication implementation outside the visible scope.
