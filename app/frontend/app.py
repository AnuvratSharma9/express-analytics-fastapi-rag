import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="Adaptive RAG Chatbot",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Adaptive RAG Chatbot")
st.caption("Powered by LangGraph • FastAPI • ChromaDB • Groq")

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat
# -----------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            st.markdown("#### 📚 Sources")

            for src in message["sources"]:
                st.write(f"- {src}")

# -----------------------------
# Chat Input
# -----------------------------

if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": prompt},
                    timeout=120,
                )

                response.raise_for_status()

                data = response.json()

                answer = data["answer"]
                sources = data.get("sources", [])

                st.markdown(answer)

                if sources:
                    st.markdown("#### 📚 Sources")

                    for src in sources:
                        st.write(f"- {src}")

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )

            except Exception as e:
                st.error(f"Error: {e}")