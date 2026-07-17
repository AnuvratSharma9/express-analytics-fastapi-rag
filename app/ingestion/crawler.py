from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class DocumentationCrawler:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.visited = set()

    def crawl(self):
        """
        Crawl the documentation website and return all internal documentation URLs.
        """
        print(f"Crawling {self.base_url}")

        response = requests.get(self.base_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        urls = set()

        for link in soup.find_all("a", href=True):

            href = link["href"]

            absolute_url = urljoin(self.base_url, href)

            parsed = urlparse(absolute_url)

            # Only keep FastAPI documentation pages
            if parsed.netloc != urlparse(self.base_url).netloc:
                continue

            # Remove URL fragments (#section)
            absolute_url = absolute_url.split("#")[0]

            # Ignore static assets
            if any(
                absolute_url.endswith(ext)
                for ext in (
                    ".png",
                    ".jpg",
                    ".jpeg",
                    ".svg",
                    ".gif",
                    ".css",
                    ".js",
                    ".ico",
                    ".xml",
                    ".json",
                )
            ):
                continue

            urls.add(absolute_url.rstrip("/"))

        urls = sorted(urls)

        print(f"Found {len(urls)} documentation pages.")

        return urls