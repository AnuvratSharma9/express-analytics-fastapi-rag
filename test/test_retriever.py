from app.retrieval.retriever import Retriever

retriever = Retriever().get_retriever()

query = "What is dependency injection in FastAPI?"

documents = retriever.invoke(query)

for i, doc in enumerate(documents, start=1):

    print("=" * 80)
    print(f"Document {i}")
    print("=" * 80)

    print(doc.page_content[:700])

    print("\nSource:")
    print(doc.metadata["source"])