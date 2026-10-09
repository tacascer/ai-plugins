use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(transparent)]
pub struct DocumentName(String);

impl DocumentName {
    pub fn parse(raw: String) -> Result<Self, &'static str> {
        if raw.trim().is_empty() {
            return Err("document name must be nonempty");
        }
        Ok(Self(raw))
    }

    pub fn as_str(&self) -> &str {
        &self.0
    }
}

#[derive(Deserialize)]
pub struct StoredDocument {
    pub name: DocumentName,
}

pub fn restore_document(json: &str) -> Result<StoredDocument, serde_json::Error> {
    serde_json::from_str(json)
}
