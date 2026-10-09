# Macro decisions

**Fit.** Prefer functions, generics, or ordinary implementations when they express the required reuse. Reach for a macro when syntax transformation or repeated declarations are the actual problem.

**Choice.** `macro_rules!` suits local syntactic repetition and token matching. A procedural macro is appropriate when parsing and generating richer syntax justifies a separate proc-macro crate, build cost, and diagnostic burden. Keep generated public APIs understandable without reading the generator. A large macro is not automatically simpler than a small amount of explicit code.

**Review.** Check fragment specifiers, repetition separators, balanced delimiters, evaluation count, and name resolution. An expression argument used twice can run its side effects twice. Use `$crate` for exported declarative macro helpers when appropriate; it does not bypass privacy. Textual and path-based macro scopes differ. Procedural macros are unhygienic, so generated identifiers and paths must not accidentally depend on caller imports. Check edition-specific fragment behavior against the macro definition's edition. [Declarative rules](https://doc.rust-lang.org/reference/macros-by-example.html) · [Procedural rules](https://doc.rust-lang.org/reference/procedural-macros.html).

**Verification.** Compile from a separate consumer crate, including renamed dependencies where supported. Exercise malformed input and diagnostics, caller name collisions, empty/multiple repetitions, and a side-effecting argument when evaluation count matters. Test generated behavior, not only pretty-printed expansion. The errata's malformed delimiters are source-listing repairs, not patterns to copy.

[Book evidence](rustaceans-sources.md#inspected-pdf-passages) · [Corrections](rustaceans-errata.md)
