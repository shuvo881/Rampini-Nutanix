# Kubernetes manifests for Rampini-Nutanix

This folder holds Kubernetes manifests used to deploy the Rampini application (backend + frontend).

Overview
 - Namespace and cluster-level resources: `namespace.yaml`, `ingress.yaml`.
 - App-specific manifests are grouped in subfolders: `backend/` and `frontend/`.

Directory layout
 - `namespace.yaml` — Namespace for the Rampini app.
 - `ingress.yaml` — Ingress to route external traffic (host configured in manifests).
 - `backend/` — Backend manifests:
	 - `deployment.yaml` — Backend Deployment.
	 - `service.yaml` — Backend Service (ClusterIP).
	 - `secret.yaml` — Backend Secret (env config, API keys, etc.).
	 - `configmap.yaml` — Backend runtime config / env vars.
 - `frontend/` — Frontend manifests:
	 - `deployment.yaml` — Frontend Deployment.
	 - `service.yaml` — Frontend Service (ClusterIP).
	 - `configmap.yaml` — Frontend runtime config / env vars.

Apply manifests (recommended order)
Use the following commands from the repository root to apply resources in the correct order:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/backend/secret.yaml
kubectl apply -f k8s/backend/deployment.yaml
kubectl apply -f k8s/backend/service.yaml
kubectl apply -f k8s/frontend/configmap.yaml
kubectl apply -f k8s/frontend/deployment.yaml
kubectl apply -f k8s/frontend/service.yaml
kubectl apply -f k8s/ingress.yaml
```

Tip: For quick local testing you can also apply everything recursively, but ordering secrets/configmaps first avoids startup errors:

```bash
kubectl apply -R -f k8s/
```

Rollback / delete

```bash
kubectl delete -R -f k8s/
```

Common variables and notes
 - Hostname: manifests use a host (e.g. `rampini.local`) in `ingress.yaml`. Add it to your hosts file (`C:\\Windows\\System32\\drivers\\etc\\hosts` on Windows) or change the host to your domain.
 - Images: deployments reference container images. By default the project expects local images like `rampini-backend:latest` and `rampini-frontend:latest` — update the image fields to point to your registry if needed.
 - Configs/secrets: Update `k8s/backend/secret.yaml` and `k8s/frontend/configmap.yaml` with any environment-specific values before applying.
 - Inspecting resources:

```bash
kubectl get all -n rampini
kubectl get ingress -n rampini
kubectl describe pod <pod-name> -n rampini
kubectl logs deploy/<deployment-name> -n rampini
```

Ingress TLS
 - The `ingress.yaml` provided is a basic example. For TLS in production, configure a TLS secret and update the ingress to reference it (or use a controller with cert-manager).

Developer notes
 - This repo includes Dockerfiles for `backend/` and `frontend/` — build and push images to your registry or use local cluster helpers (e.g. `kind load docker-image` or `minikube image load`).
 - If you change `next.config.ts` or backend CORS/proxy settings, update the manifests or ingress host accordingly.

Where to look
 - Backend manifests: `k8s/backend/`
 - Frontend manifests: `k8s/frontend/`

If you want, I can also:
 - add a `kustomization.yaml` to simplify `kubectl apply -k k8s/` usage, or
 - add a short script to apply manifests in the recommended order.

---
Updated to provide clearer structure, commands, and troubleshooting tips.
