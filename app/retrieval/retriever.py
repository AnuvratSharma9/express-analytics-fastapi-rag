from app.ingestion.embeddings import EmbeddingModel
from app.ingestion.vectorstore import VectorStore


class Retriever:

    def __init__(self):

        embedding_function = EmbeddingModel().get_embeddings()

        vector_store = VectorStore(
            embedding_function=embedding_function
        )

        self.retriever = (
            vector_store
            .get_vectorstore()
            .as_retriever(
                search_kwargs={"k": 4}
            )
        )

    def get_retriever(self):
        return self.retriever