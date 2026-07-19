from langchain_chroma import Chroma


class VectorStore:

    def __init__(
        self,
        embedding_function,
        persist_directory: str = "chroma_db"
    ):

        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_function,
        )

    def add_documents(self, documents):

        self.vectorstore.add_documents(documents)

        print(f"Stored {len(documents)} chunks in ChromaDB.")

    def get_vectorstore(self):

        return self.vectorstore