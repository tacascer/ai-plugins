# Sources and provenance

Primary source: Jon Skeet,
[Storing UTC is not a silver bullet](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/),
March 27, 2019. This plugin is not affiliated with or endorsed by the author.
The source's main article is the reference; reader comments are not part of the
attributed curriculum. No article code is reproduced.

The [principles](principles.md) contain the concise source synthesis. This map
identifies its supporting sections:

| Rule topic | Article section |
| --- | --- |
| Intended invariant | Interlude: requirements |
| Derived values | Option 3: preserve local time, using UTC as derived data to be recomputed |
| Source information | Principle of preserving supplied data; Representation vs information |
| Conversion provenance | Option 2: convert to UTC immediately, but reconvert after rule changes |
| Offsets and identity | A possible option 4? |
| Gaps and overlaps | Ambiguous and skipped times |
| Series | Recurrent events |
| Geographic assignment | Time zone boundary changes and splits |
| Historical input | Past vs recent past |
| Recorded instants | Conclusion |

All entries refer to the article linked above. Its EU scenario is explicitly
hypothetical, not evidence of actual policy or current tzdb contents. The article
also excludes leap seconds and non-Gregorian calendars; tasks requiring those
need additional authoritative sources.

The design/audit split, reporting templates, evidence levels, cache-consumer
review procedure, original fixtures, and evaluation conventions are authored
implementation choices. They are not quoted requirements from Skeet. The plugin
selects no particular language, database, library, geographic lookup service, or
policy for resolving ambiguous input.
