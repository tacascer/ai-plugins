# Tim skills evaluations

[cases.json](cases.json) combines all 161 existing evaluation cases. Each ID has
its original topic as a prefix, so cases with formerly overlapping IDs remain
unambiguous. Workflow identities use `tim-skills:<skill-name>`; external fixture
plugin identities remain unchanged. `fixture_paths` resolve from the Tim skills
plugin root, including the `evals/<topic>/` prefix.

| Topic | ID prefix | Cases | Guide |
| --- | --- | --- | --- |
| Testing | `testing-principles-` | 35 | [Testing guide](testing-principles/README.md) |
| Time modeling | `time-modeling-` | 16 | [Time guide](time-modeling/README.md) |
| Observability | `design-observability-` | 31 | [Observability guide](design-observability/README.md) |
| Domain models | `domain-driven-design-` | 21 | [Domain guide](domain-driven-design/README.md) |
| Rust | `rust-patterns-` | 38 | [Rust guide](rust-patterns/README.md) |
| GraphQL | `graphql-design-` | 20 | [GraphQL guide](graphql-design/README.md) |

Select a topic's cases by ID prefix before following its guide. References to old
unprefixed case IDs in topic prose refer to that topic's prefixed cases.

Submit only a case's prompt, context, and selected fixture files to the evaluated
model. Keep this directory's case inventory, required/forbidden findings, and
activation expectations in the grader process. Copy only runtime manifests,
skills, references, and examples when isolating plugin guidance. Apply the
selected topic guide's restrictions before exposing that runtime copy. For
GraphQL fixture audits, include `examples/graphql-design/design-decisions.md`
and exclude `examples/graphql-design/audit-findings.md`, which contains worked
fixture answers.

Grade activation telemetry separately from semantic quality. The existing
[result schema](testing-principles/result.schema.json) records observations and
unavailable checks. Preserve uncertainty and record the exact loaded revision.
Moving the cases and updating their identities does not establish a passing live
model run or automatic selection for the combined package.
