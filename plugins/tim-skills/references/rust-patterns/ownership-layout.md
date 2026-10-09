# Ownership, lifetimes, and layout

**Fit.** Use this reference when a borrow outlives its owner, an API overconstrains lifetimes, or code depends on representation. Start with ownership and access requirements, not with adding `clone`, `Arc`, or `'static` until the compiler accepts the code.

**Decisions.** Borrow for temporary access; own values that must survive their source. `T: 'static` rules out non-static borrowed dependencies; it does not require keeping an owned value alive forever. Separate lifetime parameters when an output depends on one input but not another. Check actual last uses and destructor behavior rather than equating every lifetime with its lexical scope. A value declared earlier can borrow a later value if the required ordering is satisfied, including explicit early destruction where needed.

Subtyping means a value is at least as usable in the required context, not necessarily strictly more capable. Variance is relative to a particular type or lifetime parameter. For `&'a mut T`, distinguish covariance in `'a` from invariance in `T`; shortening the borrow is not permission to replace the referenced value's type. A lifetime used in a subtyping example may be concrete rather than universally quantified. Use a small compile-pass/compile-fail example to check an API restriction before recommending extra parameters. [Rust Reference](https://doc.rust-lang.org/reference/subtyping.html).

**Representation.** Default Rust layout is not a wire format or a stable foreign ABI. Check alignment, padding, valid bit patterns, and the exact `repr` guarantee before reinterpreting bytes. `repr(C)` does not recursively change nested types or make pointers serializable. `repr(packed)` does not make unaligned references legal. A slice or trait object carries metadata; do not hard-code pointer sizes from a single target. Prefer parsing bytes into fields when no measured requirement justifies layout-dependent code. See [FFI](ffi.md) and [unsafe contracts](unsafe.md).

**Verification.** Compile lifetime examples against the project's edition and MSRV; inspect layout on each supported target if the ABI depends on it. A successful size assertion on one build establishes only that observation. Trace ownership through drop and cancellation, not just the happy path.

[Book evidence](rustaceans-sources.md#inspected-pdf-passages) · [Corrections](rustaceans-errata.md)

**Iterator receiver.** Implement `Iterator::next` with `&mut self`; yielded references must have the intended source lifetime rather than an unnecessarily short borrow of unrelated iterator configuration.
