# Express Analytics – Adaptive RAG Assistant

## Overview

An Adaptive Retrieval-Augmented Generation (RAG) assistant developed for the Express Analytics AI/ML Engineer Internship Assignment.

The assistant combines LangGraph, ChromaDB, Groq LLM, and Tavily Search to build an intelligent documentation assistant capable of adaptive retrieval, query rewriting, hallucination detection, and web search fallback.

---

# System Architecture

The system consists of two major phases:

1. **Document Ingestion Pipeline**
2. **Adaptive RAG Query Pipeline**


---

# Document Ingestion Pipeline

The ingestion pipeline is responsible for converting raw documentation into searchable vector embeddings.

The pipeline performs the following steps:

- Crawl documentation URLs
- Load webpage contents
- Split documents into chunks
- Generate embeddings
- Store embeddings in ChromaDB


# Adaptive RAG Workflow

Once the documents are indexed, every user query passes through an adaptive workflow powered by LangGraph.

The workflow consists of:

- Query Analysis
- Document Retrieval
- Document Grading
- Query Rewriting
- Answer Generation
- Hallucination Detection
- Web Search Fallback (if required)



---

# Streamlit User Interface

The Streamlit application provides an intuitive chat interface for interacting with the RAG assistant.

Features include:

- Chat Interface
- Source Citations
- Response Generation
- Chat History


---

# FastAPI Backend

The backend exposes REST APIs for document ingestion, querying, document inspection, and feedback collection.

Implemented endpoints:

- POST /ingest
- POST /query
- GET /documents
- POST /feedback



---

# Document Ingestion API

The ingestion endpoint accepts a documentation URL and indexes it into ChromaDB.

Example request:

```json
{
    "url":"https://fastapi.tiangolo.com"
}
```

Successful execution:



---

# Query Endpoint

The query endpoint executes the Adaptive RAG workflow and returns grounded responses together with source references.

Example:

```json
{
    "question":"How does dependency injection work?"
}
```

Example response:



---

# Indexed Documents Endpoint

The documents endpoint returns all indexed documentation sources currently stored in the vector database.



---

# Feedback Endpoint

The feedback endpoint allows users to rate generated responses.

The collected feedback is stored in a JSON file and can later be used for evaluation or model improvement.

---

# Project Structure

```text
express-analytics-rag-assistant/
│
├── app/
│   ├── graph/
│   ├── ingestion/
│   ├── llm/
│   ├── retrieval/
│   ├── search/
│
├── images/
├── tests/
├── main.py
├── requirements.txt
├── README.md
```

---

# Tech Stack

- Python
- FastAPI
- Streamlit
- LangGraph
- LangChain
- ChromaDB
- Groq
- Tavily Search
- BeautifulSoup
- Pydantic

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

## Run FastAPI

```bash
uvicorn main:app --reload
```

## Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

# Future Improvements

- Incremental indexing
- Multi-document ingestion
- Authentication
- Persistent feedback database
- Conversation memory
- Hybrid retrieval

---

# Author

**Anuvrat Sharma**
