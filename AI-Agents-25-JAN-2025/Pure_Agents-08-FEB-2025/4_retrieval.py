# Pydantic is the most widely used data validation library for Python.

import json
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

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_kb",
            "description": "Get the answer to the user's question from the knowledge base.",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                },
                "required": ["question"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

system_prompt = "You are a helpful assistant that answers questions from the knowledge base about our e-commerce store."
user_prompt = "What is the return policy?"

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

#print('Messages : ', messages)
llm_with_tools = model.bind_tools(tools)
knowledge_base = llm_with_tools.invoke(messages)


#---------------------------------------------------------------------------------------------------------------
# Define the knowledge base file
#---------------------------------------------------------------------------------------------------------------

def search_kb(question: str):
    """
    Load the whole knowledge base from the JSON file.
    """
    with open("kb.json", "r") as f:
        return  json.load(f)


def call_function(name, args):
    if name == "search_kb":
        return  search_kb(**args)

def KB():
    print('knowledge_base : ', knowledge_base)
    for tool_call in knowledge_base.tool_calls:
        name = tool_call['name']
        args = tool_call['args']
        messages.append(knowledge_base)

        print('name : ', name)
        print('args : ', args)
        result =   call_function(name, args)

        # Working with Memory
        messages.append(
            {"role": "tool", "tool_call_id": tool_call['id'], "content": json.dumps(result)}
        )
#---------------------------------------------------------------------------------------------------------------
# Call function weather in sync order
#---------------------------------------------------------------------------------------------------------------

KB()

#---------------------------------------------------------------------------------------------------------------
# Data Structured of returned answer from LLM
#---------------------------------------------------------------------------------------------------------------

class KBResponse(BaseModel):
    answer: str = Field(description="The answer to the user's question.")
    source: int = Field(description="The record id of the answer.")


#print('messages : ', messages)
#---------------------------------------------------------------------------------------------------------------
# Call the LLM this time with Weather Context and more information for the LLM.
#---------------------------------------------------------------------------------------------------------------
structured_llm = model.with_structured_output(KBResponse)
completion_2 = structured_llm.invoke(messages)

#---------------------------------------------------------------------------------------------------------------
# Second call to LLM with Context
#---------------------------------------------------------------------------------------------------------------
print(completion_2)
print('-------------------')


#---------------------------------------------------------------------------------------------------------------
# Call LLM with question that don't trigger the tools and the LLM don't know the answer.
#---------------------------------------------------------------------------------------------------------------

new_user_prompt = "What is the weather in London?"

messages_new = [
    {
        "role":"system",
        "content":system_prompt
    },
    {
        "role": "user",
        "content":new_user_prompt
    }
]

llm_with_tools_new = model.bind_tools(tools)
knowledge_base_new = llm_with_tools_new.invoke(messages_new)
print(knowledge_base_new)