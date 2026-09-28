---
name: design-rust
description: Use when choosing or revising Rust code boundaries, patterns, or library usage for a concrete behavior, including types, errors, async work, HTTP, and persistence. Applies to design decisions, not every request that touches a Rust file.
---

# Design Rust patterns

1. Establish the behavior, contract, constraints, and specific engineering decision. Inspect relevant code, dependency versions and features, runtime, build tools, tests, and stated architecture before selecting an approach. Treat unavailable details as assumptions.
2. Use the [decision index](../../references/index.md) to read only relevant references. Consult [source notes](../../references/sources.md) before attributing a recommendation to *Zero to Production in Rust* or claiming a current library capability. Verify version-sensitive advice against the project's pins and primary documentation; when that is unavailable, stay at the pattern level and state the limit.
3. Compare the simplest adequate choice, including the standard library where sufficient, with meaningful alternatives. Keep a sound existing framework, dependency, or build workflow unless the requirement justifies change.
4. Propose the pattern and library treatment, ownership and data flow, failure behavior, and a small illustrative example when it helps. Explain the trade-off and smallest verification of the contract. Use [reporting](../../references/reporting.md) for answer shape and unresolved assumptions.

Follow the user's requested development scope. Design advice alone does not authorize implementation, installation, or migration. Do not add an approval ceremony to an otherwise authorized task.
