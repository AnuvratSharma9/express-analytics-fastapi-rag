from app.ingestion.crawler import DocumentationCrawler
from app.ingestion.loader import DocumentationLoader

crawler = DocumentationCrawler(
    "https://fastapi.tiangolo.com"
)

urls = crawler.crawl()

loader = DocumentationLoader()

docs = loader.load(urls)

print(f"\nTotal documents: {len(docs)}")

print("\nMetadata:")
print(docs[0].metadata)

print("\nPreview:")
print(docs[0].page_content[:500])