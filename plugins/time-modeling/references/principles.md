# Time-modeling principles

This concise synthesis is based on Jon Skeet's
[Storing UTC is not a silver bullet](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/).

| Meaning or condition | Rule |
| --- | --- |
| Directly recorded instant | UTC is appropriate. |
| Commitment to local date/time | Preserve local input and zone; UTC is derived and may be cached. |
| Rule update | Recompute derived values from preserved source information. |
| Numeric offset | It does not identify a zone's changing rules. |
| Missing or repeated local time | Choose an explicit policy; rule updates can introduce these cases. |
| Recurrence | Use a coordinating zone and occurrence-specific conversions. |
| Location defines intent | Zone assignment may change; consider retaining location. |
| Recent-past local conversion | Stale rules can still make the result inaccurate. |

Preserve meaningful input, not necessarily its original formatting. Rule versions
can assist diagnostics and updates; reconstructing discarded local input from UTC
requires its original conversion context. Keeping source local input avoids that
reconstruction. Neither UTC nor local storage is universally correct. The
article's projected European policy changes are hypothetical.

## Applying the rules

The following procedure is plugin design, not an additional source prescription:

1. State the invariant in product terms before choosing fields. Use separate
   decisions for separate concepts in the same record.
2. Identify who supplies each value, who consumes it, and which dependency can
   invalidate a computation. Trace caches, jobs, indexes, and external consumers
   only where they exist in the examined system.
3. Make optional fields conditional on actual consumers. Do not require a cache,
   version field, location service, or migration just to match an example.
4. Verify the project's actual storage and conversion semantics. Names such as
   `timestamp with time zone` do not establish which input components survive a
   database round trip. Prefer repository evidence and authoritative platform
   documentation; disclose uncertainty if neither is available.
5. For a change procedure, specify its affected records and failure behavior.
   Keep the source value intact if conversion fails, and surface unresolved
   records instead of claiming a valid schedule. If materialized jobs depend on
   changed output, include their refresh or invalidation in the proposed design.
6. For existing data that lacks required inputs, describe what additional evidence
   could recover them. Do not invent a zone, local value, or conversion version.

Use the [examples](../examples/time-models.md) for concrete decisions and
[reporting conventions](reporting.md) for communicating their evidence.
