from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState

from app.graph.nodes import (
    analyze_query,
    retrieve,
    grade_documents,
    rewrite_query,
    generate,
    hallucination_check,
    decide_next_step,
    decide_hallucination,
)

from app.search.web_search import web_search_node

workflow = StateGraph(GraphState)

# ======================================================
# Nodes
# ======================================================

workflow.add_node("analyze", analyze_query)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("rewrite_query", rewrite_query)
workflow.add_node("web_search", web_search_node)
workflow.add_node("generate", generate)
workflow.add_node("hallucination_check", hallucination_check)

# ======================================================
# Initial Flow
# ======================================================

workflow.add_edge(START, "analyze")
workflow.add_edge("analyze", "retrieve")
workflow.add_edge("retrieve", "grade_documents")

# ======================================================
# Grade Documents Decision
# ======================================================

workflow.add_conditional_edges(
    "grade_documents",
    decide_next_step,
    {
        "generate": "generate",
        "rewrite": "rewrite_query",
        "web_search": "web_search",
    },
)

# ======================================================
# Rewrite Path
# ======================================================

workflow.add_edge(
    "rewrite_query",
    "retrieve",
)

# ======================================================
# Web Search Path
# ======================================================

workflow.add_edge(
    "web_search",
    "generate",
)

# ======================================================
# Hallucination Check
# ======================================================

workflow.add_edge(
    "generate",
    "hallucination_check",
)

workflow.add_conditional_edges(
    "hallucination_check",
    decide_hallucination,
    {
        "end": END,
        "web_search": "web_search",
    },
)

graph = workflow.compile()