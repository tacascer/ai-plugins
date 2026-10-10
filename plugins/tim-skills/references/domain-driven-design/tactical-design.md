# Tactical design and implementation choices

## Rules and consistency

Write invariants in business language, including the operation that must keep
each true and the consequence of violation. Trace when a decision reads state,
when it commits, and what concurrent or delayed work can change before then.
Put a rule that must hold immediately inside a reliable consistency mechanism,
such as one transaction with an atomic check. An aggregate is useful when it
encapsulates related state and operations under such a boundary; it is not a
mandatory wrapper for every record. Cross-aggregate or cross-context rules may
need a process with explicit intermediate states and compensation, or a changed
business policy. Verify the actual consistency requirement before choosing.

Use an entity when stable identity and lifecycle matter. Use a value object when
equality by attributes and immutable validated value are the useful semantics.
Domain events describe meaningful facts after a business transition. These
building blocks should clarify the rule; avoid adding them to simple forms for
their own sake.

## Select the logic pattern

| Pattern | Useful when | Watch for |
| --- | --- | --- |
| Transaction script | Operations have a few direct rules and data changes | Duplicate rules or non-atomic read/check/write paths as complexity grows |
| Active record | Simple record-centered behavior and persistence can remain coupled | Business decisions spread across persistence callbacks |
| Domain model | Rich invariants, transitions, or collaborating concepts need explicit behavior | Abstractions whose boundaries lack business evidence |
| Event-sourced domain model | Reconstructing state from business history is required and its operational cost is justified | Event versioning, replay, retention, and migration costs |

Choose business-logic implementation separately from application architecture.
Layered architecture or ports and adapters can organize dependencies; CQRS can
separate read and write models when their needs differ. Neither messaging nor a
domain model alone requires CQRS, event sourcing, or a distributed deployment.
Test business rules, boundary behavior, and failure cases at the level that
demonstrates the choice. A simple implementation that serves the known rules
needs no corrective DDD finding.
