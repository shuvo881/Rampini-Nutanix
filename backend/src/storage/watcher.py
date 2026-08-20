import os
import time
import threading
from src.storage.object_store import list_bucket_objects, download_file
from src.database.session import SessionLocal
from src.crud.file import is_downloaded, mark_downloaded
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

stop_event = threading.Event()
_thread: threading.Thread | None = None

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
LOCAL_DOWNLOAD_DIR = os.getenv("RAG_DOCS_DIR")
POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", 10))


def _poll_once(on_new_file=None):
    db = SessionLocal()
    try:
        for key in list_bucket_objects(S3_BUCKET_NAME):
            if is_downloaded(db, key):
                continue

            local_path = os.path.join(LOCAL_DOWNLOAD_DIR, key)
            download_file(key, local_path, S3_BUCKET_NAME)
            mark_downloaded(db, key, local_path)
            print(f"New file downloaded: {key}")

            if on_new_file:
                on_new_file(local_path, key)
    finally:
        db.close()


def _loop(on_new_file=None):
    os.makedirs(LOCAL_DOWNLOAD_DIR, exist_ok=True)
    print(f"Watching bucket '{S3_BUCKET_NAME}' every {POLL_INTERVAL_SECONDS}s...")
    while not stop_event.is_set():
        try:
            _poll_once(on_new_file)
        except Exception as e:
            print(f"Error polling bucket: {e}")
        print("Stopping watcher thread.")
        break
        time.sleep(POLL_INTERVAL_SECONDS)


def start_watcher(on_new_file=None):
    global _thread
    stop_event.clear()
    _thread = threading.Thread(target=_loop, args=(on_new_file,), daemon=True)
    _thread.start()


def stop_watcher():
    stop_event.set()