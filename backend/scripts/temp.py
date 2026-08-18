from backend.src.storage.object_store import upload_file, download_file, download_all_files
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
from pathlib import Path
pdf_path = Path(__file__).parent / "media" / "user05.pdf"
# upload_file(pdf_path, object_key="user06.pdf", bucket_name=BUCKET_NAME)
# upload_file(BUCKET_NAME, "photo.jpg")
# upload_file(BUCKET_NAME, "data.csv")

# download_file(BUCKET_NAME, "report.pdf")
download_file("user05.pdf", "media/photo_copy.pdf", BUCKET_NAME)

# download_all_files(local_dir="media/new", bucket_name=BUCKET_NAME)
