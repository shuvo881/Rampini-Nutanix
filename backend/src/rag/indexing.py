from src.rag.embedding import get_embedding
from src.rag.document_loader import load_documents
from src.rag.milvus_db import get_client
from src.rag.config import MILVUS_COLLECTION


def index_documents():
    """Load documents, generate embeddings, and insert them into Milvus."""

    client = get_client()
    docs = load_documents()

    data = []

    for i, doc in enumerate(docs):
        print(f"Embedding {i + 1}/{len(docs)}")

        data.append({
            "emb": get_embedding(doc.page_content),
            "content": doc.page_content,
        })

    client.insert(
        collection_name=MILVUS_COLLECTION,
        data=data,
    )

    print(f"\n✅ Successfully indexed {len(data)} documents.")


if __name__ == "__main__":
    index_documents()