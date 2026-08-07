# Rampini Nutanix RAG

This repository contains a Retrieval-Augmented Generation (RAG) application built with:

- **Backend**: FastAPI service for document ingestion, vector search, and chat generation
- **Frontend**: Next.js 16 application for user chat and document upload
- **Deployment**: Kubernetes manifests for NKP / cluster deployment

## Project Overview

Rampini Nutanix RAG provides a document-aware AI assistant. It loads documents into a vector store, uses embeddings to match user queries with relevant document content, and then generates answers through a language model.

Key features:

- Document upload and ingestion
- Chat-style question answering
- API proxying from frontend to backend
- Kubernetes deployment manifests for frontend and backend

## Repository Structure

```text
.
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── pyproject.toml
│   ├── README.md
│   └── src/
│       ├── api/
│       ├── rag/
│       └── ...
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── README.md
│   ├── .env
│   └── src/
│       └── app/
│       └── components/
├── k8s/
│   ├── ingress.yaml
│   ├── namespace.yaml
│   ├── backend/
│   └── frontend/
├── docker-compose.yml
├── nkp.conf
└── README.md
```

## How it Works

### Backend

- FastAPI app defined in `backend/src/api/app.py`
- API routes include:
  - `POST /api/chat/generate` — generate chat answers
  - `POST /api/documents/upload` — upload or ingest documents
- Backend runs on port `8000`
- Uses a vector database or embedding service to support retrieval-augmented responses

### Frontend

- Next.js app under `frontend/`
- Uses `frontend/next.config.ts` to rewrite `/api/*` requests to the backend URL
- Chat UI in `frontend/src/components/ChatInterface.tsx`
- Document upload UI in `frontend/src/components/DragDropZone.tsx`

### Kubernetes

- Namespace: `rampini-rag`
- Frontend and backend each have a `Deployment` and `Service`
- `k8s/ingress.yaml` routes external traffic to the frontend service
- ConfigMaps and Secrets provide environment configuration

## Local Development

### Backend

1. Create and activate a Python environment.
2. Install dependencies from `backend/pyproject.toml`.
3. Run the backend:

```bash
cd backend
python main.py
```

### Frontend

1. Install frontend dependencies.
2. Set `BACKEND_URL` in `frontend/.env` to your backend host.
3. Run the frontend:

```bash
cd frontend
npm run dev
```

### Notes

- For local development, `BACKEND_URL` should point to `http://localhost:8000` if the backend runs locally.
- The frontend rewrites `/api/*` to the backend path using `next.config.ts`.
- If deploying to Kubernetes, use the cluster service name such as `http://backend-service:8000`.

## Kubernetes Deployment

Apply the manifests in this order:

1. `k8s/namespace.yaml`
2. `k8s/backend/secret.yaml`
3. `k8s/backend/configmap.yaml`
4. `k8s/backend/deployment.yaml`
5. `k8s/backend/service.yaml`
6. `k8s/frontend/configmap.yaml`
7. `k8s/frontend/deployment.yaml`
8. `k8s/frontend/service.yaml`
9. `k8s/ingress.yaml`

Use the NKP kubeconfig if needed:

```bash
kubectl --kubeconfig nkp.conf apply -f k8s/namespace.yaml
kubectl --kubeconfig nkp.conf get pods -n rampini-rag
```

## Troubleshooting

- `ENOTFOUND backend`: frontend is trying to resolve a cluster hostname from outside the cluster.
- `ECONNRESET`: frontend is proxying to a backend address that is unreachable.
- `404 Not Found` on `/chat/generate`: the backend route is actually mounted under `/api/chat/generate`.

## Summary

This repository combines a Next.js frontend with a FastAPI backend to deliver a document-aware chat assistant. It supports both local development and Kubernetes deployment, with a clear path for configuring backend connectivity and environment-specific endpoints.
