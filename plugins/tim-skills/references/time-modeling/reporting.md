# Reporting time-model decisions

These conventions are plugin workflow choices. Scale the response to the user's
question; omit irrelevant sections rather than fabricate completeness.

## Design result

State the intended invariant first, then describe:

- Source fields, their origin, and which fields are optional derived values.
- Conversion inputs, update triggers, affected consumers, and failure handling.
- Applicable unresolved policies, with conditional alternatives when necessary.
- Concrete validation scenarios and expected outcomes.
- Assumptions, missing requirements, and which checks were actually executed.

A field table can distinguish provenance from representation. A value's name or
serialization alone is not evidence of its intended meaning.

## Audit result

For each material finding, give its consequence, concrete trigger, file/line
reference when source is available, and proportionate correction. Distinguish:

| Evidence level | How to report |
| --- | --- |
| Confirmed | The supplied requirement and inspected behavior conflict; cite both. |
| Conditional | Explain the requirement or runtime condition under which the risk occurs. |
| Unknown | Name the missing input, requirement, implementation, or execution evidence. |

A confirmed flaw in a code path does not mean the incident actually occurred.
When only a prose scenario is supplied, cite that scenario without inventing file
locations. If no material issue is found, report that conclusion and the examined
scope. Favor consequences over stylistic preferences.

## Scope and execution

A design request may yield a proposal; it does not independently authorize a
migration or a production data change. A review remains read-only unless the user
also requests fixes. Preserve applicable repository processes and existing user
authorization.

Label proposed checks as proposed. Record commands and outcomes when tests run,
and explain unavailable validation. Do not infer a successful runtime conversion
from a manifest check, a schema name, or a familiar library API.
