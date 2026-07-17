import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document


class DocumentationLoader:
    def __init__(self):
        pass

    def load(self, urls):
        """
        Downloads each URL and converts it into LangChain Documents.
        """

        documents = []

        for url in urls:
            try:
                print(f"Loading: {url}")

                response = requests.get(url, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")

                # Remove unwanted elements
                for tag in soup(
                    ["script", "style", "nav", "header", "footer"]
                ):
                    tag.decompose()

                text = soup.get_text(separator=" ", strip=True)

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": url
                        }
                    )
                )

            except Exception as e:
                print(f"Failed to load {url}")
                print(e)

        print(f"\nLoaded {len(documents)} documents.")

        return documents