import os
import httpx
from dotenv import load_dotenv

from pymilvus import MilvusClient

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# ==========================
# NAI Configuration
# ==========================
NAI_ENDPOINT = os.getenv("NAI_ENDPOINT")
NAI_API_KEY = os.getenv("NAI_API_KEY")
EMBED_MODEL = os.getenv("EMBED_MODEL")

# ==========================
# Milvus Configuration
# ==========================
MILVUS_URI = os.getenv("MILVUS_URI")  # e.g. http://10.38.30.50:19530
MILVUS_DATABASE = "test"
MILVUS_COLLECTION = "test_collection4"


def get_embedding(text: str):
    url = f"{NAI_ENDPOINT}/embeddings"

    headers = {
        "Authorization": f"Bearer {NAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": EMBED_MODEL,
        "input": text,
    }

    response = httpx.post(
        url,
        headers=headers,
        json=payload,
        timeout=60,
        verify=False,
    )

    response.raise_for_status()

    return response.json()["data"][0]["embedding"]


def load_documents():
    loader = PyPDFDirectoryLoader("./media")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    splits = splitter.split_documents(docs)

    return [
        d for d in splits
        if d.page_content.strip()
    ]


def main():

    client = MilvusClient(
        uri=MILVUS_URI,
        db_name=MILVUS_DATABASE,
    )

    stats = client.get_collection_stats(
        collection_name=MILVUS_COLLECTION
    )

    print("Collection Stats:")
    print(stats)

    splits = load_documents()

    data = []

    for i, doc in enumerate(splits):

        print(f"Embedding {i+1}/{len(splits)}")

        emb = get_embedding(doc.page_content)

        print("Dimension:", len(emb))

        data.append({
            "emb": emb,
            "content": doc.page_content
        })

    client.insert(
        collection_name=MILVUS_COLLECTION,
        data=data,
    )

    print("Inserted:", len(data))

    query = get_embedding("What is Nutanix Enterprise AI?")

    results = client.search(
        collection_name=MILVUS_COLLECTION,
        data=[query],
        anns_field="emb",
        limit=5,
    )

    print(results)


if __name__ == "__main__":
    main()