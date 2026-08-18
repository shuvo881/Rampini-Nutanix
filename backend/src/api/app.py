from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import api_router
from src.database.session import engine
from src.database.base import Base


from src.storage.watcher import start_watcher, stop_watcher
from src.database.session import SessionLocal
from src.crud.file import update_status
from src.database.models import FileStatus
from src.rag.indexing import index_documents


def handle_new_file(local_path: str, object_key: str):
    db = SessionLocal()
    try:
        # chunks = load_and_split(local_path)
        index_documents(local_path=local_path)
        print(f"Indexed document from {object_key}")
        update_status(db, object_key, FileStatus.INDEXED)
    except Exception as e:
        print(f"Failed to index {object_key}: {e}")
        update_status(db, object_key, FileStatus.FAILED)
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    start_watcher(on_new_file=handle_new_file)
    yield
    stop_watcher()


def create_app():
    app = FastAPI(
        title="RAG API",
        version="1.0.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")

    return app


app = create_app()