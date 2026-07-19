from app.llm.groq import GroqLLM
from app.retrieval.retriever import Retriever

llm = GroqLLM().get_llm()
retriever = Retriever().get_retriever()

query = "What is dependency injection in FastAPI?"

documents = retriever.invoke(query)

context = "\n\n".join(
    doc.page_content
    for doc in documents
)

prompt = f"""
You are an AI assistant that answers questions ONLY using the provided FastAPI documentation.

Instructions:
- Answer using only the provided context.
- If the answer is not present in the context, say:
  "I couldn't find that information in the provided documentation."
- Be concise and accurate.

Documentation:
{context}

Question:
{query}

Answer:
"""

response = llm.invoke(prompt)

print(response.content)