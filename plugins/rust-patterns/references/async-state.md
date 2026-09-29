# Async work and shared state

**Problem and fit.** Async code must make task ownership, blocking work, deadlines, and state lifetimes explicit when requests run concurrently. Keep a simple direct `await` when no independent task is needed. For spawned work, identify who observes failure, owns shutdown, and cancels or drains it; dropping an unobserved handle is not a lifecycle plan.

**Shape and options.** A blocking file read or expensive password operation on an executor worker delays other futures. Prefer a suitable async I/O API for genuinely async I/O; use bounded blocking execution for synchronous APIs and limit CPU-heavy concurrency. Tokio's `spawn_blocking` moves work off executor workers, but already-started work normally cannot be aborted and its default blocking-thread allowance is large. Check the project's runtime, feature set, and workload before naming an API. [Tokio source](sources.md#current-primary-sources-and-bounded-alternatives).

**Cancellation and failure.** A timeout drops a local future; an external service may already have accepted its request. Retries need idempotency keys, status lookup, or reconciliation when outcomes are uncertain. A database transaction protects only its own database scope; it does not roll back a remote publication. Bound each stage, record enough safe correlation to investigate, and define what happens after cancellation. [Tokio source](sources.md#current-primary-sources-and-bounded-alternatives).

**Shared state.** Establish whether state is shared across workers or built per worker; framework factories can change the lifetime. Use a mutex only when mutation needs exclusion, and choose sync or async locking according to the critical section and runtime. Keep critical sections short: release a cache guard before awaiting a remote call unless a documented ordering requirement needs another design. Reuse configured clients and pools across requests where supported rather than rebuilding them per call. See [HTTP](http.md) and [the I/O example](../examples/async-and-io-decisions.md).

**Review questions.** Where can execution block? Who owns each task? Does a deadline leave remote effects uncertain? Does a guard live across `.await`? Is shared state constructed at the intended worker scope? Are limits and shutdown behavior tested?

## Futures and pinning

A future is driven by polling, not merely by constructing it. On `Pending`, retain the in-progress state and arrange for the current task to be woken when progress is possible. A wake is a scheduling notification, not proof of completion; a later poll can still return `Pending`. Do not spin-poll or recreate an in-flight operation on each poll. Once `Ready` is returned, generic callers must not assume repolling is permitted. Prefer compiler-generated async state machines to manual futures unless the abstraction needs one. [Future contract](https://doc.rust-lang.org/std/future/trait.Future.html).

`Pin<P>` constrains movement of the pointee, not of the pointer handle. `Unpin` changes which restrictions matter; pinning is neither shared ownership nor a guarantee of thread safety. Use safe pinning/projection facilities where possible and inspect any unsafe projection and destructor together. [Pin](https://doc.rust-lang.org/std/pin/index.html).

The book's receiver names and generator syntax are explanatory examples, not a runtime API specification. Use actual dependency methods; do not rename a real `recv` method because the errata standardizes the book's fictional receiver to `next`. Check runtime-specific cancellation and `Send` requirements. [Book evidence and corrections](rustaceans-sources.md).
