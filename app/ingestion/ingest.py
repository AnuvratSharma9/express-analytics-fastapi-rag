from app.ingestion.crawler import DocumentationCrawler
from app.ingestion.loader import DocumentationLoader
from app.ingestion.splitter import DocumentSplitter
from app.ingestion.embeddings import EmbeddingModel
from app.ingestion.vectorstore import VectorStore


def ingest_documents(base_url: str):

    print("Starting ingestion pipeline...\n")

    crawler = DocumentationCrawler(base_url)
    urls = crawler.crawl()

    loader = DocumentationLoader()
    documents = loader.load(urls)

    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    embedding_model = EmbeddingModel()

    vectorstore = VectorStore(
        embedding_function=embedding_model.get_embeddings()
    )

    vectorstore.add_documents(chunks)

    print("\nIngestion completed successfully!")

    return len(chunks)

if __name__ == "__main__":
    ingest_documents("https://fastapi.tiangolo.com")