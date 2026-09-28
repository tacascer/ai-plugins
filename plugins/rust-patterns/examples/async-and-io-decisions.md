# Document-processing I/O decisions

These original, incomplete sketches show where ownership and failure boundaries belong. They are illustrative fragments, not a buildable service. API-specific context: Tokio 1 with `rt`, `time`, and needed I/O features; reqwest 0.13 with the project's TLS choice; SQLx with its pinned PostgreSQL features. Check the repository's lockfile, build targets, and adapter APIs before applying them. [Async and state](../references/async-state.md), [persistence](../references/persistence.md), [HTTP](../references/http.md), and [source notes](../references/sources.md) provide the decision criteria.

## A small shared-state implementation

The following complete standard-library program shows a short metadata update. The lock is released at the block boundary before an external async operation would start. A real service can use its existing cache and state conventions.

```rust
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

type Cache = Arc<Mutex<HashMap<u64, String>>>;

fn set_status(cache: &Cache, id: u64, status: &str) {
    let mut entries = cache.lock().expect("cache mutex poisoned");
    entries.insert(id, status.to_owned());
} // guard ends here

fn main() {
    let cache = Cache::default();
    set_status(&cache, 7, "queued");
    assert_eq!(cache.lock().unwrap().get(&7).map(String::as_str), Some("queued"));
}
```

In an async handler, finish this local update before `remote.index(id).await`. If the contract requires local and remote state to move together, a mutex across the network wait is still not an atomic cross-system transaction; design ordering, idempotency, and reconciliation instead. Pick a sync or async lock for the actual critical section and workload, not by the presence of `async fn` alone.

## Deadlines and blocking work

For a synchronous renderer inside an async request, bound concurrency before `tokio::task::spawn_blocking(move || render_preview(bytes))`; observe its join result. A Tokio timeout on the awaiting future does not stop a blocking job that has already started. Use an async file API when it fits the workload. [Tokio's documented limits](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html) govern this choice.

An illustrative remote call is `tokio::time::timeout(deadline, remote.publish(id)).await`. An elapsed deadline says the local future stopped waiting; the remote may have accepted the publication. Record an operation key before sending, make duplicate attempts safe where the remote contract allows it, or reconcile status before retrying. Do not report “publish rolled back” from a local timeout. [Tokio timeout source](https://docs.rs/tokio/latest/tokio/time/fn.timeout.html).

## Reuse and atomic local writes

Create a configured `reqwest::Client` once in service state and clone its handle for repeated notifications. The client already owns a connection pool; constructing one for every send forfeits reuse across sends. [reqwest client source](https://docs.rs/reqwest/latest/reqwest/struct.Client.html).

When a document row and delivery receipt must appear together, begin one database transaction, execute both writes through that transaction, then commit after both succeed. Inject failure between writes and assert neither row becomes visible. An external indexing request remains outside the local database transaction; use an outbox or another explicit coordination design only when the stated delivery contract needs it. [SQLx transaction source](https://docs.rs/sqlx/latest/sqlx/struct.Transaction.html).
