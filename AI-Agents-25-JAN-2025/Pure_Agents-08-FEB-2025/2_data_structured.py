# Pydantic is the most widely used data validation library for Python.
from pydantic import BaseModel
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

# Python library to define the response format into a pydantic model
class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]



messages = [
    {
        "role":"system",
        "content":"Extract the event information."
    },
    {
        "role": "user",
        "content":"Chris and Thomas are going to a AI Conferences on Saturday February 15th."
    }
]
structured_llm = model.with_structured_output(CalendarEvent)
event = structured_llm.invoke(messages)
print(event)
print('Name : ',event.name)
print('Date : ',event.date)
print('Who  : ',event.participants)

