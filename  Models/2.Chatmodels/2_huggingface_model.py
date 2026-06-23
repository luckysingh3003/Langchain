from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of India?")

print(response.content)