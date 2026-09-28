#[tracing::instrument]
pub async fn ingest_document(
    request_id: &str,
    authorization_token: String,
    body: Vec<u8>,
) -> Result<(), IngestError> {
    // Omitted ingestion steps use the token to call the indexer.
    submit_to_indexer(&authorization_token, &body).await?;
    tracing::info!(%request_id, "document ingested");
    Ok(())
}
