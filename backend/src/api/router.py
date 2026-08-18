from fastapi import APIRouter

from src.api.endpoints.documents import router as documents_router
from src.api.endpoints.chat import router as chat_router
from src.api.endpoints.bucket_files import router as bucket_files_router

api_router = APIRouter()

api_router.include_router(
    documents_router,
    prefix="/documents",
    tags=["Documents"],
)

api_router.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"],
)

api_router.include_router(
    bucket_files_router,
    prefix="/bucket-files",
    tags=["Bucket Files"],
)