import os

from tavily import TavilyClient
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def web_search(query: str, max_results: int = 3):
    """
    Performs a web search using Tavily.
    """

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=max_results,
    )

    return response["results"]


def web_search_node(state):
    """
    LangGraph node that performs a web search when
    retrieval fails or hallucination is detected.
    """

    query = state["question"]

    results = web_search(query)

    documents = []

    for result in results:
        documents.append(
            Document(
                page_content=result["content"],
                metadata={
                    "source": result["url"]
                },
            )
        )

    return {
        "documents": documents
    }