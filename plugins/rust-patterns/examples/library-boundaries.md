# Borrowing, dispatch, and partial progress

The original [runnable example](library-boundaries.rs) models a byte-to-display-text boundary. It illustrates [interface](../references/interfaces.md) and [initialization](../references/unsafe.md) decisions without copying book listings.

`display_text` returns borrowed text when possible and an allocated repair when necessary. The caller still owns its byte buffer. Lossy repair is appropriate only for display; a protocol requiring valid UTF-8 should reject invalid input instead.

`accepted_by` accepts a concrete rule or a borrowed trait object. Runtime selection need not force `Box` or allocation. The trait's single method preserves dyn compatibility.

`append_available` deliberately promises partial progress, not transactional rollback. Safe `push` keeps vector length consistent on early stop and unwinding. A producer panic preserves completed additions; a caller needing all-or-nothing behavior requires a different contract. The drop-count test verifies each produced value is destroyed once. Catching an unwind in this test does not handle aborting panics.

From the plugin directory, compile and run the standalone tests into a temporary location:

```bash
rustc --edition=2021 --test examples/library-boundaries.rs -o /tmp/rust-patterns-library-tests
/tmp/rust-patterns-library-tests
```

These tests verify this example on the executing compiler and host. They do not certify an arbitrary unsafe replacement, foreign ABI, feature matrix, or MSRV.
