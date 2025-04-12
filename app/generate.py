import asyncio

from openai import AsyncOpenAI
from config import token

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="token",
)

async def aigenerate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324", #здесь сами можем поставить модель из документации openrouter
    messages=[
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  )
  print(completion)
  return completion.choises[0].message.content
