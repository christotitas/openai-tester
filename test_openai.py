import os
import httpx
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def test_openai():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4",
                "messages": [
                    {"role": "user", "content": "Bonjour, pouvez-vous répondre à cette question ?"}
                ]
            }
        )
        print(response.json())

import asyncio
asyncio.run(test_openai())
