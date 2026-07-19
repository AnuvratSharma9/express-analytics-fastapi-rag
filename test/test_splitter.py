from app.ingestion.crawler import DocumentationCrawler
from app.ingestion.loader import DocumentationLoader
from app.ingestion.splitter import DocumentSplitter


crawler = DocumentationCrawler(
    "https://fastapi.tiangolo.com"
)

urls = crawler.crawl()

loader = DocumentationLoader()

documents = loader.load(urls)

splitter = DocumentSplitter()

chunks = splitter.split(documents)

print()

print(f"Documents : {len(documents)}")

print(f"Chunks : {len(chunks)}")

print()

print(chunks[0].page_content[:500])

print()

print(chunks[0].metadata)