# Document names and recoverable errors

This original example has one supplied rule: a document name must not be empty after trimming. It adds no length, character-set, or uniqueness rule. The following is a complete standard-library program; the type and error model are local examples, not a required application API. [Types](../references/types.md), [errors](../references/errors.md), and [book-derived evidence](../references/sources.md#verified-book-principles) explain the choices.

```rust
use std::error::Error;
use std::fmt;

#[derive(Clone, Eq, PartialEq)]
struct DocumentName(String);

#[derive(Debug)]
struct EmptyDocumentName;

impl fmt::Display for EmptyDocumentName {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "document name is empty")
    }
}
impl Error for EmptyDocumentName {}

impl TryFrom<String> for DocumentName {
    type Error = EmptyDocumentName;

    fn try_from(raw: String) -> Result<Self, Self::Error> {
        if raw.trim().is_empty() {
            Err(EmptyDocumentName)
        } else {
            Ok(Self(raw)) // Preserve display spelling; trim only for validation.
        }
    }
}

impl DocumentName {
    fn as_str(&self) -> &str { &self.0 }
}

fn main() {
    assert!(DocumentName::try_from("  ".to_owned()).is_err());
    let name = DocumentName::try_from(" Draft ".to_owned()).unwrap();
    assert_eq!(name.as_str(), " Draft ");
}
```

The private field and fallible conversion make ordinary construction explicit. They do not validate a `serde` derive, ORM mapping, stored JSON, unsafe code, or a future mutable accessor. If persistence restores a primitive, call the same validator or use custom deserialization and define how historical invalid records fail. Do not assert that a particular restoration path is safe without inspecting it.

At an ingest boundary, a caller might need these distinct outcomes:

```text
BadName          -> reject request; do not retry
StorageUnavailable { source } -> retry policy may apply; record safe operation context
```

An application error can preserve the storage source while a handler maps `BadName` to a client response and storage failure to a generic server response. The response must not expose SQL, credentials, or submitted document contents. An opaque error report is enough where no caller branches; typed variants are justified where retry behavior differs. Avoid converting both to one string before the decision. This sketch deliberately omits database and HTTP APIs; verify those against the actual service and pinned versions.
