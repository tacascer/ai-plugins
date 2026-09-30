# GraphQL Design plugin design

Date: 2026-09-30

Status: conversational design approved; written spec awaiting user review.

## Intent and success criteria

Create an independently installable `graphql-design` plugin for Codex and Claude
Code with `design-graphql` and `audit-graphql` skills. The user selected design
and audit, Relay compatibility as a required baseline, and this package name.
Both workflows are language- and framework-agnostic.

Success means agents can propose actionable GraphQL schemas and resolver
contracts, or identify evidenced compatibility violations in existing APIs.
Guidance must distinguish formal requirements, optional specification features,
and additional engineering recommendations. Valid designs should receive a
no-findings assessment rather than preference-driven changes.

## Scope and sources

The baseline covers object identification, refetching, cursor connections,
pagination ordering, and page metadata. Source anchors are:

- [Relay server guide](https://relay.dev/docs/guides/graphql-server-specification/).
- [Global object identification](https://relay.dev/graphql/objectidentification.htm).
- [Cursor connections](https://relay.dev/graphql/connections.htm).

The unversioned guide timed out during initial research; its
[v20.1.0 version](https://relay.dev/docs/v20.1.0/guides/graphql-server-specification/)
was accessible through search. Both formal specifications were inspected directly
on 2026-09-30. Record source versions/access dates in the authored source notes;
verify detailed claims against the formal specifications during implementation.
Write original summaries and examples, with attribution and no claim of Meta
endorsement. Do not bundle upstream documents.

Object identification guidance covers the exact `Node` interface and
`node(id: ID!): Node` root contract, global uniqueness, refetching the same object,
nullable unavailable results, and field stability for repeated identities within
a query. Plural identifying fields are optional; explain their correspondence
rules when present. Base64 is a convention, not a required ID encoding.

Connection guidance covers reserved connection types, edge and cursor fields,
`PageInfo`, pagination argument pairs, slicing semantics, and page boundaries.
Forward-only, backward-only, and bidirectional connections are permitted.
Backward pagination preserves the same edge ordering. An edge's `node` need not
implement `Node`. Cover zero and negative sizes, empty pages, cursor bounds,
combined slicing, and the direction-dependent page-flag requirements and allowed
efficiency concessions. Preserve specification distinctions between required
fields and optional nullability choices.

Required baseline does not mean every object implements `Node` or every list is
a connection. Explain which application objects need refetching and which
relationships need pagination. Do not silently relax the baseline because the
application currently has no Relay client.

Broader GraphQL topics appear only where they affect these contracts. For
example, authorization must remain effective through refetching, and pagination
needs a defined ordering and visibility scope. Label such engineering guidance
separately from Relay mandates. General mutation design, federation,
subscriptions, deployment, and exhaustive security or performance guidance are
outside the initial scope. No required framework, database, or Relay client
installation is introduced.

## Package architecture

Keep all package content under `plugins/graphql-design/`:

- Matching `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`, initial
  version `0.1.0`.
- `skills/design-graphql/SKILL.md` and `skills/audit-graphql/SKILL.md`.
- Focused shared references for principles, identification, connections,
  reporting, and sources.
- Original examples of design decisions and audit findings.
- Evaluation prompts, grader expectations, and small audit fixtures.
- README, design/plan documents, and verification records.

Skills route readers to relevant references rather than duplicating curriculum.
During implementation, register the package in `catalogs/plugins.json`, regenerate
both platform catalogs, and update the repository README. The spec-only commit
does not register an incomplete plugin. No sibling plugin is a prerequisite;
user configuration and platform-specific curriculum copies are out of scope.

## Design workflow

Activate for designing or revising GraphQL server schemas, refetching contracts,
and connection pagination. Avoid triggering for unrelated REST endpoints or
client-only presentation changes.

1. Inspect requirements, existing schema/resolvers, client query needs, and
   repository conventions. Separate observed facts from assumptions.
2. Establish object identity, refetchable entities, relationship traversal,
   filtering, ordering, and required pagination directions. Ask only for missing
   decisions that materially change the contract.
3. Propose relevant SDL and resolver behavior against the required baseline.
4. Explain identity construction, cursor interpretation, page boundaries,
   unavailable objects, and invalid pagination inputs. Identify application
   policies separately from specification requirements.
5. Return rationale, a meaningful alternative where useful, verification
   scenarios, and any migration sequence needed for existing clients.

Output depth follows the request. The skill provides guidance and illustrative
contracts; it does not itself authorize application edits or dependency installs,
and it does not impose an additional approval ceremony on every invocation.

## Audit workflow

Activate for reviewing GraphQL schemas and server behavior against the baseline.
Audits are read-only unless the user separately requests fixes.

1. Establish the inspected scope and available schema, resolver, test, and runtime
   evidence. Read applicable shared references.
2. Check schema contracts, then trace resolver behavior where implementation is
   available. Schema appearance alone cannot establish runtime compatibility.
3. Report confirmed violations in priority order with location, triggering
   query/input, consequence, supporting evidence, and a practical correction.
4. Separate formal violations from engineering recommendations and unverified
   behavior. State coverage limits, including unavailable execution evidence.
5. Report no findings when appropriate; do not invent violations for optional
   features, conventional encodings, or different implementation preferences.

Do not claim a query, test, or agent evaluation ran without execution evidence.
Do not convert unavailable evidence into either a confirmed defect or a pass.

## Examples and evaluations

Use small original domains and schema/resolver fixtures, not a reproduction of
Relay's Star Wars walkthrough. Include a compliant design and an existing API
with actionable audit findings. Keep model-visible prompts separate from hidden
grader expectations; score behavior and evidence rather than exact prose.

Evaluation coverage includes:

- Correct design/audit selection and unrelated prompts that should not activate.
- Required-baseline behavior even without an existing Relay client.
- Exact node lookup shape, identity collisions, repeated identity consistency,
  and unavailable refetch results.
- Valid non-base64 IDs and edge nodes that do not implement `Node`.
- Forward-only connections and sound designs requiring no change.
- Reversed backward ordering, incorrect page flags, and cursor boundaries.
- Empty pages, zero/negative sizes, and combined pagination arguments.
- Distinguishing mandated behavior from optional features and recommendations.
- Schema-only evidence with runtime behavior explicitly unverified.
- Read-only auditing and useful findings grounded in fixture locations.

These evaluations assess the plugin's reasoning and selection. They are distinct
from repository structural tests and from conformance tests a consuming project
would implement for its own GraphQL server.

## Validation and delivery

Use the existing isolated worktree on `feat/graphql-design`. Before committing:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
git diff --check
```

After inventory or manifest changes, first run
`.venv/bin/python -m scripts.catalogs`. Native Codex and Claude checks are
supplemental when available. Repository validation is structural and narrower
than exhaustive platform-schema validation. Record live agent activation and
semantic evaluation separately, marking anything unexecuted as unverified.

This stage delivers only the reviewed and committed written spec. After the user
approves this file, use the writing-plans skill to prepare the implementation
plan. Obtain plan review and execution-method selection before implementation.
