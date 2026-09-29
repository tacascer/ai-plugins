# Foreign function interfaces

**Fit.** Use when Rust and another language exchange functions, pointers, or data. Establish the actual foreign header, ABI, target, linker inputs, ownership rules, and callback lifetime before selecting Rust types. Generated bindings still require this contract review.

**Representation.** Use the target's C-compatible types, an explicit calling convention, and suitable `repr` where layouts cross the boundary. `repr(C)` is not a blanket guarantee that arbitrary nested Rust fields are FFI-safe. Rust `String`, `Vec`, and trait-object representations are not portable C interfaces. Keep allocation and deallocation with the correct allocator; transfer explicit handles or pointer/length pairs with documented ownership. [ABI](https://doc.rust-lang.org/reference/abi.html).

A nullable raw pointer already admits null; do not assume `Option<*mut T>` has the same representation as that pointer. `Option<NonNull<T>>` has the documented niche guarantee, and the type is named `NonNull`, not the errata's spelling `NotNull`. Check the complete function signature and target contract separately. Non-null does not imply dereferenceable. [NonNull representation](https://doc.rust-lang.org/std/ptr/struct.NonNull.html#representation).

An opaque `*mut c_void` is not a pointer to a zero-sized `()` object. Transparent wrappers must meet their representation rules; an opaque handle's pointee need not be instantiated or dereferenced in Rust. Use distinct handle types to prevent mixing foreign resources, with explicit constructor and destructor pairing. [c_void](https://doc.rust-lang.org/std/ffi/enum.c_void.html).

**Safety boundary.** Check null, length, alignment, validity, and lifetimes before constructing references or slices. Keep callback state alive until deregistration guarantees callbacks have stopped; inspect foreign thread affinity before asserting `Send`/`Sync`. Specify unwind behavior at the ABI boundary and translate recoverable failures deliberately. Do not assume `catch_unwind` catches aborts or all foreign exceptions. Edition-specific extern and exported-symbol syntax must match the pinned toolchain.

**Verification.** Compile and link a real foreign consumer against the header on supported targets. Exercise allocation/free pairing, null and empty input, callback teardown, and failure paths. A Rust-only size assertion or successful bindings generation is insufficient to establish cross-language compatibility.

[Book evidence](rustaceans-sources.md#inspected-pdf-passages) · [Corrections](rustaceans-errata.md)
