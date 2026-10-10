# Sources and authority

Accessed 2026-09-30. These links are attribution for an original synthesis, not
bundled upstream text or a claim of Meta endorsement.

| Source | Version and access | Governs |
| --- | --- | --- |
| [Relay GraphQL server guide](https://relay.dev/docs/v20.1.0/guides/graphql-server-specification/) | v20.1.0, accessible on 2026-09-30. The [unversioned URL](https://relay.dev/docs/guides/graphql-server-specification/) timed out during the initial review and returned an access error during implementation. | Introductory refetch and connection assumptions; examples are illustrative, not the detailed rule source. |
| [Global Object Identification Specification](https://relay.dev/graphql/objectidentification.htm) | Unversioned formal specification, inspected directly 2026-09-30. | Reserved `Node` and `node` shapes (§§1–3), field stability (§4), optional plural identifying root fields (§5). |
| [GraphQL Cursor Connections Specification](https://relay.dev/graphql/connections.htm) | Unversioned formal specification, inspected directly 2026-09-30. | Reserved connection and edge shapes (§§1–3), argument pairs and pagination algorithm (§4), `PageInfo` and direction-dependent flags (§5). |

No immutable revision is supplied for either unversioned formal specification.
Their exact text may change after this access date. The references in this
package paraphrase the inspected rules and should be rechecked against the linked
specifications when a consequential ambiguity appears. [Identification](identification.md)
and [connections](connections.md) label formal requirements and optional features;
[principles](principles.md) and [reporting](reporting.md) also distinguish independent
engineering advice. Authorization, business ordering, visibility scope, and
migration planning are engineering or product decisions, not extra Relay rules.
