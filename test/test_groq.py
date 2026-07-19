from app.llm.groq import GroqLLM

llm = GroqLLM().get_llm()

response = llm.invoke("What is FastAPI?")

print(response.content)