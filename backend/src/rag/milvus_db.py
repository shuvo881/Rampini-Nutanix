from pymilvus import MilvusClient

from src.rag.config import (
    MILVUS_URI,
    MILVUS_DATABASE,
)


def get_client():
    return MilvusClient(
        uri=MILVUS_URI,
        db_name=MILVUS_DATABASE,
    )