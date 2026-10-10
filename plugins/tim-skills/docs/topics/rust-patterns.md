# Rust Patterns

This plugin helps Codex and Claude Code choose and review practical Rust patterns,
code boundaries, and library usage. It covers decisions about validated types,
errors, async work, configuration, persistence, HTTP, observability,
authentication, and testing, plus ownership and layout, trait APIs, macros, unsafe
contracts, concurrency, FFI, and no_std. It adapts to the project's dependencies, runtime,
framework, and build tools; a sound simple implementation can need no change.

The guidance draws on Luca Palmieri's *Zero to Production in Rust*, Jon Gjengset's
*Rust for Rustaceans*, and original engineering synthesis. [Source notes](../../references/rust-patterns/sources.md) identify the
book-derived principles, current primary documentation, independently researched
alternatives, access dates, and limits. The plugin does not include the book or
claim that historical library choices are current defaults. The
[Rustaceans source map](../../references/rust-patterns/rustaceans-sources.md) identifies the inspected
published first edition and all 13 chapter areas; the [correction ledger](../../references/rust-patterns/rustaceans-errata.md)
tracks all 37 errata entries visible on 2026-09-29.

## Workflows

- `design-rust` helps choose a pattern and library treatment for a concrete Rust
  behavior or boundary. It compares the simplest adequate option with relevant
  alternatives and explains failure behavior and verification.
- `audit-rust` reviews existing Rust usage against actual contracts and code
  paths. It reports evidenced findings and coverage limits, or no change when
  the inspected design is sound. Audits are read-only unless edits are requested.

The skill descriptions allow matching tasks to select a workflow automatically;
live selection has not been verified. The [initial verification record](../rust-patterns/verification/2026-09-28-initial.md)
separates package checks from model behavior. Invoke a workflow explicitly as follows:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Design | `$tim-skills:design-rust` | `/tim-skills:design-rust` |
| Audit | `$tim-skills:audit-rust` | `/tim-skills:audit-rust` |

Each workflow works independently. The collection README has local loading
instructions.

## Guidance and evaluation

The [decision index](../../references/rust-patterns/index.md) routes to focused references; read
only those needed for the task. The original [type and error](../../examples/rust-patterns/type-and-error-boundaries.md)
and [async and I/O](../../examples/rust-patterns/async-and-io-decisions.md) examples illustrate
trade-offs without prescribing a stack. The [evaluation guide](../../evals/rust-patterns/README.md)
defines 38 authored cases, including an unrelated-task case and a small Rust
audit fixture. The cases and structural checks do not establish live activation
or semantic behavior; both live Claude attempts stopped at authentication
before model inference, and the user chose to stop Claude testing. The
verification record documents these limits.

The [library boundary example](../../examples/rust-patterns/library-boundaries.md) adds executable
borrowing, dispatch, and unwind behavior checks. The [Rustaceans verification
record](docs/verification/2026-09-29-rustaceans.md) records the expansion's checks
and limits separately from the initial platform attempts.
