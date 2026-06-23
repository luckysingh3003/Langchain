import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

print(os.getenv("GEMMNI_API_KEY"))  # check

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMMNI_API_KEY")
)

response = llm.invoke("What is the capital of India?")

print(response)