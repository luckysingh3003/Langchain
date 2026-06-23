from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=10
    
    # more create ke lye temp ke value 1. kuch rakho
   
)

response = llm.invoke("What is the capital of India?")
print(response.content)