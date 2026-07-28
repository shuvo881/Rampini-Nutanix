from src.rag.indexing import index_pdf_directory

if __name__ == "__main__":
    print("Indexing PDF files in the 'media' directory...")
    vector_store = index_pdf_directory("./media")
    print("Indexing completed.")