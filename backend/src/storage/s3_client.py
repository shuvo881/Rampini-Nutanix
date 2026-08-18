
import os
import boto3
from botocore.client import Config
from dotenv import load_dotenv
import urllib3

urllib3.disable_warnings()  # silence self-signed cert warnings
load_dotenv()  # loads variables from .env into environment

# --- Connection details pulled from .env ---
ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
SECRET_KEY = os.getenv("S3_SECRET_KEY")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version="s3v4"),
    verify=False,
)
