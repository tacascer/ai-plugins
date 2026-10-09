// The schema and DocumentId definition are outside this excerpt.
pub async fn store_document_and_receipt(
    pool: &sqlx::PgPool,
    id: &str,
    name: &str,
) -> Result<(), sqlx::Error> {
    sqlx::query("INSERT INTO documents (id, name) VALUES ($1, $2)")
        .bind(id)
        .bind(name)
        .execute(pool)
        .await?;

    sqlx::query("INSERT INTO delivery_receipts (document_id) VALUES ($1)")
        .bind(id)
        .execute(pool)
        .await?;
    Ok(())
}
