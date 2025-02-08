# Pydantic is the most widely used data validation library for Python.
# Asyncio is a library to write concurrent code using the async/await syntax.
# Aiohttp is Asynchronous HTTP Client/Server for asyncio and Python
import aiohttp
import json
import asyncio
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_API_KEY = "ollama"

model = ChatOpenAI(
    model="llama3.2",
    temperature=0.8,
    max_tokens=None,
    max_retries=2,
    api_key=OLLAMA_API_KEY,
    base_url=OLLAMA_BASE_URL
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates",
        "parameters": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"},
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True
}]

system_prompt = "You are a helpful weather assistant"
user_prompt = "What's the weather like in Pariss today?"

messages = [
    {
        "role":"system",
        "content":system_prompt
    },
    {
        "role": "user",
        "content":user_prompt
    }
]

llm_with_tools = model.bind_tools(tools)
location = llm_with_tools.invoke(messages)
#print('Messages : ', messages)

# https://open-meteo.com/
# Open Source Weather Information
async def get_weather(lat, lon):
    """This is a publicly available API that returns the weather for a given location"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m") as response:
            res = await response.json()
            return res

# Check if get Weather information is needed.
async def call_function(name, args):
    if name == "get_weathers":
        return  await asyncio.gather(get_weather(**args))

async def weather():
    print('location : ', location)
    for tool_call in location.tool_calls:
        name = tool_call['name']
        args = tool_call['args']
        messages.append(location)

        result =  await asyncio.gather(call_function(name, args))

        # Working with Memory
        messages.append(
            {"role": "tool", "tool_call_id": tool_call['id'], "content": json.dumps(result)}
        )

# Call function weather in sync order
asyncio.run(weather())

# Data Structured of returned answer from LLM
class WeatherResponse(BaseModel):
    temperature: float = Field( description="The current temperature in celsius for the given location.")
    response: str = Field(description="A natural language response to the user's question.")


#print('messages : ', messages)
# Call the LLM this time with Weather Context and more information for the LLM.
structured_llm = models.with_structured_output(WeatherResponse)
completion_2 = structured_llm.invoke(messages)
print('Second call to LLM with Context :  ',completion_2)