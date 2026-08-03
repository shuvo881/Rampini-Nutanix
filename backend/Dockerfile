# Backend Dockerfile
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY pyproject.toml ./
RUN pip install --no-cache-dir \
    fastapi>=0.140.13 \
    python-dotenv>=1.0.0 \
    chromadb>=0.3.25 \
    langchain>=1.3.14 \
    langgraph>=1.2.9 \
    langchain-openai>=1.4.1 \
    langchain-text-splitters>=1.1.2 \
    langchain-community>=0.4.2 \
    pypdf>=6.14.2 \
    pymilvus>=3.0.0 \
    uvicorn>=0.51.0 \
    python-multipart>=0.0.32

COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
