from src.rag.indexing import main

if __name__ == "__main__":
    print("Indexing PDF files in the 'media' directory...")
    vector_store = main()
    print("Indexing completed.")