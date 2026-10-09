# Strategic design and discovery

## Business capability and language

Identify the business goal and representative successful and failed scenarios.
Ask who decides each rule and which facts they need. Classify subdomains as
core, supporting, or generic only when their role in differentiation and their
complexity are evidenced. The classification can change with strategy; avoid
claiming one from package names alone.

Build a vocabulary for each bounded context with domain experts. Record the
meaning of important terms, allowed transitions, and examples. When two teams
use the same word for different concepts, keep their models and terms locally
coherent; define translation at the boundary. A subdomain describes part of the
business problem. A bounded context defines where one model is consistent. One
context can cover more than one subdomain, and a subdomain can involve multiple
models. Draw the boundary around model meaning and ownership, not around every
class or deployment unit.

## Ownership and integration

For a relationship between contexts, name the owner of each fact, the upstream
provider, the downstream user, and who can change the contract. Specify what
the downstream model needs and where translation occurs. Shared persistence
entities can couple meanings and release schedules; choose that deliberately
only when shared ownership and semantics justify it. A local translation layer
can protect a context from an upstream model with different language. Shared
kernel and cooperative changes need explicit governance, not mere shared code.
Do not derive a service per context or per aggregate; deployment follows team,
operational, and scaling evidence.

## EventStorming as discovery

When the process is uncertain or teams disagree, propose a bounded workshop
with the relevant business experts and implementers. Explore actual business
events in time order, commands or decisions that precede them, policies,
exceptions, external actors, and contested terms. Mark pain points and candidate
boundaries. The resulting map is a hypothesis until stakeholders validate it;
an agent can prepare questions and draft examples but cannot confer expert
agreement. Record decisions and unresolved policy questions after the workshop.
