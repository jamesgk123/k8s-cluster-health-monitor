# Kubernetes Cluster Health Monitor (Production-ready Monitoring Stack)

This repository provides scripts, docs and **production-ready** Kubernetes manifests to deploy a monitoring stack (Prometheus + Grafana) with PVCs, ConfigMaps, RBAC, Services, and a CrashLoopBackOff auto-restart script.

---
## Features
- Production-ready Prometheus StatefulSet with PVC and ConfigMap (prometheus.yml).
- Grafana Deployment with PVC, ConfigMap for provisioning datasources and dashboards.
- Namespace and RBAC (ServiceAccounts, ClusterRole/Binding) for secure access.
- Scripts to check cluster health and auto-restart CrashLoopBackOff pods.
- Sample application YAML for testing.
- Documentation and usage guide.

---
## Repo layout
```
k8s-cluster-health-monitor-prod/
├── README.md
├── scripts/
│   ├── check_cluster_health.sh
│   ├── restart_crashloop_pods.py
│   └── collect_events.sh
├── manifests/
│   ├── 00-namespace-monitoring.yaml
│   ├── 10-prometheus-configmap.yaml
│   ├── 11-prometheus-statefulset.yaml
│   ├── 12-prometheus-service.yaml
│   ├── 20-grafana-deployment.yaml
│   ├── 21-grafana-service.yaml
│   └── sample-app-crashloop.yaml
└── docs/
    └── troubleshooting.md
```

---
## Quickstart (example)
1. Apply manifests (requires StorageClass available in cluster):
```bash
kubectl apply -f manifests/00-namespace-monitoring.yaml
kubectl apply -f manifests/10-prometheus-configmap.yaml
kubectl apply -f manifests/11-prometheus-statefulset.yaml
kubectl apply -f manifests/12-prometheus-service.yaml
kubectl apply -f manifests/20-grafana-deployment.yaml
kubectl apply -f manifests/21-grafana-service.yaml
```

2. Port-forward to access dashboards locally:
```bash
kubectl port-forward -n monitoring svc/prometheus 9090:9090 &
kubectl port-forward -n monitoring svc/grafana 3000:3000 &
```

3. Grafana default admin password comes from the grafana deploy manifest (see manifests/20-grafana-deployment.yaml). Change it after first login.

---
## Scripts
- `scripts/check_cluster_health.sh` - prints nodes, pods, deployments and events.
- `scripts/restart_crashloop_pods.py` - restarts pods in CrashLoopBackOff for a namespace.
- `scripts/collect_events.sh` - collects events sorted by timestamp.

---
## Notes
- These manifests assume a dynamic StorageClass is available in your cluster (AKS/GKE/EKS). Adjust PVC storage class if needed.
- For production at scale, use Prometheus Operator (kube-prometheus-stack / prometheus-operator) and Helm charts. This repo provides a self-contained example suitable for demos and smaller production clusters.

---
## Author
James George — Senior Kubernetes Admin (AKS, Mirantis Cloud)
