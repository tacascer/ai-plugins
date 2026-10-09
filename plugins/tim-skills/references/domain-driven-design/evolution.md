# Evolving domain design

Revisit a design when business strategy, domain knowledge, team ownership,
transaction needs, or consumers change. A formerly generic capability may
become differentiating; a former core capability may become routine. Recheck
the actual business role and complexity before changing investment, language,
bounded contexts, or implementation pattern. A prior classification is a
decision made under older evidence, not a permanent label.

For an existing system, identify the business behavior to preserve and the
smallest useful improvement. Locate the current decision owner, transaction
boundary, data and message contracts, and callers before moving a rule. A
transaction script can grow into a domain model as invariants become complex;
an ownership boundary can change without first creating a new service. Compare
the benefit with migration, coordination, and operational cost. Broader
restructuring needs evidence of a problem it will solve.

Make the transition explicit:

1. State the changed requirement and the existing behavior to protect. Mark
   missing policy for domain-expert confirmation.
2. Choose a narrow boundary or rule change. Identify data owners, consumers,
   dependencies, and what can run concurrently during transition.
3. For an external event contract, test old and new reader behavior rather than
   assuming a new field or version is compatible. Add or translate a contract,
   deploy consumers and producers in a safe order, and allow old and new
   participants to coexist until evidence supports retirement. Avoid exposing
   internal persistence fields as the migration interface.
4. Verify business scenarios, concurrency and failure paths, contract parsing,
   replay or reconciliation where relevant, and observed adoption. State which
   checks are proposed versus executed. Retire obsolete paths only after their
   consumers and recovery obligations are accounted for.

If a team relationship changes, revisit upstream and downstream control,
translation, and contract governance. If an aggregate boundary changes, revisit
which invariant must remain immediate and how old records migrate. Treat
microservice or analytics-platform changes as separate decisions justified by
operational and consumer evidence. The sequence above is authored engineering
synthesis; the [source notes](sources.md) identify what the accessible chapter
preview confirms.
