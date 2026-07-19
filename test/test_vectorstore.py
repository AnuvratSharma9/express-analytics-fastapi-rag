from app.ingestion.crawler import DocumentationCrawler
from app.ingestion.loader import DocumentationLoader
from app.ingestion.splitter import DocumentSplitter
from app.ingestion.embeddings import EmbeddingModel
from app.ingestion.vectorstore import VectorStore


crawler = DocumentationCrawler(
    "https://fastapi.tiangolo.com"
)

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

print("Vector database created successfully.")