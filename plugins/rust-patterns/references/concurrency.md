# Concurrency and atomics

**Fit.** Separate concurrency (overlapping progress) from parallel execution. Keep serial work when coordination costs exceed measured benefits. Choose a mutex for a shared invariant, channels for ownership transfer, and bounded workers for independent jobs. Define queue limits, failure observation, and shutdown.

**Thread contracts.** `Send` concerns moving values between threads; `Sync` concerns shared references being usable across threads. Reference counting does not make the contents thread-safe. An `unsafe impl Send` or `Sync` requires an argument covering all methods, destruction, callbacks, and foreign thread-affinity requirements. Review lock ordering and reentrancy, not only data races.

**Atomics.** State the invariant and synchronization event before choosing orderings. `Relaxed` gives atomic access without publishing unrelated memory. An acquire operation that observes the relevant release (or release sequence) can establish synchronization; wall-clock ordering alone cannot. Read-modify-write success and failure orderings have different restrictions. `SeqCst` does not make a multi-step protocol atomic or fix lifetime reclamation. [Ordering](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html).

A separate load followed by a store is not lock acquisition. A weak compare-exchange may fail spuriously; retry using the observed value and re-evaluate dependent work. Do not infer that a matching current value proves no intervening changes occurred (ABA). Prefer established synchronization to an unproven custom primitive. [AtomicBool](https://doc.rust-lang.org/std/sync/atomic/struct.Atomic.html#method.compare_exchange_weak).

**Cleanup.** If a custom lock uses `true` for held, its guard must release the same atomic to `false`, with publication ordering paired with acquisition. Check unwinding and every exit. Correcting that one store does not establish a complete mutex proof. A non-panicking ordinary callback test alone misses cleanup failures.

**Verification.** Test contracts at the ownership boundary and use a model checker such as Loom for small protocols when supported. Stress tests sample schedules; they do not prove absence of races or deadlocks. Measure throughput and latency against the serial baseline before recommending parallelism.

[Book evidence](rustaceans-sources.md#inspected-pdf-passages) · [Corrections](rustaceans-errata.md)
