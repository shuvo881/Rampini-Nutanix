import os
from dotenv import load_dotenv

load_dotenv()

# NAI
NAI_ENDPOINT = os.getenv("NAI_ENDPOINT")
NAI_API_KEY = os.getenv("NAI_API_KEY")
EMBED_MODEL = os.getenv("EMBED_MODEL")
CHAT_MODEL = os.getenv("CHAT_MODEL")

# Milvus
MILVUS_URI = os.getenv("MILVUS_URI")
MILVUS_DATABASE = os.getenv("MILVUS_DATABASE")
MILVUS_COLLECTION = os.getenv("MILVUS_COLLECTION")