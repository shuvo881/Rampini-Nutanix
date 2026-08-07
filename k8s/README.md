# Kubernetes Deployment — Rampini-Nutanix

This directory contains the Kubernetes manifests required to deploy the **Rampini-Nutanix RAG application** on a Kubernetes/Nutanix Kubernetes Platform (NKP) cluster.

The application consists of:

* **Backend** — API/backend service
* **Frontend** — Next.js web application
* **ConfigMaps** — Runtime configuration
* **Secrets** — Sensitive configuration and API credentials
* **Services** — Internal Kubernetes networking
* **Ingress** — External access to the application

---

## 1. Kubernetes Namespace

The application is deployed in the following namespace:

```text
rampini-rag
```

All Kubernetes commands should use:

```bash
-n rampini-rag
```

If you are using the NKP kubeconfig:

```bash
--kubeconfig nkp.conf
```

Example:

```bash
kubectl --kubeconfig nkp.conf get pods -n rampini-rag
```

---

# 2. Directory Structure

```text
k8s/
├── namespace.yaml
├── ingress.yaml
│
├── backend/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── secret.yaml
│   └── configmap.yaml
│
└── frontend/
    ├── deployment.yaml
    ├── service.yaml
    └── configmap.yaml
```

### Namespace

`namespace.yaml`

Creates the Kubernetes namespace:

```text
rampini-rag
```

### Ingress

`ingress.yaml`

Routes external HTTP/HTTPS traffic to the frontend and backend services.

### Backend

```text
backend/
├── deployment.yaml
├── service.yaml
├── secret.yaml
└── configmap.yaml
```

* `deployment.yaml` — Backend Deployment
* `service.yaml` — Backend ClusterIP Service
* `secret.yaml` — Sensitive environment variables/API credentials
* `configmap.yaml` — Backend runtime configuration

### Frontend

```text
frontend/
├── deployment.yaml
├── service.yaml
└── configmap.yaml
```

* `deployment.yaml` — Next.js frontend Deployment
* `service.yaml` — Frontend ClusterIP Service
* `configmap.yaml` — Frontend runtime configuration

---

# 3. Prerequisites

Make sure the following are available:

* Kubernetes cluster
* `kubectl`
* NKP kubeconfig file (`nkp.conf`)
* Docker
* Access to the container registry
* Frontend and backend Docker images pushed to the registry

Check Kubernetes connectivity:

```powershell
kubectl --kubeconfig nkp.conf cluster-info
```

Check cluster nodes:

```powershell
kubectl --kubeconfig nkp.conf get nodes -o wide
```

---

# 4. Deploy the Application

## Step 1 — Create Namespace

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/namespace.yaml
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get namespace rampini-rag
```

---

## Step 2 — Deploy Backend Secret

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/backend/secret.yaml
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get secret -n rampini-rag
```

---

## Step 3 — Deploy Backend ConfigMap

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/backend/configmap.yaml
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get configmap -n rampini-rag
```

---

## Step 4 — Deploy Backend

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/backend/deployment.yaml
```

Check Deployment:

```powershell
kubectl --kubeconfig nkp.conf get deployment backend -n rampini-rag
```

Check Pods:

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag
```

---

## Step 5 — Create Backend Service

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/backend/service.yaml
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get svc -n rampini-rag
```

---

## Step 6 — Deploy Frontend ConfigMap

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/frontend/configmap.yaml
```

---

## Step 7 — Deploy Frontend

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/frontend/deployment.yaml
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get deployment frontend -n rampini-rag
```

---

## Step 8 — Create Frontend Service

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/frontend/service.yaml
```

---

## Step 9 — Deploy Ingress

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/ingress.yaml
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get ingress -n rampini-rag
```

---

# 5. Recommended Deployment Order

The complete deployment sequence is:

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/namespace.yaml

kubectl --kubeconfig nkp.conf apply -f k8s/backend/secret.yaml
kubectl --kubeconfig nkp.conf apply -f k8s/backend/configmap.yaml
kubectl --kubeconfig nkp.conf apply -f k8s/backend/deployment.yaml
kubectl --kubeconfig nkp.conf apply -f k8s/backend/service.yaml

kubectl --kubeconfig nkp.conf apply -f k8s/frontend/configmap.yaml
kubectl --kubeconfig nkp.conf apply -f k8s/frontend/deployment.yaml
kubectl --kubeconfig nkp.conf apply -f k8s/frontend/service.yaml

kubectl --kubeconfig nkp.conf apply -f k8s/ingress.yaml
```

---

# 6. Verify Deployment

Check all resources:

```powershell
kubectl --kubeconfig nkp.conf get all -n rampini-rag
```

Check Pods:

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag -o wide
```

Expected:

```text
NAME                         READY   STATUS    RESTARTS   AGE
backend-xxxxxxxxxx-xxxxx     1/1     Running   0          ...
frontend-xxxxxxxxxx-xxxxx    1/1     Running   0          ...
```

Check Deployments:

```powershell
kubectl --kubeconfig nkp.conf get deployments -n rampini-rag
```

Check Services:

```powershell
kubectl --kubeconfig nkp.conf get svc -n rampini-rag
```

Check Ingress:

```powershell
kubectl --kubeconfig nkp.conf get ingress -n rampini-rag
```

---

# 7. Check Backend

Get backend Pod:

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag -l app=backend
```

Check backend logs:

```powershell
kubectl --kubeconfig nkp.conf logs -f deployment/backend -n rampini-rag
```

Check the last 100 lines:

```powershell
kubectl --kubeconfig nkp.conf logs --tail=100 deployment/backend -n rampini-rag
```

Describe backend Deployment:

```powershell
kubectl --kubeconfig nkp.conf describe deployment backend -n rampini-rag
```

---

# 8. Check Frontend

Get frontend Pod:

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag -l app=frontend
```

Check frontend logs:

```powershell
kubectl --kubeconfig nkp.conf logs -f deployment/frontend -n rampini-rag
```

Describe frontend Deployment:

```powershell
kubectl --kubeconfig nkp.conf describe deployment frontend -n rampini-rag
```

---

# 9. Check Docker Images

## Backend Image

Check the image configured in the Deployment:

```powershell
kubectl --kubeconfig nkp.conf get deployment backend -n rampini-rag -o jsonpath="{.spec.template.spec.containers[0].image}"
```

## Frontend Image

```powershell
kubectl --kubeconfig nkp.conf get deployment frontend -n rampini-rag -o jsonpath="{.spec.template.spec.containers[0].image}"
```

Check the image actually used by the running Pod:

```powershell
kubectl --kubeconfig nkp.conf get pod -n rampini-rag -l app=backend -o jsonpath="{.items[0].spec.containers[0].image}"
```

```powershell
kubectl --kubeconfig nkp.conf get pod -n rampini-rag -l app=frontend -o jsonpath="{.items[0].spec.containers[0].image}"
```

For the exact pulled image digest:

```powershell
kubectl --kubeconfig nkp.conf describe pod -n rampini-rag -l app=backend
```

Look for:

```text
Image:
Image ID:
```

---

# 10. Updating the Backend Image

Build a new backend image using a new version tag:

```powershell
docker build -t mdgolammostofa705/rampini-backend:v3 ./backend
```

Push it:

```powershell
docker push mdgolammostofa705/rampini-backend:v3
```

Update `k8s/backend/deployment.yaml`:

```yaml
image: mdgolammostofa705/rampini-backend:v3
```

Apply:

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/backend/deployment.yaml
```

Check rollout:

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/backend -n rampini-rag
```

---

# 11. Updating the Frontend Image

Build:

```powershell
docker build -t mdgolammostofa705/rampini-frontend:v3 ./frontend
```

Push:

```powershell
docker push mdgolammostofa705/rampini-frontend:v3
```

Update:

```yaml
image: mdgolammostofa705/rampini-frontend:v3
```

Apply:

```powershell
kubectl --kubeconfig nkp.conf apply -f k8s/frontend/deployment.yaml
```

Check rollout:

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/frontend -n rampini-rag
```

---

# 12. Restart Deployments

Restart backend:

```powershell
kubectl --kubeconfig nkp.conf rollout restart deployment/backend -n rampini-rag
```

Restart frontend:

```powershell
kubectl --kubeconfig nkp.conf rollout restart deployment/frontend -n rampini-rag
```

Watch rollout:

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/backend -n rampini-rag
```

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/frontend -n rampini-rag
```

---

# 13. Temporarily Stop the Application

To stop the application without deleting the Kubernetes resources:

```powershell
kubectl --kubeconfig nkp.conf scale deployment/backend --replicas=0 -n rampini-rag

kubectl --kubeconfig nkp.conf scale deployment/frontend --replicas=0 -n rampini-rag
```

Verify:

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag
```

---

# 14. Start the Application Again

Scale backend:

```powershell
kubectl --kubeconfig nkp.conf scale deployment/backend --replicas=1 -n rampini-rag
```

Scale frontend:

```powershell
kubectl --kubeconfig nkp.conf scale deployment/frontend --replicas=1 -n rampini-rag
```

Check rollout:

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/backend -n rampini-rag

kubectl --kubeconfig nkp.conf rollout status deployment/frontend -n rampini-rag
```

---

# 15. Frontend Public Endpoint

The frontend is exposed through the Kubernetes Ingress.

Get the endpoint:

```powershell
kubectl --kubeconfig nkp.conf get ingress -n rampini-rag
```

Get only the hostname:

```powershell
kubectl --kubeconfig nkp.conf get ingress rampini-ingress `
  -n rampini-rag `
  -o jsonpath="{.spec.rules[0].host}"
```

The public URL follows:

```text
https://<ingress-host>
```

---

# 16. Kubernetes Services

Check all Services:

```powershell
kubectl --kubeconfig nkp.conf get svc -n rampini-rag
```

Expected services include:

```text
backend-service
frontend-service
```

The frontend can communicate with the backend using the Kubernetes Service DNS name:

```text
http://backend-service:8000
```

or:

```text
http://backend-service.rampini-rag.svc.cluster.local:8000
```

---

# 17. Local Port Forwarding

For local frontend testing:

```powershell
kubectl --kubeconfig nkp.conf port-forward `
  deployment/frontend `
  3000:3000 `
  -n rampini-rag
```

Then open:

```text
http://localhost:3000
```

For local backend testing:

```powershell
kubectl --kubeconfig nkp.conf port-forward `
  deployment/backend `
  8000:8000 `
  -n rampini-rag
```

Then:

```text
http://localhost:8000
```

---

# 18. Troubleshooting

## Check Pod Status

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag
```

## Describe a Pod

```powershell
kubectl --kubeconfig nkp.conf describe pod <pod-name> -n rampini-rag
```

## Check Events

```powershell
kubectl --kubeconfig nkp.conf get events `
  -n rampini-rag `
  --sort-by=.metadata.creationTimestamp
```

## Check Deployment

```powershell
kubectl --kubeconfig nkp.conf describe deployment backend -n rampini-rag
```

```powershell
kubectl --kubeconfig nkp.conf describe deployment frontend -n rampini-rag
```

## Check ReplicaSets

```powershell
kubectl --kubeconfig nkp.conf get rs -n rampini-rag
```

## Check Service Endpoints

```powershell
kubectl --kubeconfig nkp.conf get endpoints -n rampini-rag
```

---

# 19. Rollback

View rollout history:

```powershell
kubectl --kubeconfig nkp.conf rollout history deployment/backend -n rampini-rag
```

```powershell
kubectl --kubeconfig nkp.conf rollout history deployment/frontend -n rampini-rag
```

Rollback backend:

```powershell
kubectl --kubeconfig nkp.conf rollout undo deployment/backend -n rampini-rag
```

Rollback frontend:

```powershell
kubectl --kubeconfig nkp.conf rollout undo deployment/frontend -n rampini-rag
```

Check status:

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/backend -n rampini-rag

kubectl --kubeconfig nkp.conf rollout status deployment/frontend -n rampini-rag
```

---

# 20. Delete the Application

To remove all resources defined by the manifests:

```powershell
kubectl --kubeconfig nkp.conf delete -R -f k8s/
```

> **Warning:** This deletes the Kubernetes resources defined under `k8s/`. Use this carefully in a shared or production environment.

---

# 21. Recommended Production Image Strategy

Use a **unique image tag for every deployment** instead of repeatedly pushing the same tag such as `latest` or `v2`.

Recommended:

```text
rampini-backend:v1
rampini-backend:v2
rampini-backend:v3

rampini-frontend:v1
rampini-frontend:v2
rampini-frontend:v3
```

Even better, use a Git commit SHA:

```text
rampini-backend:8f31a2c
rampini-frontend:8f31a2c
```

This makes it easy to identify exactly which version is running in Kubernetes.

---

# 22. Quick Health Check

Run the following commands to quickly check the entire application:

```powershell
kubectl --kubeconfig nkp.conf get pods -n rampini-rag

kubectl --kubeconfig nkp.conf get deployments -n rampini-rag

kubectl --kubeconfig nkp.conf get svc -n rampini-rag

kubectl --kubeconfig nkp.conf get ingress -n rampini-rag
```

Check both deployments:

```powershell
kubectl --kubeconfig nkp.conf rollout status deployment/backend -n rampini-rag

kubectl --kubeconfig nkp.conf rollout status deployment/frontend -n rampini-rag
```

Check logs:

```powershell
kubectl --kubeconfig nkp.conf logs --tail=50 deployment/backend -n rampini-rag

kubectl --kubeconfig nkp.conf logs --tail=50 deployment/frontend -n rampini-rag
```

---

# 23. Useful Commands Cheat Sheet

| Task                  | Command                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Cluster info          | `kubectl --kubeconfig nkp.conf cluster-info`                                                                                   |
| Nodes                 | `kubectl --kubeconfig nkp.conf get nodes -o wide`                                                                              |
| Pods                  | `kubectl --kubeconfig nkp.conf get pods -n rampini-rag`                                                                        |
| Deployments           | `kubectl --kubeconfig nkp.conf get deployments -n rampini-rag`                                                                 |
| Services              | `kubectl --kubeconfig nkp.conf get svc -n rampini-rag`                                                                         |
| Ingress               | `kubectl --kubeconfig nkp.conf get ingress -n rampini-rag`                                                                     |
| Backend logs          | `kubectl --kubeconfig nkp.conf logs -f deployment/backend -n rampini-rag`                                                      |
| Frontend logs         | `kubectl --kubeconfig nkp.conf logs -f deployment/frontend -n rampini-rag`                                                     |
| Restart backend       | `kubectl --kubeconfig nkp.conf rollout restart deployment/backend -n rampini-rag`                                              |
| Restart frontend      | `kubectl --kubeconfig nkp.conf rollout restart deployment/frontend -n rampini-rag`                                             |
| Backend image         | `kubectl --kubeconfig nkp.conf get deployment backend -n rampini-rag -o jsonpath="{.spec.template.spec.containers[0].image}"`  |
| Frontend image        | `kubectl --kubeconfig nkp.conf get deployment frontend -n rampini-rag -o jsonpath="{.spec.template.spec.containers[0].image}"` |
| Rollout status        | `kubectl --kubeconfig nkp.conf rollout status deployment/backend -n rampini-rag`                                               |
| Events                | `kubectl --kubeconfig nkp.conf get events -n rampini-rag --sort-by=.metadata.creationTimestamp`                                |
| Port-forward frontend | `kubectl --kubeconfig nkp.conf port-forward deployment/frontend 3000:3000 -n rampini-rag`                                      |
| Port-forward backend  | `kubectl --kubeconfig nkp.conf port-forward deployment/backend 8000:8000 -n rampini-rag`                                       |

---

# 24. Architecture

The deployed architecture is:

```text
                         Internet
                            │
                            ▼
                    ┌─────────────────┐
                    │ Kubernetes      │
                    │ Ingress (NGINX) │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
             Frontend                    /api
                │                         │
                ▼                         ▼
      ┌──────────────────┐      ┌──────────────────┐
      │ frontend-service │      │ backend-service  │
      │     :3000        │      │      :8000       │
      └────────┬─────────┘      └────────┬─────────┘
               │                         │
               ▼                         ▼
      ┌──────────────────┐      ┌──────────────────┐
      │ Frontend Pod     │      │ Backend Pod      │
      │ Next.js          │      │ FastAPI/API      │
      └──────────────────┘      └──────────────────┘

              Namespace: rampini-rag
```

---

# 25. Deployment Checklist

Before considering a deployment complete, verify:

* [ ] Namespace `rampini-rag` exists
* [ ] Backend Secret is configured
* [ ] Backend ConfigMap is configured
* [ ] Backend Deployment is running
* [ ] Backend Service is available
* [ ] Frontend ConfigMap is configured
* [ ] Frontend Deployment is running
* [ ] Frontend Service is available
* [ ] Ingress is configured
* [ ] Frontend and backend images are correct
* [ ] Backend logs show no startup errors
* [ ] Frontend logs show Next.js is ready
* [ ] Ingress endpoint is accessible
* [ ] Frontend can communicate with backend
* [ ] End-to-end RAG functionality has been tested

---

## Project

**Rampini-Nutanix — RAG Application**

Kubernetes Namespace:

```text
rampini-rag
```

Main Kubernetes components:

```text
Namespace
├── Backend Deployment
├── Backend Service
├── Backend Secret
├── Backend ConfigMap
├── Frontend Deployment
├── Frontend Service
├── Frontend ConfigMap
└── NGINX Ingress
```
