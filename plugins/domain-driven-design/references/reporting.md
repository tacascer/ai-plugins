# Reporting decisions and findings

Keep the response proportional to the request. A local rule decision can be a
short recommendation; a cross-context review may need a flow map and prioritized
findings. Separate the following where they matter:

- **Evidence:** supplied scenario facts, inspected code or contract locations,
  and checks actually run. Cite a path and line when available. Do not invent a
  source location for a prose-only scenario.
- **Assumptions and limits:** what was not available or was inferred. Mark a
  suspected problem as a hypothesis until evidence establishes it.
- **Decision or finding:** the affected business rule, owner or boundary; why
  the current or proposed model matters; and the consequence or benefit.
- **Trade-offs:** an alternative that fits the same evidence and why the chosen
  option is proportionate.
- **Open questions:** ask the domain expert for a policy answer when it changes
  state, invariants, or integration responsibilities. Do not fill it in silently.
- **Correction and verification:** the smallest useful change or design step,
  dependencies and compatibility concerns, and a check that would demonstrate
  the business behavior. Label checks as proposed or executed.

For an audit, state the reviewed scope and prioritize demonstrated consequences.
Include a no-change conclusion when the implementation adequately serves the
known rules. For design, give actionable responsibilities and a sequence at the
scope requested. An audit is read-only unless the user also requests edits.
