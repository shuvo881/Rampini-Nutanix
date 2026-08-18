from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.session import get_db
from src.crud.file import list_files
from src.schemas.file import BucketFileOut

router = APIRouter()


@router.get("/", response_model=list[BucketFileOut])
def get_bucket_files(db: Session = Depends(get_db)):
    """List all files downloaded from the bucket, with their indexing status."""
    return list_files(db)