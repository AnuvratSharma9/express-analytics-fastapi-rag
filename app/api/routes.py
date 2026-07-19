from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from app.graph.graph import graph
import json
import os

from app.ingestion.ingest import ingest_documents
from app.ingestion.embeddings import EmbeddingModel
from app.ingestion.vectorstore import VectorStore

router = APIRouter()


# -------------------------
# Query Models
# -------------------------

class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[str]


# -------------------------
# Ingest Model
# -------------------------

class IngestRequest(BaseModel):
    url: str


# -------------------------
# Feedback Model
# -------------------------

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: str
    comment: Optional[str] = None


# -------------------------
# Query Endpoint
# -------------------------

@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):

    result = graph.invoke(
        {
            "question": request.question,
            "rewritten_query": "",
            "documents": [],
            "answer": "",
            "retries": 0,
        }
    )

    return QueryResponse(
        question=request.question,
        answer=result["answer"],
        sources=result["sources"],
    )


# -------------------------
# Ingest Endpoint
# -------------------------

@router.post("/ingest")
def ingest(request: IngestRequest):

    chunks = ingest_documents(request.url)

    return {
        "message": "Documents ingested successfully.",
        "chunks_indexed": chunks,
    }


# -------------------------
# Documents Endpoint
# -------------------------

@router.get("/documents")
def list_documents():

    embedding_model = EmbeddingModel()

    vectorstore = VectorStore(
        embedding_function=embedding_model.get_embeddings()
    )

    collection = vectorstore.get_vectorstore()

    data = collection.get()

    sources = set()

    for metadata in data["metadatas"]:
        if metadata and metadata.get("source"):
            sources.add(metadata["source"])

    return {
        "total_documents": len(sources),
        "documents": [
            {"source": source}
            for source in sorted(sources)
        ],
    }
# -------------------------
# Feedback Endpoint
# -------------------------

@router.post("/feedback")
def feedback(request: FeedbackRequest):

    filename = "feedback.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(request.model_dump())

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Feedback received successfully."
    }