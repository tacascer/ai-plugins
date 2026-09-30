# Evidence and reporting

For design, provide the relevant SDL, resolver contracts, rationale, assumptions,
proposed verification queries, and a client migration sequence where an existing
contract would change. Label undecided product policies and conditional examples.
A proposed query is not evidence that it ran.

For audit, report confirmed findings in priority order. Each finding names the
location or supplied contract/trace, a triggering query or input, the observed
or implied consequence, evidence, and a practical correction. Group formal
specification violations separately from engineering recommendations. Put gaps
in schema, resolver, test, or runtime evidence in a distinct coverage note; do
not turn missing evidence into a pass or a confirmed defect. If the supplied
contracts satisfy the relevant rules, say there are no evidenced violations.

| Evidence | Safe conclusion |
| --- | --- |
| SDL or introspection only | Schema shape can be assessed; ID uniqueness, refetch, ordering, slicing, and flags remain unverified. |
| Resolver code | Trace the implemented branches; behavior requiring external state may still need execution. |
| Supplied response trace | Describe what that trace proves and its limits; do not claim you ran it. |
| Executed query/test with result | Report the exact observed result and environment. |

An audit is read-only unless the user separately requests fixes. Do not claim a
query, test, or model evaluation ran unless there is execution evidence.
