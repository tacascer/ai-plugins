# Domain-Driven Design plugin design

Date: 2026-09-27

Status: written spec and implementation plan approved by the user; subagent-driven
implementation selected. Tasks 1 and 2 are complete; Task 3 verification is
recorded in [the initial verification record](../../verification/2026-09-27-initial.md).

## Purpose and agreed scope

Create a language-agnostic agent plugin that applies the knowledge in Vlad
Khononov's *Learning Domain-Driven Design* to real projects. Give equal weight
to designing new systems or features and assessing and evolving existing systems.
The user explicitly requested advice on event-driven design as part of this scope.

Success means helping an agent make concrete, proportionate decisions grounded
in business scenarios and project evidence. The plugin must support simple
solutions, richer domain models when justified, and incremental modernization.
It must identify missing domain knowledge rather than invent business policies.

The approved structure is two decision-oriented workflows sharing one knowledge
base. Structured teaching and chapter-by-chapter exercises are outside scope.

## Package and components

The package is `plugins/domain-driven-design/`, initially version `0.1.0`.
It contains matching Codex and Claude manifests and shared content:

- `skills/design-domain-model/SKILL.md`: design workflow.
- `skills/audit-domain-model/SKILL.md`: evidence-based review workflow.
- `references/principles.md`: common decision procedure and reference routing.
- `references/strategic-design.md`: business discovery and model boundaries.
- `references/tactical-design.md`: business rules and implementation choices.
- `references/event-driven-design.md`: event semantics, integration, and coupling.
- `references/evolution.md`: reassessment and incremental modernization.
- `references/reporting.md`: output conventions and evidence handling.
- `references/sources.md`: attribution and topic-to-source mapping.
- `examples/`: original scenarios illustrating contrasting decisions.
- `evals/`: model-visible tasks and separate grader expectations.
- `README.md` and `docs/`: usage, design, and verification records.

The skill entry points read the common principles and only the topic references
needed for the task. References depend on no particular framework, database,
message broker, or other installed plugin. Examples use prose, diagrams, or
pseudocode when those make the decision clearer.

Register the package in `catalogs/plugins.json`, regenerate both platform
catalogs, and add it to the repository README during implementation. Keep all
plugin content inside its own directory; do not duplicate guidance by platform.
User configuration, installation, and NixOS changes are outside this delivery.

## Shared knowledge and decision criteria

### Business discovery and strategic design

Start with business goals, representative scenarios, terminology, domain experts,
and existing organizational constraints. Distinguish core, supporting, and generic
subdomains using evidence of business role and complexity. Treat classification
as revisable as the business changes.

Develop a ubiquitous language scoped to each bounded context. Distinguish
problem-space subdomains from solution-space model boundaries. Explain ownership
and context relationships, including translation and upstream/downstream
responsibilities. Do not infer a service deployment boundary from every context
or aggregate. Include EventStorming as a discovery technique when appropriate;
an agent's proposed model cannot substitute for stakeholder knowledge.

### Tactical design

Choose transaction script, active record, domain model, or event-sourced domain
model based on business complexity and requirements. Explain trade-offs rather
than prescribe a uniform architecture.

Identify entities, value objects, aggregates, domain events, and business
invariants where useful. Tie aggregate boundaries to consistency requirements
and business operations. Evaluate layered architecture, ports and adapters, and
CQRS separately from the choice of business-logic implementation pattern.
Recommend checks that demonstrate business rules and boundary behavior.

### Event-driven design

Give event-driven design a dedicated reference used by both workflows:

- Distinguish commands, domain events, and externally consumed integration
  events. Identify intent, business fact, producer, consumers, and ownership.
- Choose event notification or consumer-relevant state transfer based on consumer
  needs, ownership, compatibility, and coupling. Avoid exposing internal models
  merely because serialization is convenient.
- Examine temporal, functional, and implementation coupling. Trace complete
  business flows to find decision logic dispersed across consumers or event
  chains whose business purpose is unclear.
- Assess choreography, sagas, and process managers against coordination needs.
  Make responsibility for workflow progress and compensation explicit.
- Specify publication consistency, retry and duplicate handling, relevant
  ordering scope, and failure recovery. Consider an outbox when a state change
  and message publication must be coordinated. Do not imply transport guarantees
  alone establish exactly-once business effects.
- Assess event sourcing and CQRS independently. Explain their costs and the
  requirements that justify them; using messages does not mandate either.

Reliability mechanisms and reporting conventions must be attributed accurately:
separate verified book guidance from supplementary engineering synthesis.
Domain and integration events have business contracts; telemetry events serve
observability consumers and do not automatically satisfy those contracts.

### Evolution

Reassess boundaries and implementation choices as domain knowledge, business
importance, or team relationships change. For existing systems, describe the
smallest useful improvement, dependencies, compatibility constraints, and how
to verify preserved business behavior. Event-contract changes must consider
old and new producers and consumers during migration. Propose broader redesign
only when evidence supports its cost.

The book's relationships to microservices and data mesh are contextual guidance
when relevant to ownership and boundaries, not separate deployment or analytics
platform workflows in this release.

## Workflow behavior

### Design domain model

Activation: requests to design or revise business models, bounded contexts,
aggregates, domain rules, or business-event interactions. Generic use of the word
"domain" or unrelated infrastructure tasks should not trigger the workflow.

1. Inspect the request, existing code and documentation, representative scenarios,
   constraints, and relevant message or persistence contracts.
2. Separate observed facts, supplied business rules, assumptions, and unresolved
   questions. Ask domain experts for missing information that changes decisions.
3. Propose terminology, context boundaries, responsibilities, and business
   invariants at the scope needed for the task.
4. Compare suitable implementation and integration choices and explain the
   selected option against the actual requirements.
5. For event-driven flows, describe message meaning, producer and consumer
   responsibilities, consistency, and failure handling.
6. Return concrete decisions, alternatives and trade-offs, open questions,
   proposed verification, and an implementation or migration sequence.

Scale output to the request. A single aggregate decision does not require a
whole-system report. This skill produces design guidance and follows the user's
authorized scope and development process; it adds no blanket permission to edit.

### Audit domain model

Activation: requests to assess existing domain models, boundaries, invariants,
or business-event integrations and to identify modernization opportunities.

1. Establish the requested review scope and inspect available requirements.
2. Trace representative business flows through code, schemas, transaction
   boundaries, and message contracts using the relevant shared references.
3. Identify demonstrated problems and distinguish them from hypotheses or
   questions needing business expertise.
4. For each finding, provide location or other concrete evidence, business or
   operational consequence, reasoning, a proportionate correction, and a way to
   verify it. Prioritize by impact rather than distance from pattern vocabulary.
5. Report reviewed scope, limitations, and checks actually performed. Recommend
   no change when the current design adequately serves the requirements.

Audits remain read-only unless changes are also requested. Missing evidence is
reported as a limitation, not converted into a defect. An appropriate simple
implementation must not receive findings just for lacking DDD abstractions.

## Source grounding

Primary source: Vlad Khononov, *Learning Domain-Driven Design*, O'Reilly, 2021.
The [publisher's contents and overview](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/)
were consulted to establish the topic map for this spec. They are not evidence
that every chapter's full text has been reviewed.

Map authored guidance to relevant sections: strategic design (chapters 1-4),
tactical implementation and architecture (5-8), communication patterns (9),
heuristics and evolution (10-11), discovery and real-world adoption (12-13), and
related architectures (14-16), especially event-driven architecture (15).

During content authoring, verify detailed attributions against accessible
primary material. Record access limitations and distinguish independently
authored synthesis from confirmed book claims. Request relevant source material
if an important attribution cannot otherwise be verified. Do not invent quotes
or page numbers. Use original prose and examples, and state that the plugin is
not affiliated with or endorsed by the author or publisher.

## Evaluation and acceptance

Use scenario evaluations for both explicit invocation and implicit selection.
Keep grader expectations separate from model-visible prompts. Include:

1. Simple business logic where transaction script is sufficient.
2. Ambiguous terminology requiring different context-specific models.
3. Confusion between subdomains, bounded contexts, and deployment boundaries.
4. A business invariant violated by an aggregate or transaction boundary.
5. Context integration requiring explicit ownership or translation.
6. Event contracts exposing implementation details and coupling consumers.
7. Event notification versus consumer-relevant state transfer trade-offs.
8. Business decisions dispersed across a chain of event consumers.
9. Publication failure, duplicate delivery, and ordering requirements.
10. Coordination requiring explicit progress or compensation responsibilities.
11. An unjustified assumption that messaging requires CQRS or event sourcing.
12. Incremental modernization with compatible event-contract evolution.
13. Missing domain knowledge where the correct output includes questions.
14. A sound existing design where no change is the appropriate recommendation.
15. An unrelated task that should not activate either skill.

Together the scenarios must exercise both new-design and existing-system tasks,
require evidence for audit findings, and reward proportionate choices. Include
at least one fixture-based audit so evidence tracing is observable. Evaluation
results must state which model runs occurred and preserve their evidence under
the repository's evaluation conventions. Authored cases alone do not demonstrate
reliable selection or behavior.

Before committing, run the repository unittest suite, catalog drift check, and
Python validator. Regenerate catalogs after implementation changes the inventory
or manifests. Use native platform validators as supplemental checks when
available; repository validation is not exhaustive platform-schema validation.

Delivery acceptance requires a complete package, accurate source boundaries,
the two workflows and shared references, original examples, evaluation cases,
updated inventory and catalogs, and a verification record separating structural
checks, supplemental checks, and executed or pending model evaluations.

## Review and next stage

The user approved this spec and the implementation plan and selected
subagent-driven execution. The verification record distinguishes completed
structural checks from runtime evaluations still pending authentication and a
safe isolated loader.
