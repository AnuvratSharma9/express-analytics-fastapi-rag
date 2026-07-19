import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class GroqLLM:

    def __init__(
        self,
        model_name: str = "llama-3.3-70b-versatile",
        temperature: float = 0,
    ):

        self.llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv("GROQ_API_KEY"),
        )

    def get_llm(self):
        return self.llm