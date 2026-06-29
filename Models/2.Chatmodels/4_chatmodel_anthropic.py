from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-sonnet-4-0",
    temperature=0.2,
    max_tokens=100
)

result = model.invoke("What is the capital of India?")

print(result.content)