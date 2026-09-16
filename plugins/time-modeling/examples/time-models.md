# Original time-model examples

These are authored decision exercises using the [principles](../references/principles.md).
They are not copied article examples or evidence of executed tests. `Test/Venue`
and the transition rules below are synthetic fixtures, not real tzdb identities.

## Job-completion record

An export worker obtains `completed_at` directly from its clock. Consumers order
completed jobs and compute elapsed durations. A UTC instant satisfies those
requirements; adding `local_start`, `venue`, and `zone` creates no demonstrated
benefit. An audit should report no storage defect on this evidence.

Contrast a CSV column containing a device-entered local value: inspect its origin
and conversion before assuming the same model applies.

## Venue appointment under a rule update

The product promises local 09:00. Assume a unique mapping under each rule set:

| Field | Rule set A | Rule set B |
| --- | --- | --- |
| `local_start` | 2032-06-15T09:00 | 2032-06-15T09:00 |
| `zone` | Test/Venue | Test/Venue |
| Applicable offset | +02:00 | +01:00 |
| Optional `cached_utc` | 2032-06-15T07:00Z | 2032-06-15T08:00Z |

Keeping the cached 07:00Z job would trigger it at 08:00 local under B. A proposed
update must account for the scheduling consumer, not merely show a corrected
column. If `local_start` and `zone` are retained, the new computation can use B
directly. If they were discarded, do not promise an automatic migration without
first identifying recoverable source evidence.

Conversely, if a remote broadcast explicitly promises the instant 07:00Z,
changing it to 08:00Z would violate that different requirement.

## Zero or two conversion candidates

A fixture maps appointment A to no candidates and appointment B to two instants.
The UI can ask the organizer to choose another local value for A and a specific
occurrence for B. That is one possible product policy, not a universal rule.
A background recomputation cannot assume an organizer is present: it might flag
the unresolved record for review and withhold a replacement reminder. Document
which behavior the actual product chooses and test that path.

## Weekly occurrence

A weekly series promises Monday 09:00 in its coordinating zone. In a synthetic
week, the first occurrence uses +02:00 and the next uses +01:00. Their UTC hours
are 07:00 and 08:00 respectively. Advancing 168 elapsed hours yields the wrong
second local hour. Resolve the second occurrence from the recurrence definition;
render attendee views from that occurrence's instant using each attendee's zone.

## Insufficient evidence

Given only `starts_at = 2032-06-15T07:00Z`, neither the field name nor the value
establishes a flaw. State the missing fact: does the product promise that instant
or a particular local appointment? Inspect input and consumers when available.
If no further evidence exists, offer conditional models and leave the finding
unconfirmed rather than invent a requirement or a database type.
