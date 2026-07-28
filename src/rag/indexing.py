import os
import httpx
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

NAI_ENDPOINT = os.getenv("NAI_ENDPOINT")
NAI_API_KEY = os.getenv("NAI_API_KEY")
EMBED_MODEL = os.getenv("EMBED_MODEL")


def get_embedding(text: str):
    url = f"{NAI_ENDPOINT}/embeddings"

    headers = {
        "Authorization": f"Bearer {NAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": EMBED_MODEL,
        "input": text,
        "input_type": "string",
    }

    response = httpx.post(
        url,
        headers=headers,
        json=payload,
        timeout=60,
        verify=False,  # Remove if your certificate is valid
    )

    print("Status:", response.status_code)
    print(response.text)

    response.raise_for_status()

    return response.json()["data"][0]["embedding"]


def main():
    loader = PyPDFDirectoryLoader("./media")
    docs = loader.load()

    print("Pages:", len(docs))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    splits = splitter.split_documents(docs)

    splits = [d for d in splits if d.page_content.strip()]

    print("Chunks:", len(splits))

    for i, doc in enumerate(splits):
        print(f"\nEmbedding chunk {i+1}/{len(splits)}")

        embedding = get_embedding(doc.page_content)

        print("Embedding dimension:", len(embedding))

    print("\nDone!")


if __name__ == "__main__":
    main()