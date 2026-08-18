import enum
from sqlalchemy import Column, String, DateTime, Integer, Enum as SQLEnum
from sqlalchemy.sql import func
from src.database.session import Base


class FileStatus(str, enum.Enum):
    DOWNLOADED = "downloaded"
    INDEXED = "indexed"
    FAILED = "failed"


class BucketFile(Base):
    __tablename__ = "bucket_files"

    id = Column(Integer, primary_key=True, index=True)
    object_key = Column(String, unique=True, index=True, nullable=False)
    local_path = Column(String, nullable=False)
    status = Column(
        SQLEnum(FileStatus, name="file_status"),
        default=FileStatus.DOWNLOADED,
        nullable=False,
    )
    downloaded_at = Column(DateTime(timezone=True), server_default=func.now())