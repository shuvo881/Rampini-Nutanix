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
MILVUS_URI = os.getenv("MILVUS_URI")
MILVUS_DATABASE = os.getenv("MILVUS_DATABASE")
MILVUS_COLLECTION = os.getenv("MILVUS_COLLECTION")


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


def load_documents():
    loader = PyPDFDirectoryLoader("./media")

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    return splitter.split_documents(docs)


def index_documents():

    client = MilvusClient(
        uri=MILVUS_URI,
        db_name=MILVUS_DATABASE,
    )

    docs = load_documents()

    data = []

    for i, doc in enumerate(docs):

        print(f"Embedding {i+1}/{len(docs)}")

        embedding = get_embedding(doc.page_content)

        data.append({
            "emb": embedding,
            "content": doc.page_content,
        })

    client.insert(
        collection_name=MILVUS_COLLECTION,
        data=data,
    )

    print(f"\nInserted {len(data)} documents.")


if __name__ == "__main__":
    index_documents()