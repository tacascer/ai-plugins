---
name: audit-rust
description: Use when reviewing existing Rust patterns, code boundaries, or library usage for concrete correctness or maintainability risks. Applies to Rust design and usage audits, not formatting requests or routine edits merely involving Rust.
---

# Audit Rust patterns

1. Establish the requested scope and contract. Inspect actual dependencies, enabled features, runtime, build tools, relevant production paths, and tests. State what is unavailable.
2. Use the [decision index](../../references/index.md) to read only references relevant to the paths found. Check whether a pattern's review question applies before treating it as a problem. Consult [source notes](../../references/sources.md) for book attribution and current library claims; check pinned versions against primary documentation where API details matter.
3. Trace each possible finding from a concrete code location through its trigger and consequence. Separate confirmed behavior from hypotheses whose caller, runtime, or contract evidence is missing.
4. Report actionable findings in priority order with location, evidence, consequence, smallest useful correction, and a verification idea. Use [reporting](../../references/reporting.md) for coverage limits and uncertainty. When inspected code meets the known contract, report no finding and recommend no change.

A different library preference, missing abstraction, or departure from the book's sample is not itself a defect. Audits are read-only unless the user separately requests changes. Claim compilation, tests, runtime behavior, or security properties only with corresponding evidence.
