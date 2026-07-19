# Express Analytics – Adaptive RAG Assistant

An **Adaptive Retrieval-Augmented Generation (Adaptive RAG)** system developed as part of the **Express Analytics AI/ML Engineer Internship Assignment**.

The project combines **FastAPI**, **LangGraph**, **ChromaDB**, **Groq LLM**, and **Tavily Search** to build an intelligent documentation assistant capable of retrieving relevant information, rewriting ambiguous queries, detecting hallucinations, and performing web search fallback when required.

---

# 🚀 Features

- Adaptive RAG workflow using LangGraph
- Documentation ingestion from any website
- Semantic search using ChromaDB
- Query analysis and routing
- Document relevance grading
- Query rewriting
- Hallucination detection
- Web search fallback using Tavily
- REST APIs with FastAPI
- Interactive Streamlit frontend
- Source citation support
- User feedback collection

---

# 🏗️ Document Ingestion Pipeline

The ingestion pipeline converts raw documentation into a searchable vector knowledge base.

The pipeline performs the following operations:

- Crawl documentation URLs
- Load webpage contents
- Split documents into semantic chunks
- Generate vector embeddings
- Store embeddings in ChromaDB

<p align="center">
    <img src="images/ingestion-pipeline.png" alt="Document Ingestion Pipeline" width="900">
</p>

<p align="center">
    <em>Figure 1. End-to-end document ingestion pipeline.</em>
</p>

---

# 🧠 Adaptive RAG Workflow

After the documentation has been indexed, every incoming user query passes through an adaptive workflow powered by **LangGraph**.

Unlike a traditional RAG pipeline, the workflow dynamically decides whether to:

- Retrieve documents
- Rewrite the user query
- Generate an answer
- Verify answer grounding
- Perform web search when necessary

This adaptive routing significantly improves answer quality while reducing hallucinations.

<p align="center">
    <img src="images/langgraph-rag-workflow.png" alt="Adaptive RAG Workflow" width="950">
</p>

<p align="center">
    <em>Figure 2. Adaptive RAG workflow implemented using LangGraph.</em>
</p>

---

# 💻 Streamlit User Interface

The frontend is developed using **Streamlit**, providing a simple and interactive interface for communicating with the assistant.

Users can:

- Ask documentation-related questions
- Receive grounded answers
- View retrieved sources
- Interact with the assistant in real time

<p align="center">
    <img src="images/ui.png" alt="Streamlit UI" width="900">
</p>

<p align="center">
    <em>Figure 3. Streamlit User Interface.</em>
</p>

---

# ⚙️ REST API

The backend exposes REST APIs for ingestion, querying, document inspection, and feedback collection.

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/ingest` | Ingest documentation into ChromaDB |
| POST | `/query` | Execute Adaptive RAG workflow |
| GET | `/documents` | View indexed documents |
| POST | `/feedback` | Store user feedback |

---

# 📥 Document Ingestion Endpoint

The `/ingest` endpoint crawls documentation from the provided URL, creates embeddings, and stores them inside ChromaDB.

<p align="center">
    <img src="images/ingest-endpoint.png" alt="Ingest Endpoint" width="900">
</p>

<p align="center">
    <em>Figure 4. Successful document ingestion.</em>
</p>

---

# 💬 Query Endpoint

The `/query` endpoint executes the complete Adaptive RAG workflow and returns grounded responses along with supporting sources.

<p align="center">
    <img src="images/query-endpoint.png" alt="Query Endpoint" width="900">
</p>

<p align="center">
    <em>Figure 5. Query execution using Adaptive RAG.</em>
</p>

---

# 📚 Documents Endpoint

The `/documents` endpoint displays all indexed documentation sources currently stored inside ChromaDB.

<p align="center">
    <img src="images/documents-endpoint.png" alt="Documents Endpoint" width="900">
</p>

<p align="center">
    <em>Figure 6. Indexed documentation sources.</em>
</p>

---

# ⭐ Feedback Endpoint

The `/feedback` endpoint allows users to rate generated responses.

User feedback is stored inside a JSON file and can later be used for evaluation and future improvements.

<p align="center">
    <img src="images/feedback-endpoint-jsonfile.png" alt="Feedback Endpoint" width="850">
</p>

<p align="center">
    <em>Figure 7. Feedback endpoint storing responses in JSON.</em>
</p>

---

# 📂 Project Structure

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
│   ├── ingestion-pipeline.png
│   ├── langgraph-rag-workflow.png
│   ├── ui.png
│   ├── ingest-endpoint.png
│   ├── query-endpoint.png
│   ├── documents-endpoint.png
│   └── feedback-endpoint-jsonfile.png
│
├── test/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── main.py
```

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Workflow Engine | LangGraph |
| LLM | Groq |
| Vector Database | ChromaDB |
| Web Search | Tavily Search |
| Embeddings | HuggingFace Embeddings |
| Parsing | BeautifulSoup |
| Validation | Pydantic |

---

# 📦 Installation

## Clone the repository

```bash
git clone https://github.com/AnuvratSharma9/express-analytics-fastapi-rag.git
cd express-analytics-fastapi-rag
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Run FastAPI

```bash
uvicorn main:app --reload
```

FastAPI Documentation:

```
http://127.0.0.1:8000/docs
```

## Run Streamlit

```bash
streamlit run app/frontend/app.py
```

---

# 🔄 Adaptive RAG Workflow

```text
User Query
     │
     ▼
Query Analysis
     │
     ▼
Retrieve Documents
     │
     ▼
Grade Documents
     │
 ┌───┴─────────────┐
 │                 │
 ▼                 ▼
Generate      Rewrite Query
 │                 │
 ▼                 │
Hallucination Check│
 │                 │
 ├────Grounded────►END
 │
 ▼
Web Search
 │
 ▼
Generate Final Answer
 │
 ▼
END
```

---

# 🔮 Future Improvements

- Hybrid Retrieval (BM25 + Vector Search)
- Incremental document indexing
- Authentication and user management
- Persistent feedback database
- Conversation memory
- Docker deployment
- Kubernetes support

---

# 👨‍💻 Author

**Anuvrat Sharma**

AI/ML Engineer | Python | FastAPI | LangGraph | LLMs | Retrieval-Augmented Generation
