from langchain_openai import ChatOpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_API_KEY = "ollama"

model = ChatOpenAI(
    model="llama3.2",
    temperature=0.8,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=OLLAMA_API_KEY,
    base_url="http://localhost:11434/v1"
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to German. Translate the user sentence.",
    ),
    (
        "human", "I love Artificial intelligence."
    ),
]
ai_msg = model.invoke(messages)

print(ai_msg.content)