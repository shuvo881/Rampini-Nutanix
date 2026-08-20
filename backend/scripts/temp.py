from src.storage.object_store import upload_file, download_file, download_all_files
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
from pathlib import Path
# pdf_path = Path(r'E:\Codes\Rampini-Nutanix\backend\media\rag_docs\Request for Proposal (RFP) - Vector Database Ingestion Test (1).pdf')
# upload_file(pdf_path, object_key="rfp-vector-database.pdf", bucket_name=BUCKET_NAME)
# upload_file(BUCKET_NAME, "photo.jpg")
# upload_file(BUCKET_NAME, "data.csv")

# download_file(BUCKET_NAME, "report.pdf")
# download_file("rfp-vector-database.pdf", "media/rfp-vector-database.pdf", BUCKET_NAME)

# download_all_files(local_dir="media/new", bucket_name=BUCKET_NAME)
