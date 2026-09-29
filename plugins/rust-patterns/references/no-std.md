# Rust without the standard library

**Fit.** Use when the deployment target or reusable-library contract excludes `std`. The published edition’s chapter 12 informs this guidance; current primary documentation governs toolchain details.

**Capability boundary.** Separate a `core`-only API, optional `alloc` conveniences, and optional `std` integration. `#![no_std]` changes the implicit standard-library linkage and prelude; it is not by itself proof of an allocation-free dependency graph. `alloc` supplies heap-backed types but needs allocator support in the final environment. Prefer caller-provided buffers, slices, and iterators when allocation is forbidden. Put OS I/O, threads, and platform setup outside the portable core. [Preludes](https://doc.rust-lang.org/reference/names/preludes.html#the-no_std-attribute) · [alloc](https://doc.rust-lang.org/alloc/index.html).

**Features.** A common contract has additive `alloc` and `std` features, with `std` enabling `alloc` if that matches the API. Gate allocation-dependent exports and dependencies together. Inspect transitive default features: another dependency edge can re-enable `std`. Keep [MSRV and feature promises](project-structure.md) explicit instead of claiming every target is supported.

**Final artifact.** A reusable library generally leaves panic handling, allocator selection, entry point, and linker configuration to its final binary and target runtime. Check target atomic availability and platform APIs; compiling without `std` does not supply an embedded runtime or guarantee thread support.

**Hardware access.** Volatile operations preserve device-access effects but are not thread synchronization. Interrupts and shared device state need their own exclusion protocol. Use a hardware abstraction with ownership or typestate where it prevents invalid register sequences; a plain mutable static flag is not a concurrency proof. Verify inline assembly support for the actual target rather than repeating the book-era nightly restriction. [Volatile](https://doc.rust-lang.org/std/ptr/fn.read_volatile.html) · [Assembly](https://doc.rust-lang.org/reference/inline-assembly.html).

**Verification.** Check the library with no defaults on a supported target without `std`, then separately check `alloc` and `std` configurations promised by the package. A host test harness can use `std`, so passing host tests does not establish the deployment contract. Verify the final consumer's target build, including runtime and linker requirements, where in scope.

[Source limits](rustaceans-sources.md) · [Corrections](rustaceans-errata.md)
