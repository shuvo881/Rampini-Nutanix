from fastapi import APIRouter

from src.api.schemas import QuestionRequest
from src.rag.generator import answer_question

router = APIRouter()


@router.get("/")
def health():
    return {
        "status": "running",
        "service": "RAG API",
    }


@router.post("/generate")
def generate(request: QuestionRequest):

    answer = answer_question(request.question)

    return {
        "question": request.question,
        "answer": answer,
    }