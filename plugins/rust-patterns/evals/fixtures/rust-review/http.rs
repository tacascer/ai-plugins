// Notifications are sent repeatedly to the same remote origin.
pub async fn send_notification(
    endpoint: &str,
    document_id: &str,
) -> Result<(), reqwest::Error> {
    let client = reqwest::Client::new();
    client
        .post(endpoint)
        .json(&serde_json::json!({ "document_id": document_id }))
        .send()
        .await?
        .error_for_status()?;
    Ok(())
}
