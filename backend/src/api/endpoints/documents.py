from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException

from src.rag.config import RAG_DOCS_DIR
from src.rag.indexing import index_documents

router = APIRouter()

RAG_DOCS_PATH = Path(RAG_DOCS_DIR)
RAG_DOCS_PATH.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_documents(files: list[UploadFile] = File(...)):

    uploaded_files = []

    for file in files:

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail=f"{file.filename} is not a PDF file.",
            )

        destination = RAG_DOCS_PATH / file.filename

        with destination.open("wb") as f:
            f.write(await file.read())

        uploaded_files.append(file.filename)

    indexed_chunks = index_documents()

    return {
        "success": True,
        "uploaded_files": uploaded_files,
        "indexed_chunks": indexed_chunks,
    }