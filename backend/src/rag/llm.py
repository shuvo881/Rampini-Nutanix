import httpx

from src.rag.config import (
    CHAT_MODEL,
    CHAT_MODEL_API_KEY,
    CHAT_MODEL_ENDPOINT,
)


def generate(prompt: str):

    response = httpx.post(
        f"{CHAT_MODEL_ENDPOINT}",
        headers={
            "Authorization": f"Bearer {CHAT_MODEL_API_KEY}",
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
        timeout=600,
        verify=False,
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]