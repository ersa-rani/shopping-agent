from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv,find_dotenv
import os

gemini_api_key=os.getenv("GEMINI_API_KEY")

external_client:AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model:OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)