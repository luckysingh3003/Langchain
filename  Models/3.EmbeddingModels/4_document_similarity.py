import google.generativeai as genai
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMMNI_API_KEY"))

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about bumrah"

# Document Embeddings
doc_embeddings = [
    genai.embed_content(
        model="models/gemini-embedding-001",
        content=doc
    )["embedding"]
    for doc in documents
]

# Query Embedding
query_embedding = genai.embed_content(
    model="models/gemini-embedding-001",
    content=query
)["embedding"]

# Similarity
scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

index = np.argmax(scores)

print("Query:", query)
print("Best Match:", documents[index])
print("Similarity Score:", scores[index])