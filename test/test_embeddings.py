from app.ingestion.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()

embeddings = embedding_model.get_embeddings()

vector = embeddings.embed_query(
    "What is FastAPI?"
)

print(len(vector))

print(vector[:10])