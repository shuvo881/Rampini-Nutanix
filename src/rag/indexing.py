from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def index_pdf_directory(directory_path: str):
    """Load all PDF files from a directory, split them, and index them into a vector store."""
    # 1. Load PDF files from the media directory
    loader = PyPDFDirectoryLoader(directory_path)
    docs = loader.load()

    # 2. Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)

    # 3. Initialize embeddings and vector store
    embeddings = OpenAIEmbeddings(
        base_url="http://localhost:11434/v1",
        api_key="your-api-key",
        model="nomic-embed-text",
    )
    vector_store = InMemoryVectorStore.from_documents(
        documents=all_splits, embedding=embeddings
    )

    print(f"Successfully indexed {len(all_splits)} chunks from {len(docs)} PDF pages.")
    return vector_store


# Example usage:
vector_store = index_pdf_directory("./media")