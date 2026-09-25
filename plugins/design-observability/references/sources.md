# Sources and attribution

The original logging foundations are informed by Nikita Sobolev,
[Do not log](https://sobolevn.me/2020/03/do-not-log), published March 11, 2020.
They cover preventing invalid states, representing expected failures explicitly,
separating important failure reporting from business-outcome monitoring,
recognizing logging as a fallible side effect and maintained subsystem, and
retaining useful, structured, safe diagnostics. The synthesis is original and
does not reproduce the article's prose, code, or screenshots.

The structured-event and listener architecture is this plugin's design choice,
not a claim from the source article. Event contracts, emission timing, metric
cardinality, listener lifecycle, delivery rules, the availability exception,
verification boundaries, procedures, reports, evaluations, and examples are
original plugin guidance. No vendor, library, or functional rewrite is required.

This plugin is not affiliated with or endorsed by Nikita Sobolev.
