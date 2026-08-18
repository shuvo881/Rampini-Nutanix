import os
from dotenv import load_dotenv
from src.storage.s3_client import s3

load_dotenv()
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


def upload_file(local_file_path, object_key=None, bucket_name=BUCKET_NAME):
    """
    Upload any file to the bucket (defaults to S3_BUCKET_NAME from .env).
    If object_key is not provided, the local filename is used.
    """
    if object_key is None:
        object_key = os.path.basename(local_file_path)

    s3.upload_file(local_file_path, bucket_name, object_key)
    print(f"Uploaded '{local_file_path}' to s3://{bucket_name}/{object_key}")
    return object_key


def download_file(object_key, local_save_path=None, bucket_name=BUCKET_NAME):
    """
    Download any file from the bucket (defaults to S3_BUCKET_NAME from .env).
    If local_save_path is not provided, saves using the object_key as filename.
    """
    if local_save_path is None:
        local_save_path = object_key

    s3.download_file(bucket_name, object_key, local_save_path)
    print(f"Downloaded s3://{bucket_name}/{object_key} to '{local_save_path}'")
    return local_save_path

def download_all_files(local_dir="downloads", bucket_name=BUCKET_NAME):
    """
    Download every object in the bucket into local_dir,
    preserving the folder structure from the object keys.
    """
    paginator = s3.get_paginator("list_objects_v2")
    count = 0

    for page in paginator.paginate(Bucket=bucket_name):
        for obj in page.get("Contents", []):
            key = obj["Key"]

            # Skip "folder" placeholder objects (keys ending in /)
            if key.endswith("/"):
                continue

            local_path = os.path.join(local_dir, key)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            s3.download_file(bucket_name, key, local_path)
            print(f"Downloaded s3://{bucket_name}/{key} -> {local_path}")
            count += 1

    if count == 0:
        print("Bucket is empty — nothing to download.")
    else:
        print(f"Done. Downloaded {count} file(s) to '{local_dir}'.")

    return count

def list_bucket_objects(bucket_name: str = BUCKET_NAME):
    """Yields every object key in the bucket, handling pagination."""
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket_name):
        for obj in page.get("Contents", []):
            if not obj["Key"].endswith("/"):
                yield obj["Key"]