from sqlalchemy.orm import Session
from src.database.models import BucketFile, FileStatus


def is_downloaded(db: Session, object_key: str) -> bool:
    return db.query(BucketFile).filter(BucketFile.object_key == object_key).first() is not None


def mark_downloaded(db: Session, object_key: str, local_path: str) -> BucketFile:
    record = BucketFile(object_key=object_key, local_path=local_path, status=FileStatus.DOWNLOADED)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def update_status(db: Session, object_key: str, status: FileStatus) -> None:
    db.query(BucketFile).filter(BucketFile.object_key == object_key).update({"status": status})
    db.commit()


def list_files(db: Session):
    return db.query(BucketFile).order_by(BucketFile.downloaded_at.desc()).all()