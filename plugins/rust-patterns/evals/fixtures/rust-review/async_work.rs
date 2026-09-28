use std::{collections::HashMap, path::Path, sync::Arc, time::Duration};
use tokio::{sync::Mutex, time::timeout};

// RemoteIndexer and DocumentId are supplied by omitted service modules.
pub async fn render_preview(path: &Path) -> std::io::Result<String> {
    let source = std::fs::read_to_string(path)?;
    Ok(source.lines().take(20).collect::<Vec<_>>().join("\n"))
}

pub fn launch_index_notification(remote: Arc<RemoteIndexer>, id: DocumentId) {
    let handle = tokio::spawn(async move { remote.index(id).await });
    drop(handle);
}

pub async fn update_cache_and_index(
    cache: Arc<Mutex<HashMap<DocumentId, String>>>,
    remote: &RemoteIndexer,
    id: DocumentId,
    preview: String,
) -> Result<(), IndexError> {
    let mut entries = cache.lock().await;
    entries.insert(id.clone(), preview);
    remote.index(id).await?;
    Ok(())
}

pub async fn publish_with_deadline(
    remote: &RemoteIndexer,
    id: DocumentId,
) -> Result<(), PublishError> {
    timeout(Duration::from_secs(2), remote.publish(id))
        .await
        .map_err(|_| PublishError::TimedOut)??;
    Ok(())
}
