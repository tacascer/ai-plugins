# Sources and attribution

This plugin is informed by Vlad Khononov, *Learning Domain-Driven Design:
Aligning Software Architecture and Business Strategy* (O'Reilly, 2021). It is
not affiliated with or endorsed by the author or publisher. Its wording and
scenarios are original; it contains no copied book exercises or extended text.

The [publisher overview and contents](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/)
establish the book's structure. The accessible publisher chapter previews were
consulted for the following narrower points:

| Reference | Publisher preview and supported topic |
| --- | --- |
| [Strategic design](strategic-design.md) | [Chapter 1](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch01.html) introduces subdomains; [chapter 2](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch02.html) introduces domain knowledge and ubiquitous language; [chapter 3](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch03.html) shows the same term can differ between teams and introduces model boundaries; [chapter 4](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch04.html) names context integration patterns. |
| [Tactical design](tactical-design.md) | [Chapter 5](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch05.html) explicitly treats transaction script and active record as patterns for simpler logic; [chapter 6](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch06.html) introduces domain models and building blocks for complex logic; [chapters 7–8](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch08.html) locate event sourcing, layered architecture, ports and adapters, and CQRS as distinct topics. |
| Discovery | [Chapter 12](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/ch12.html) describes EventStorming as a group exploration of a business process using domain events and later concepts; the workshop is a way to learn from stakeholders. |
| Later references | The [contents](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/) lists chapter 9's translation, outbox, saga, and process manager topics; chapter 11's design evolution; and chapter 15's event-driven architecture and coupling topics. The contents establish coverage only, not detailed claims. |

Publisher previews stop after opening portions of chapters; the full book was
not available in this authoring session. Therefore detailed procedures in these
references are the plugin authors' engineering synthesis, informed by the
approved design and common DDD practice, unless the table identifies direct
preview support. In particular, the exact audit checklist, atomicity and
concurrency tests, message publication and retry advice, migration sequencing,
and report format are authored guidance rather than verified book instructions.
The examples are synthetic. No quotes or page-specific claims are made.

Source claims should stay within those access limits. If a future revision
needs a precise claim about an inaccessible chapter, obtain the relevant
licensed source material or another accessible primary source first.
