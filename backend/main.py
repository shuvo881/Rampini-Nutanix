from src.rag.indexing import index_documents
from src.rag.generator import answer_question

if __name__ == "__main__":
    print("Indexing PDF files in the 'media' directory...")
    index_documents()
    print("Indexing completed.")
    while True:
        question = input("Question: ")

        if question.lower() in {"exit", "quit"}:
            break

        answer = answer_question(question)
        print("\nAnswer:")
        print(answer)
        print("-" * 80)