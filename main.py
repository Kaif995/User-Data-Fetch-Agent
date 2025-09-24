from agents import Agent,RunContextWrapper,Runner,function_tool,AsyncOpenAI,OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled
from dataclasses import dataclass 
import os
from dotenv import load_dotenv
import asyncio
import requests

set_tracing_disabled(True)
load_dotenv()

# Access environment variables
key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("base_url")

# Initialize Gemini client
gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

# Define model
Model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client
)
@function_tool
def fetch_user_data() ->list:
    """fetch function fo ruser data and return list"""
    url= "https://jsonplaceholder.typicode.com/users"
    print("fetch_user_data tool called")
    res= requests.get(url)
    return res.json()

async def main():

    agent=Agent(
        name="Kaif Shamim",
        instructions="You are a helpful assiatant& also reply with context of api given by me",
        tools=[fetch_user_data],
        model=Model
    )

    result= await Runner.run(
        starting_agent=agent,
        input="Please fetch and show me the list of user names with theor id."
    )

    print(result.final_output)





asyncio.run(main())  
