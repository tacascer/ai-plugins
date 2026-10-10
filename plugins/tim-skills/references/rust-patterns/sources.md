# Source evidence and decision limits

For *Rust for Rustaceans*, see the separate [edition, passage, and primary-source map](rustaceans-sources.md) and [correction ledger](rustaceans-errata.md). The material below concerns *Zero to Production in Rust*.

Accessed 2026-09-28. This is a map of evidence for the decision references, not
a reproduction of the book. The supplied PDF is a historical snapshot: its
framework comparison describes March 2022, and its database comparison
describes August 2020. Neither date establishes the current best library or
current API. Check the project's pinned versions and enabled features before
using version-specific advice. The linked `latest` documentation is a snapshot
at access time, not a promise about later releases.

## Verified book principles

Source for every row: *Zero to Production in Rust*, [supplied
PDF](https://github.com/rustaccato/e-books/blob/main/Zero%20to%20Production%20in%20Rust.pdf);
[author's site](https://www.zero2prod.com/). Attribution category:
**book-derived principle**. The sections below were read in the supplied PDF
extraction; the contents page alone was not used as proof of the claims.

| Decision topic | Passage inspected | Supported principle and limit |
| --- | --- | --- |
| Types and boundaries | §§6.3–6.5, 6.14, 9.8 | A plain `String` does not express a nonempty-name invariant; a validated type and fallible boundary conversion can make the guarantee local. Revalidate values arriving from storage or other untrusted construction paths. The book's particular subscriber constraints are application examples, not generic document-name rules. |
| Errors | §§8.1–8.5 | Errors serve caller decisions, operator diagnosis, and edge responses differently. Preserve causal context for diagnosis and keep HTTP status mapping at the handler boundary. The text discusses typed error enums and opaque application errors as different tools; it does not mandate one crate or error type everywhere. |
| Async and state | §§3.3.2.4, 3.9, 4.5.4, 10.2.4 | Blocking password work can stall async execution; shared application state has worker-lifetime implications; future-aware span instrumentation follows polls. These passages do not establish a universal synchronization primitive or cancellation guarantee. |
| Configuration and serialization | §§3.8.5.2, 5.3.6, 6.14 | Layered sources can deserialize into typed settings; form/JSON parsing and domain validation are separate decisions. The book's settings shape and source precedence are examples, not required configuration policy. |
| Persistence | §§3.8.2, 7.6.2, 7.8.1–7.8.3 | Choose a database interface by query form, checking model, and async needs; group related writes under a database transaction when the contract is all-or-nothing; allow old and new app versions to coexist during rolling schema changes. The historical SQLx choice is not a universal recommendation. |
| HTTP | §§3.2, 7.2.2–7.2.3 | Framework choice was contextual; a reused HTTP client can retain connection pooling; an HTTP mock server can control an external dependency at the protocol boundary. The book's dated framework preference and download counts are not current evidence. |
| Observability | §§4.4–4.5.4, 4.5.12–4.5.14 | Correlate structured request and external-operation context; instrument futures correctly; review automatically captured arguments for secrets. The particular logging stack is optional. |
| Authentication | §§10.2.3–10.2.5, 10.7 | Password hashing is deliberately expensive and should not occupy async executor workers; session tokens are sensitive credentials. Algorithm parameters and cookie policy require current primary guidance below. |
| Testing | §§3.4.1, 3.8.3, 6.13.2, 7.2.3 | Exercise HTTP contracts through a running application, isolate database effects, and control external HTTP; property testing can explore validated inputs. The historical quickcheck selection is a local choice, not a ranking. |

## Current primary sources and bounded alternatives

Each entry gives a topic, URL, access date, version context, supported advice,
and attribution category. The decision criteria following each group are **our
engineering synthesis**, rather than quotations or claims of general
superiority.

| Topic and primary source | Access and version context | Supported advice | Category |
| --- | --- | --- | --- |
| Web state: [Actix Web application guide](https://actix.rs/docs/application/) | 2026-09-28; online guide, inspect pinned `actix-web` version | `App` registers routes and middleware; `web::Data<T>` shares state, and its creation relative to the server factory affects worker-local versus shared state. | upstream documentation |
| Web state: [Axum `State`](https://docs.rs/axum/latest/axum/extract/struct.State.html) | 2026-09-28; docs.rs `axum` 0.8.9 | `Router::with_state` and `State<S>` supply handler state; extraction and router composition follow Axum's type model. | upstream documentation |
| Query checking: [SQLx `query!`](https://docs.rs/sqlx/latest/sqlx/macro.query.html) | 2026-09-28; docs.rs `latest`, inspect pinned SQLx version | Literal SQL macros check against a build-time schema connection or prepared offline metadata; dynamic SQL cannot use this macro's inspection path. | upstream documentation |
| Query interface: [Diesel getting started](https://diesel.rs/guides/getting-started) and [Diesel selects guide](https://diesel.rs/guides/all-about-selects/) | 2026-09-28; current online guide, inspect pinned Diesel version and MSRV | Diesel shows a schema-backed query DSL with compile-time result mapping checks and model derives. | upstream documentation |
| Configuration: [`config` crate](https://docs.rs/config/latest/config/) | 2026-09-28; docs.rs `config` 0.15.25 | Merge file, environment, and override sources, then deserialize a typed settings structure. | upstream documentation |
| Configuration: [Figment providers](https://docs.rs/figment/latest/figment/providers/index.html) | 2026-09-28; docs.rs `figment` 0.10.19 | Providers supply file, environment, serialized, and format-specific input to extraction. | upstream documentation |
| Property testing: [quickcheck `Arbitrary`](https://docs.rs/quickcheck/latest/quickcheck/trait.Arbitrary.html) | 2026-09-28; docs.rs `quickcheck` 1.1.0 | Type-oriented arbitrary generation has an optional shrink implementation. | upstream documentation |
| Property testing: [proptest `Strategy`](https://docs.rs/proptest/latest/proptest/strategy/trait.Strategy.html) | 2026-09-28; docs.rs `proptest` 1.11.0 | Composable strategies transform/generated constrained values and shrink through source strategies. | upstream documentation |
| External HTTP tests: [Wiremock `MockServer`](https://docs.rs/wiremock/latest/wiremock/struct.MockServer.html) | 2026-09-28; docs.rs `wiremock` 0.6.5 | A local server can emulate an external HTTP dependency, with an instance per test for isolation. | upstream documentation |
| Client reuse: [reqwest `Client`](https://docs.rs/reqwest/latest/reqwest/struct.Client.html) | 2026-09-28; docs.rs `reqwest` 0.13.5 | A client contains a reusable connection pool and can be cloned for shared use. | upstream documentation |
| Blocking work: [Tokio `spawn_blocking`](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html) | 2026-09-28; docs.rs `tokio` 1.53.1 | Move bounded blocking work off executor workers; CPU-heavy concurrent calls need an explicit concurrency limit, and started blocking tasks cannot normally be aborted. | upstream documentation |
| Timeout: [Tokio `timeout`](https://docs.rs/tokio/latest/tokio/time/fn.timeout.html) | 2026-09-28; docs.rs `tokio` 1.53.1 | Timeout drops the local future on expiry; this does not establish rollback of a remote side effect. | upstream documentation plus stated inference |
| Transaction: [SQLx `Transaction`](https://docs.rs/sqlx/latest/sqlx/struct.Transaction.html) | 2026-09-28; docs.rs `latest`, inspect pinned SQLx version | An in-progress SQLx transaction rolls back when dropped; the application must put related writes within that scope and commit explicitly. | upstream documentation |
| Span fields: [tracing `instrument`](https://docs.rs/tracing/latest/tracing/attr.instrument.html) | 2026-09-28; docs.rs `latest`, inspect pinned tracing version | `skip(field)` or `skip_all` excludes automatic argument capture from spans. | upstream documentation |
| Passwords: [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | 2026-09-28; living guidance, no crate version | Use a suitable adaptive password hash with unique salt; tune work factors against current guidance and the service's resources. | current security guidance |
| Sessions: [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | 2026-09-28; living guidance, no crate version | Protect session IDs as credentials and use HTTPS with deliberate cookie attributes such as `Secure`, `HttpOnly`, and `SameSite` for browser sessions. | current security guidance |

**Decision synthesis.** Keep an existing Actix Web service when its state and
handler model meet the requirement; Axum offers a typed `Router`/`State` path
when designing a new stack or when that integration is specifically valuable.
For SQL-heavy work where the team wants to write literal SQL, SQLx macros offer
schema checking with build metadata obligations. For a team that prefers
composable typed query construction, Diesel's DSL is a relevant option; check
its version, MSRV, database backend, and async integration before choosing.
Neither choice alone proves runtime schema compatibility. `config` and Figment
are both source-composition tools. `config` documents live file watching; that
is a concrete reason to evaluate it when reload is required. Figment's
`Provider` interface is relevant when the project already composes custom
providers or serialized defaults. Separately validate domain limits either
way.
For property tests, quickcheck is compact when type-wide `Arbitrary` generation
fits; proptest strategies are useful when a particular property needs explicit
constrained generation and shrink composition. Wiremock is relevant when a test
needs to observe a real HTTP request while controlling the remote responder;
it is not a reason to mock owned database or internal application behavior.

**Access limits.** The supplied PDF extraction and linked web documentation
were inspected, but no library source was built and no API snippet was compiled
against this plugin. Online `latest` aliases can move. The sources establish
documented capabilities and bounded decisions, not benchmark rankings,
security certification, or compatibility with an unknown project's pins.
