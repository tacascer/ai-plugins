# Sources and provenance

This curriculum is an original, compact guide informed by Vladimir Khorikov's *Unit Testing: Principles, Practices, and Patterns* and his public articles. It is not a substitute for the book and is not endorsed by the author.

## Source map

| Curriculum topic | Book attribution | Public material checked | Evidence status |
| --- | --- | --- | --- |
| Unit-test definition; classical and London schools | Chapter 2 | [Pragmatic unit testing](https://enterprisecraftsmanship.com/posts/pragmatic-unit-testing/), [Unit Testing Dependencies](https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/), and [When to Mock](https://enterprisecraftsmanship.com/posts/when-to-mock/) | Public articles explain isolation between tests, independent dependency dimensions, and the schools' dependency treatment. The chapter contents confirm the chapter topics; the chapter text was not available in the excerpt. |
| Four quality pillars | Chapter 4 | [How to Assert Database State?](https://enterprisecraftsmanship.com/posts/how-to-assert-database-state/) and [Unit tests value proposition](https://enterprisecraftsmanship.com/posts/unit-test-value-proposition/) | The public articles explain the pillars and connect observable behavior to refactoring resistance. The excerpt contains only the chapter title and section headings for chapter 4. |
| Mocks, stubs, and observable behavior | Chapter 5 | [When to Mock](https://enterprisecraftsmanship.com/posts/when-to-mock/) and [How to Assert Database State?](https://enterprisecraftsmanship.com/posts/how-to-assert-database-state/) | The public articles explain double roles, inappropriate stub verification, system boundaries, and externally observable effects. The excerpt contains only chapter 5 headings. |
| Output-, state-, and communication-based styles | Chapter 6 | [Styles of unit testing](https://enterprisecraftsmanship.com/posts/styles-of-unit-testing/) | The article explains the three styles and their refactoring tradeoffs. The excerpt contains only chapter 6 headings. |
| Integration tests, managed dependencies, mocks, and databases | Chapters 8–10 | [Pragmatic integration testing](https://enterprisecraftsmanship.com/posts/pragmatic-integration-testing/) and [When to Mock](https://enterprisecraftsmanship.com/posts/when-to-mock/) | The articles explain direct use of owned dependencies and verification of external effects. The excerpt contains only chapter and section headings for chapters 8–10. |
| Interfaces and separating decisions from persistence | Related public guidance; no additional chapter-text claim | [Interfaces for repositories: do or don't?](https://enterprisecraftsmanship.com/posts/interfaces-for-repositories/) | The article argues against repository interfaces introduced solely to mock owned persistence and demonstrates isolated domain decisions with real-database integration coverage. |

The [publisher-provided excerpt and contents](https://enterprisecraftsmanship.com/files/Unit-Testing-Chapter-1-Excerpt.pdf) includes chapter 1 and the book's table of contents. It establishes the topic-to-chapter mapping above, but it does not provide the text of chapters 2–11. This plugin therefore does not claim to have verified those unavailable chapters line by line.

## What is source-backed

The following ideas are explained in the author's available material:

- tests should be isolated from one another; exercising several production classes does not by itself make a test an integration test;
- dependency dimensions such as in/out of process and shared/private answer different questions, and shared means that tests can affect one another through the dependency;
- output, state, and communication are distinct assertion styles;
- protection against regressions, resistance to refactoring, feedback speed, and maintainability are separate contributors to test value;
- a mock examines an outgoing side effect, while a stub provides input; verifying how a stub was queried couples a test to an implementation step;
- communications inside a chosen system boundary are usually implementation details, while effects visible to an external system can be observable behavior;
- an out-of-process dependency can be managed as part of the application or unmanaged and externally observed; that decision depends on ownership and visibility, not on technology alone.

## Plugin conventions

The five-dimension classification record, `supported`/`conditional`/`unresolved` confidence vocabulary, evidence fields, report layout, and conditional branches for missing architecture facts are original workflow conventions for this plugin. The guided decision sequence, prospective coverage guidance, language-neutral interface decision table, production-composition checks, and worked examples are also original plugin guidance, not claims of verified chapter content. They organize the source-backed concepts without being attributed to the book.

The explicit umbrella terminology and dummy/spy/fake descriptions organize conventional test-double vocabulary; they do not claim verification of additional book text.

Terms such as contract test, property-based test, component test, or consumer-driven contract may supplement the classification when a repository uses them. Treat them as repository or industry labels unless an available source supports a narrower attribution.

## Logging guidance

The [logging reference](logging.md) and [examples](../examples/logging.md) distinguish direct article advice from plugin applications:

- [Unit Testing Dependencies: The Complete Guide](https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/) explicitly recommends injecting loggers; cumbersome propagation can indicate too many layers or too much logging.
- [Code pollution](https://enterprisecraftsmanship.com/posts/code-pollution/) shows an injected substitute avoiding irrelevant logging I/O instead of a production test-mode switch.
- [When to Mock](https://enterprisecraftsmanship.com/posts/when-to-mock/) supplies the general observability and dependency-ownership rules.

Applying these rules to diagnostic wording, required support events, structured fields, and unknown consumers is original plugin guidance. The support/diagnostic vocabulary here is operationally defined in the reference; the searched articles do not establish the book’s full distinction. The available contents map logging to section 8.6, but that section’s text was not verified. These additions do not claim exhaustive coverage of its advice.
