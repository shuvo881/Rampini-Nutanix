import httpx

from src.rag.config import (
    NAI_API_KEY,
    NAI_ENDPOINT,
    EMBED_MODEL,
)


def get_embedding(text: str):

    response = httpx.post(
        f"{NAI_ENDPOINT}/embeddings",
        headers={
            "Authorization": f"Bearer {NAI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": EMBED_MODEL,
            "input": text,
        },
        timeout=60,
        verify=False,
    )

    response.raise_for_status()

    return response.json()["data"][0]["embedding"]