# Event-driven business design

Use this reference when a business decision crosses a context or message
boundary. Begin with a complete business flow: the triggering request, each
decision and state change, the customer-visible promise, and the failure path.
Name who owns the fact and who must act on it. An asynchronous hop changes
timing; it does not transfer ownership of a business rule by itself. If one
transaction or a direct request answers the need more clearly, use it.

## Meaning and contract

- A **command** asks a named owner to do something and may be refused. Its
  imperative intent remains a command even if a broker carries it or its name
  ends in `Event`.
- A **domain event** records a meaningful fact after a transition inside its
  model. It may contain private details needed for local behavior or history.
- An **integration event** is a public contract for consumers outside that
  owner. It should communicate a stable business fact with a defined meaning,
  identity, version policy, and producer; it need not serialize every private
  domain event. State what a consumer may rely on and who owns changes.
- A **telemetry event** reports operation to observability consumers. Local
  logging can be best effort. It is not a fulfillment or settlement contract
  unless the required durable delivery and business semantics are explicitly
  designed.

Choose message content from the consumer's actual decision. A small event
notification can say that something changed and let a consumer fetch current
state; that adds a live lookup dependency and needs a policy for unavailable or
newer state. Event-carried state can let an eventually consistent consumer
update its view without that lookup, but only carry consumer-relevant public
facts. Neither choice warrants exposing table columns, ORM objects, private
costs, or all internal events. For a decision requiring the latest authoritative
fact, consider a synchronous query or a stronger shared consistency boundary.

## Coupling and coordination

Trace where business decisions actually occur, not only the arrows between
services. **Temporal coupling** appears when progress requires another party
to be available within a deadline or a chain cannot tolerate delay.
**Functional coupling** appears when one promise depends on rules distributed
among consumers or requires them to perform a precise sequence.
**Implementation coupling** appears when consumers must know producer table
fields, private event classes, or internal state codes. Record concrete
evidence and the consequence of each; asynchronous transport alone removes
none of these obligations.

Choreography suits a short flow whose participants can react to owned facts
without one party secretly coordinating the whole promise. If progress,
timeouts, and partial failure span several owners, name a workflow owner.
A saga coordinates business steps with explicit intermediate states and
possible compensating actions. A process manager can hold progress and route
commands based on outcomes and timers. Compare a small orchestrated process,
a local transaction, and a changed business rule before adding a distributed
workflow. Compensation is another business action, not a guaranteed rollback:
an external charge or non-refundable reservation may need reconciliation,
customer communication, or manual remedy.

## Delivery and recovery (engineering synthesis)

These reliability checks are independently authored engineering guidance;
the [source notes](sources.md) distinguish the accessible book and talk evidence.
When a committed state change requires a message, trace both sides of the
boundary. A database commit followed by broker publish can leave committed
state without a message if publication fails. A transactional outbox can record
the message with the state change, then relay and retry it; the relay needs
recovery, monitoring, and a retention policy. Depending on requirements,
another durable coordination method may fit. A broker does not make an
unrelated database commit atomic.

State the consumer's duplicate policy and the exact ordering scope that the
business needs, often per aggregate or order rather than globally. Retries or
relay crashes can deliver a message twice. Make effects idempotent through
stable message or business keys and an atomic check with the effect, or explain
why a duplicate is harmless. If order matters, carry a scoped version and
reject or defer stale messages; plan for missing predecessors and replay.
Transport claims do not prove exactly-once business effects. Specify failure
injection, replay, old/new contract tests, and operational reconciliation for
the promised outcome.

Assess CQRS and event sourcing separately. CQRS may justify distinct read and
write models when their requirements diverge; they can share a database.
Separately maintained read projections add synchronization work and can
introduce lag.
Event sourcing persists history as the state source when historical behavior
or reconstruction warrants replay, event evolution, and retention costs.
Messages alone require neither. Microservice deployment and data mesh are
contextual to ownership and consumers, not automatic consequences of events.
