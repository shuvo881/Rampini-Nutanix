from src.rag.embedding import get_embedding
from src.rag.llm import generate
from src.rag.milvus_db import get_client
from src.rag.config import MILVUS_COLLECTION





def search(question: str, limit: int = 5) -> str:
    """Search relevant documents from Milvus."""

    emb = get_embedding(question)
    client = get_client()

    results = client.search(
        collection_name=MILVUS_COLLECTION,
        data=[emb],
        anns_field="emb",
        limit=limit,
        output_fields=["content"],
    )

    return "\n\n".join(
        hit["entity"]["content"]
        for hit in results[0]
    )


def answer_question(question: str) -> str:
    """Retrieve context and generate an answer."""

    context = search(question)

    prompt = f"""Context:
        {context}

        Question:
        {question}

        Answer using only the context. If the answer is not present in the context, say "I don't know based on the provided documents."
    """

    return generate(prompt)