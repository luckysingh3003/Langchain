from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L12-v2"
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal"
]

vectors = embedding.embed_documents(documents)

print("No. of vectors:", len(vectors))
print("Dimension:", len(vectors[0]))