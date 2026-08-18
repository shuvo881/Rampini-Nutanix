import os

from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader, S3DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from .config import RAG_DOCS_DIR


def load_documents(path=RAG_DOCS_DIR):

    loader = PyPDFDirectoryLoader(path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    return splitter.split_documents(docs)


def load_documents_from_bucket(bucket_name=None):
    bucket_name = bucket_name or os.getenv("S3_BUCKET_NAME")

    loader = S3DirectoryLoader(
        bucket=bucket_name,
        endpoint_url=os.getenv("S3_ENDPOINT_URL"),
        aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
        use_ssl=True,
        verify=False,  # for self-signed certs in your lab
    )
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    return splitter.split_documents(docs)

def load_and_split(local_path: str):
    loader = PyPDFLoader(local_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)