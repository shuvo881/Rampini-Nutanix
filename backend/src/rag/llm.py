import httpx

from src.rag.config import (
    CHAT_MODEL,
    NAI_API_KEY,
    NAI_ENDPOINT,
)


def generate(prompt: str):

    response = httpx.post(
        f"{NAI_ENDPOINT}/chat/completions",
        headers={
            "Authorization": f"Bearer {NAI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": CHAT_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": 0,
        },
        timeout=120,
        verify=False,
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]