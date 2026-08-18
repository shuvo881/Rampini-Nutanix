from pydantic import BaseModel
from datetime import datetime
from src.database.models import FileStatus

class BucketFileOut(BaseModel):
    object_key: str
    local_path: str
    status: FileStatus
    downloaded_at: datetime

    class Config:
        from_attributes = True  # enables .from_orm() / model_validate() from SQLAlchemy objects