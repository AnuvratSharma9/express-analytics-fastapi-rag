from app.ingestion.crawler import DocumentationCrawler

crawler = DocumentationCrawler(
    "https://fastapi.tiangolo.com"
)

urls = crawler.crawl()

print(f"\nTotal URLs: {len(urls)}\n")

for url in urls[:20]:
    print(url)