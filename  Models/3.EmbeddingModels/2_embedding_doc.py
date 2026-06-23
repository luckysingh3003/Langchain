import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMMNI_API_KEY"))


texts = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Bangalore is India's Silicon Valley"
]


result = genai.embed_content(
    model="models/gemini-embedding-001",
    content=texts
)

 

embedding = result["embedding"]

print("Dimension:", len(embedding))
print(embedding)