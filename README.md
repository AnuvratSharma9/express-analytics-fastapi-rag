# Express Analytics – Adaptive RAG Assistant

An **Adaptive Retrieval-Augmented Generation (Adaptive RAG)** assistant developed as part of the **Express Analytics AI/ML Engineer Internship Assignment**.

The application combines **FastAPI**, **LangGraph**, **ChromaDB**, **Groq LLM**, and **Tavily Search** to answer user queries using retrieved documentation while minimizing hallucinations through document grading, query rewriting, and web-search fallback.

---

## Features

- Adaptive RAG workflow using LangGraph
- Documentation ingestion from any website
- Semantic search using ChromaDB
- Query analysis and routing
- Document relevance grading
- Query rewriting for improved retrieval
- Hallucination detection
- Web search fallback using Tavily
- FastAPI REST APIs
- Streamlit User Interface
- Source citation support
- Feedback collection endpoint

---

# System Architecture

The application consists of two primary workflows:

1. **Document Ingestion Pipeline**
2. **Adaptive RAG Query Pipeline**

---

# Document Ingestion Pipeline

The ingestion pipeline converts raw documentation into a searchable vector database.

The pipeline performs the following operations:

- Crawl documentation URLs
- Load webpage contents
- Split documents into semantic chunks
- Generate vector embeddings
- Store embeddings in ChromaDB

<p align="center">
    <img src="images/ingestion-pipeline.png" width="900">
</p>

<p align="center">
<i>Figure 1. End-to-end document ingestion pipeline.</i>
</p>

---

# Adaptive RAG Workflow

After ingestion, every user query is processed through an adaptive workflow powered by **LangGraph**.

Instead of following a fixed pipeline, the system dynamically decides whether to:

- Retrieve documents
- Rewrite the query
- Generate an answer
- Verify grounding
- Perform web search if necessary

This adaptive routing significantly improves answer quality while reducing hallucinations.

<p align="center">
    <img src="images/langgraph-rag-workflow.png" width="950">
</p>

<p align="center">
<i>Figure 2. Adaptive RAG workflow implemented using LangGraph.</i>
</p>

---

# Streamlit User Interface

The frontend is developed using **Streamlit**, providing a clean and interactive chat interface.

Users can:

- Ask questions
- Receive grounded responses
- View retrieved sources
- Interact with the RAG assistant in real time

<p align="center">
    <img src="images/ui.png" width="900">
</p>

<p align="center">
<i>Figure 3. Streamlit interface.</i>
</p>

---

# REST API

The backend exposes four REST endpoints.

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/ingest` | Ingest documentation into ChromaDB |
| POST | `/query` | Execute Adaptive RAG workflow |
| GET | `/documents` | View indexed documentation |
| POST | `/feedback` | Store user feedback |

---

## Documentation Ingestion Endpoint

The `/ingest` endpoint indexes documentation from a provided URL.

<p align="center">
    <img src="images/ingest-endpoint.png" width="900">
</p>

<p align="center">
<i>Figure 4. Successful document ingestion.</i>
</p>

---

## Query Endpoint

The `/query` endpoint executes the Adaptive RAG workflow and returns grounded responses together with source references.

<p align="center">
    <img src="images/query-endpoint.png" width="900">
</p>

<p align="center">
<i>Figure 5. Adaptive RAG query execution.</i>
</p>

---

## Documents Endpoint

The `/documents` endpoint lists all indexed documentation sources stored inside ChromaDB.

<p align="center">
    <img src="images/documents-endpoint.png" width="900">
</p>

<p align="center">
<i>Figure 6. Indexed documentation.</i>
</p>

---

## Feedback Endpoint

Users can provide feedback on generated responses through the `/feedback` endpoint.

The feedback is stored inside a JSON file and can later be used for evaluation or future improvements.

<p align="center">
    <img src="images/feedback-endpoint-jsonfile.png" width="850">
</p>

<p align="center">
<i>Figure 7. Feedback storage endpoint.</i>
</p>

---

# Project Structure

```text
express-analytics-fastapi-rag/
│
├── app/
│   ├── api/
│   ├── frontend/
│   ├── graph/
│   ├── ingestion/
│   ├── llm/
│   ├── retrieval/
│   └── search/
│
├── images/
├── test/
├── README.md
├── requirements.txt
├── main.py
└── .env.example
```

---

# Tech Stack

| Category | Technologies |
|-----------|--------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Workflow | LangGraph |
| LLM | Groq |
| Vector Database | ChromaDB |
| Search | Tavily |
| Embeddings | HuggingFace Embeddings |
| Parsing | BeautifulSoup |
| Validation | Pydantic |

---

# Installation

Clone the repository

```bash
git clone https://github.com/AnuvratSharma9/express-analytics-fastapi-rag.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

Run the FastAPI backend

```bash
uvicorn main:app --reload
```

Run the Streamlit frontend

```bash
streamlit run app/frontend/app.py
```

---

# Future Improvements

- Hybrid Retrieval (BM25 + Vector Search)
- Multi-document ingestion
- Persistent database for feedback
- Conversation memory
- Authentication
- Incremental indexing
- Docker deployment

---

# Author

**Anuvrat Sharma**

AI/ML Engineer | Python | FastAPI | LangGraph | LLMs | RAG Systems
