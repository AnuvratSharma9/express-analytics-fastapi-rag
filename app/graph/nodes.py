from app.graph.state import GraphState
from app.llm.groq import GroqLLM
from app.retrieval.retriever import Retriever

from langchain_core.prompts import ChatPromptTemplate





# Initialize heavy objects only once
retriever = Retriever().get_retriever()
llm = GroqLLM().get_llm()

# Maximum number of query rewrite attempts
MAX_RETRIES = 2


def analyze_query(state: GraphState):
    """
    Rewrites the user's query to improve retrieval quality.
    """

    prompt = f"""
You are helping improve document retrieval for a RAG system.

Rewrite the user's question to make it more specific and retrieval-friendly.

Rules:
- Preserve the original meaning.
- Expand abbreviations if needed.
- Add relevant technical keywords if they are implied.
- Return exactly one rewritten query as plain text.
- Do not include explanations, markdown, quotation marks, bullet points, or labels.
- Do not answer the question.

User Question:
{state["question"]}
"""

    response = llm.invoke(prompt)

    return {
        "rewritten_query": response.content.strip()
    }


def retrieve(state: GraphState):
    """
    Retrieves the most relevant documents using the rewritten query.
    """

    documents = retriever.invoke(state["rewritten_query"])

    return {
        "documents": documents
    }


def grade_documents(state: GraphState):
    """
    Filters retrieved documents by checking whether they
    are relevant to the user's question.
    """

    filtered_documents = []

    for document in state["documents"]:

        prompt = f"""
You are a relevance grader for a Retrieval-Augmented Generation (RAG) system.

Determine whether the retrieved document contains information that can help answer the user's question.

Respond with ONLY one word:

yes

or

no

Question:
{state["question"]}

Document:
{document.page_content}
"""

        response = llm.invoke(prompt)

        grade = response.content.strip().lower()

        if grade.startswith("yes"):
            filtered_documents.append(document)

    return {
        "documents": filtered_documents
    }


def rewrite_query(state: GraphState):
    """
    Rewrites the query again when no relevant documents
    were found and increments the retry counter.
    """

    prompt = f"""
The previous retrieval did not return relevant documents.

Rewrite the user's question differently while preserving its meaning.

Original Question:
{state["question"]}

Previous Rewritten Query:
{state["rewritten_query"]}

Return only the rewritten query.
"""

    response = llm.invoke(prompt)

    return {
        "rewritten_query": response.content.strip(),
        "retries": state["retries"] + 1
    }


def decide_next_step(state: GraphState):
    """
    Decide whether to generate an answer,
    rewrite the query, or fall back to web search.
    """

    if len(state["documents"]) > 0:
        return "generate"

    if state["retries"] >= MAX_RETRIES:
        return "web_search"

    return "rewrite"
def generate(state: GraphState):

    context = "\n\n".join(
        [doc.page_content for doc in state["documents"]]
    )

    prompt = f"""
    You are an expert FastAPI assistant.

    Answer the user's question ONLY using the provided context.

    If the answer is not present in the context,
    respond with:
    "I couldn't find relevant information in the documentation."

    Context:
    {context}

    Question:
    {state["question"]}
    """

    response = llm.invoke(prompt)

    sources = []

    for document in state["documents"]:
        source = document.metadata.get("source")

        if source and source not in sources:
            sources.append(source)

    return {
        "answer": response.content,
        "sources": sources
    }



def hallucination_check(state):
    """
    Verifies whether the generated answer is supported by
    the retrieved context.
    """

    print("-----HALLUCINATION CHECK-----")

    context = "\n\n".join(
        doc.page_content
        for doc in state["documents"]
    )

    answer = state["answer"]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a hallucination detection assistant.

Your task is to determine whether the given answer is completely supported by the provided context.

Respond ONLY with:

yes

or

no
"""
            ),
            (
                "human",
                """
Context:

{context}

------------------------

Answer:

{answer}
"""
            )
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "answer": answer
        }
    )

    grounded = response.content.strip().lower().startswith("yes")

    return {
        "grounded": grounded
    }

def decide_hallucination(state):
    """
    If the answer is grounded, finish.
    Otherwise perform a web search.
    """

    if state["grounded"]:
        return "end"

    return "web_search"