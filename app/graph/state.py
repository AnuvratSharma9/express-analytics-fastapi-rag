from typing import TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    question: str
    rewritten_query: str
    documents: list[Document]
    answer: str
    sources: list[str]
    retries: int
    grounded: bool