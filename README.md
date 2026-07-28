# Rampini Nutanix RAG

This project provides a retrieval-augmented generation (RAG) system using LangChain and Nutanix NAI.

## Setup

1. Create a `.env` file from `.env.example`:

   ```powershell
   copy .env.example .env
   ```

2. Install dependencies in the project virtual environment:

   ```powershell
   e:/Codes/Rampini-Nutanix/.venv/Scripts/python.exe -m pip install -r requirements.txt
   ```

   If you prefer, install directly from `pyproject.toml`.

3. Place source documents under the `docs/` folder.

## Usage

- Ingest documents into the local vector store:

  ```powershell
  e:/Codes/Rampini-Nutanix/.venv/Scripts/python.exe main.py ingest
  ```

- Ask a question using the vector store:

  ```powershell
  e:/Codes/Rampini-Nutanix/.venv/Scripts/python.exe main.py query "What is the status of my Nutanix cluster?"
  ```

- Override the source directory or persistence directory at runtime:

  ```powershell
  e:/Codes/Rampini-Nutanix/.venv/Scripts/python.exe main.py ingest --source-dir docs --persist-dir app/.vector_store
  ```

## Notes

- The system uses the `NAI_ENDPOINT`, `NAI_API_KEY`, `MODEL`, and `EMBED_MODEL` values from `.env`.
- `docs/` is the default content source directory.
- The local vector store is persisted under `app/.vector_store` by default.
