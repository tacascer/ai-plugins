# Rust for Rustaceans: evidence and limits

Accessed 2026-09-29. Guidance is original decision-oriented synthesis informed by Jon Gjengset's *Rust for Rustaceans*, corrected by the [author's errata](https://rust-for-rustaceans.com/), and checked against primary documentation. It is not a substitute for the book and includes no redistributed book text or listings.

## Edition and provenance

The originally supplied [GitHub PDF](https://github.com/rustaccato/road-to-being-master-rustacean/blob/main/Rust%20for%20Rustaceans.pdf) is the 2021-07-28 early-access edition: 214 PDF pages, ending at FFI. Its contents announce chapters absent from the file. Chapter numbering differs from the published edition.

The user requested a newer copy. The [published PDF inspected](https://fizmat.space/coding/files/NoStarchPress/Rust_for_Rustaceans_2021_Jon_Gjengset.pdf) contains 283 PDF pages, identifies itself as first printing, copyright 2022, and gives ISBNs 9781718501850 and 9781718501867. The [publisher](https://nostarch.com/rust-rustaceans) lists the November 2021 publication and 280-page book; PDF page count includes front/back matter and is not its printed pagination. The [O'Reilly listing](https://www.oreilly.com/library/view/rust-for-rustaceans/9781098129828/) independently lists all 13 published chapters. This is the completed first edition, not evidence of a second edition or an errata-corrected printing.

Inspected file SHA-256: `c6d10d26e51a1ff7708d801a2bde2db5f0a72ab757bf6175fd1a34534d8acd81`. The PDF stays outside the package. Printed page N corresponds to one-based PDF page N + 26 in this file. The errata ledger uses published page numbers, never early-access chapter numbers.

## Inspected PDF passages

These are selected passage checks, not a claim of exhaustive reading. Each row identifies the passage supporting the topic; recommendations combine that evidence with the current sources below.

| Published chapter | Printed pages inspected | Decision reference |
| --- | --- | --- |
| 1 Foundations | 9, 15–16: destruction and variance | [Ownership](ownership-layout.md) |
| 2 Types | 21, 26, 30: layout, dispatch, coherence | [Interfaces](interfaces.md) |
| 3 Designing Interfaces | 40, 44–45, 49–50: wrappers and contracts | [Interfaces](interfaces.md), [types](types.md) |
| 4 Error Handling | 58: caller recovery | [Errors](errors.md) |
| 5 Project Structure | 68, 70, 81: features and MSRV | [Projects](project-structure.md) |
| 6 Testing | 89, 93, 96: harnesses and augmentation | [Testing](testing.md) |
| 7 Macros | 103, 109: repetition and scope | [Macros](macros.md) |
| 8 Asynchronous Programming | 117, 125, 128: polling and pinning | [Async](async-state.md) |
| 9 Unsafe Code | 142, 144, 156, 158: obligations and initialization | [Unsafe](unsafe.md) |
| 10 Concurrency | 177, 185, 187: atomics | [Concurrency](concurrency.md) |
| 11 FFI | 202, 207: representation | [FFI](ffi.md) |
| 12 Without std | 213–222: allocation, runtime, targets | [no_std](no-std.md) |
| 13 Ecosystem | 224–226, 233–241: tools and reusable patterns | [Projects](project-structure.md), [interfaces](interfaces.md) |

## Primary documentation

Accessed 2026-09-29. Rust online standard-library pages observed here identify Rust 1.98.1; living Reference/Cargo pages have no fixed project version. These access observations do not establish the consumer's toolchain. Check pinned edition, MSRV, features, target, and library versions before emitting version-specific code. Category: **upstream documentation**; design preferences and verification suggestions are **engineering synthesis**.

| Topic | Sources and supported scope |
| --- | --- |
| Lifetimes/layout | [Variance](https://doc.rust-lang.org/reference/subtyping.html), [layout](https://doc.rust-lang.org/reference/type-layout.html): parameter-relative variance and representation guarantees |
| Traits/API | [Traits](https://doc.rust-lang.org/reference/items/traits.html), [coherence](https://doc.rust-lang.org/reference/items/implementations.html), [SemVer](https://doc.rust-lang.org/cargo/reference/semver.html): dyn compatibility, implementation legality, downstream compatibility |
| Borrowing/allocation | [String](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy), [Deref](https://doc.rust-lang.org/std/ops/trait.Deref.html): borrowed input, repaired owned output, implicit API exposure |
| Build | [Features](https://doc.rust-lang.org/cargo/reference/features.html), [MSRV](https://doc.rust-lang.org/cargo/reference/rust-version.html), [configuration](https://doc.rust-lang.org/cargo/reference/config.html): additive flags, rust-version, target-dir |
| Macros | [Declarative](https://doc.rust-lang.org/reference/macros-by-example.html), [procedural](https://doc.rust-lang.org/reference/procedural-macros.html): matching, hygiene, visibility, editions |
| Async | [Future](https://doc.rust-lang.org/std/future/trait.Future.html), [Pin](https://doc.rust-lang.org/std/pin/index.html): Pending/wake contract and address stability |
| Unsafe | [UnsafeCell](https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html), [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.set_len), [exception safety](https://doc.rust-lang.org/nomicon/exception-safety.html): aliasing, initialized length, unwind invariants |
| Synchronization | [Ordering](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html), [AtomicBool](https://doc.rust-lang.org/std/sync/atomic/struct.Atomic.html#method.compare_exchange_weak): synchronization and compare-exchange contracts |
| FFI | [ABI](https://doc.rust-lang.org/reference/abi.html), [NonNull](https://doc.rust-lang.org/std/ptr/struct.NonNull.html), [c_void](https://doc.rust-lang.org/std/ffi/enum.c_void.html): boundary rules and representations |
| Embedded | [Preludes](https://doc.rust-lang.org/reference/names/preludes.html), [alloc](https://doc.rust-lang.org/alloc/index.html), [volatile](https://doc.rust-lang.org/std/ptr/fn.read_volatile.html), [assembly](https://doc.rust-lang.org/reference/inline-assembly.html): no_std scope, allocation, device access, target restrictions |
| Historical predictions | [AsyncIterator](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html), [rustdoc](https://doc.rust-lang.org/rustdoc/unstable-features.html): inspect stability labels rather than treating predictions as guarantees |

## Corrections and later recommendations

The [errata ledger](rustaceans-errata.md) maps every entry visible at access time to its treatment. Guidance incorporates applicable corrections in place. Source-listing typos stay recorded as such; they do not justify rewriting unrelated user code. If an erratum is itself imprecise, check primary documentation (for example, the actual type is `NonNull`).

The author's separate updates mention panic policy, test builders, reading resources, MSRV tooling, snapshots, and prospective APIs. They are recommendations or dated updates, not errata. The plugin treats tools as optional and makes no universal library ranking. For evolving features, prefer the project's documented capabilities; online latest documentation is not proof of MSRV support.
