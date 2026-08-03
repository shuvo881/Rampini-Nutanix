FROM ghcr.io/astral-sh/uv:0.12.1 AS uv

FROM python:3.13-slim AS builder

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY --from=uv /uv /usr/local/bin/uv

RUN uv export --frozen --no-dev -o requirements.txt && \
    python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.13-slim

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]