# Sources and attribution

This plugin is informed by Vlad Khononov, *Learning Domain-Driven Design:
Aligning Software Architecture and Business Strategy* (O'Reilly, 2021). It is
not affiliated with or endorsed by the author or publisher. Its wording and
scenarios are original; it contains no copied book exercises or extended text.

The [publisher overview and contents](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/)
establish the book's structure. Accessible publisher chapter previews and a
separate author talk were consulted for the following narrower points:

| Reference | Accessible primary source and supported topic |
| --- | --- |
| [Strategic design](strategic-design.md) | [Chapter 1](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch01.html) introduces subdomains; [chapter 2](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch02.html) introduces domain knowledge and ubiquitous language; [chapter 3](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch03.html) shows the same term can differ between teams and introduces model boundaries; [chapter 4](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch04.html) names context integration patterns. |
| [Tactical design](tactical-design.md) | [Chapter 5](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch05.html) explicitly treats transaction script and active record as patterns for simpler logic; [chapter 6](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch06.html) introduces domain models and building blocks for complex logic; [chapter 7](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch07.html) introduces event sourcing as a separate state-persistence pattern; [chapter 8](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch08.html) locates layered architecture, ports and adapters, and CQRS as distinct topics. |
| [Event-driven design](event-driven-design.md) | The [chapter 9 preview](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch09.html) introduces cross-context communication, model translation, and processes spanning components; its contents list outbox, saga, and process manager. The [chapter 15 preview](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch15.html) explicitly cautions that careless event-driven integration can increase coupling; its contents list event types and temporal, functional, and implementation coupling. The author's separate [Dark Side of Events talk](https://speakerdeck.com/vladikk/the-dark-side-of-events-eda) visibly distinguishes private/public events, notification/carried-state events, commands masquerading as events, and an outbox. The talk is support for these topics, not evidence that the book's full chapters were read. |
| [Evolution](evolution.md) | The [chapter 11 preview](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch11.html) says design decisions must respond to changes in business domain, organization, knowledge, and growth; its contents list shifts among subdomain types, implementation patterns, and boundaries. [Chapter 13's contents](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch13.html) list modernization topics. |
| Discovery | [Chapter 12](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch12.html) describes EventStorming as a group exploration of a business process using domain events and later concepts; the workshop is a way to learn from stakeholders. |
| Contextual relationships | The [contents](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/) lists microservices in chapter 14 and data mesh in chapter 16. Those chapters support contextual topic routing only; this plugin does not prescribe a deployment or analytics platform. |

Publisher previews stop after opening portions of chapters; the full book was
not available in this authoring session. Therefore detailed procedures in these
references are the plugin authors' engineering synthesis, informed by the
approved design and common DDD practice, unless the table identifies direct
preview or separately identified author-talk support. In particular, the exact
audit checklist, atomicity and concurrency tests, retry and idempotency design,
ordering and replay rules, migration sequencing, and report format are authored
engineering guidance rather than verified book instructions. The talk's outbox
slide supports the pattern's relevance, but does not verify every operational
step in this plugin's reliability advice.
The examples are synthetic. No quotes or page-specific claims are made.

Source claims should stay within those access limits. If a future revision
needs a precise claim about an inaccessible chapter, obtain the relevant
licensed source material or another accessible primary source first.
