---
name: audit-time-models
description: Use when reviewing or investigating existing date/time storage, scheduling, time-zone conversions, or failures caused by changing time-zone rules.
---

# Audit Time Models

Find mismatches between intended time semantics and demonstrated behavior.
Read the shared [principles](../../references/principles.md); a representation's
name alone is not evidence of a defect.

## Procedure

1. Trace input through persistence, conversion, update paths, and relevant
   consumers. Inspect requirements and repository conventions. Establish which
   values are original input, directly recorded instants, or computations.
2. Compare the observed flow with the principles. Inspect applicable policies and
   affected jobs or caches. Verify actual library and database semantics; report
   missing implementation evidence explicitly. When requirements are unknown,
   give conditional conclusions instead of inventing a product promise.
3. For each material mismatch, state a concrete failure condition, consequence,
   supporting file/line references, and a proportionate correction. With only a
   supplied scenario, cite it without fabricating files or observed incidents.
4. Separate confirmed findings, conditional concerns, and missing evidence using
   [reporting](../../references/reporting.md). If no material issue is found,
   say so and describe the inspected scope. Claim executed verification only
   when command or runtime evidence supports it.

Consult the [examples](../../examples/time-models.md) when distinguishing similar
representations with different intended behavior. Keep the review read-only
unless the user also authorizes changes. Do not launch this workflow merely
because an unrelated task includes a timestamp.
