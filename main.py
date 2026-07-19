from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="FastAPI RAG Assistant",
    description="A RAG chatbot built using FastAPI, LangGraph, ChromaDB, and Groq",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "FastAPI RAG Assistant is running!"
    }