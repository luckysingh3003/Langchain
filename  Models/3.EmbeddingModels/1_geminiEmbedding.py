import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMMNI_API_KEY"))

result = genai.embed_content(
    model="models/gemini-embedding-001",
    content="What is Artificial Intelligence?"
)

embedding = result["embedding"]

print("Dimension:", len(embedding))
print(embedding[:32])