---
name: design-time-models
description: Use when designing or changing temporal storage, scheduling models, time conversions, or behavior after time-zone rule updates.
---

# Design Time Models

Choose representations from the product's intended invariant and the provenance
of its input. Consult the shared [principles](../../references/principles.md)
before recommending fields or conversion policies.

## Procedure

1. Inspect requirements, input boundaries, schemas, types, consumers, and local
   conventions. Determine what the user expects to remain fixed. If that fact is
   missing, explain conditional alternatives and ask the smallest necessary
   question; do not silently assign meaning to a field name.
2. Identify source and derived data using the principles. Include only fields
   required by the task, marking caches and diagnostic provenance optional when
   appropriate. Verify actual database/library behavior instead of inferring it
   from a type name.
3. Describe conversion inputs, update triggers, affected consumers, and failure
   handling. For applicable gaps, overlaps, recurrence, or geographic assignment
   changes, make the policy explicit. Preserve unresolved choices for the product
   owner instead of adopting an unexplained default.
4. Report a concrete model, expected behavior, proposed validation scenarios, and
   unresolved assumptions using [reporting](../../references/reporting.md).
   Distinguish checks proposed from checks executed.

Use [original examples](../../examples/time-models.md) when a contrasting case
helps. Follow repository conventions and other applicable implementation
processes; this workflow does not expand authorization to modify code or data.
It applies to temporal modeling, not incidental timestamps in unrelated prose.
