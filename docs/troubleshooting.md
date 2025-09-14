# Troubleshooting Guide

## Prometheus
- If Prometheus fails to start check pod logs:
  ```bash
  kubectl -n monitoring logs sts/prometheus -c prometheus
  ```
- PVC issues: Ensure StorageClass available and binding succeeded:
  ```bash
  kubectl -n monitoring get pvc
  ```

## Grafana
- Default admin credentials are set via environment variables in the deployment (change immediately):
  - user: admin
  - password: ChangeMe123
- To change password, use grafana UI or create a Kubernetes secret and mount it as env.

## CrashLoopBackOff script
- If script can't access kubectl ensure that kubeconfig is present and kubectl works locally.
- For permission issues running in-cluster, create a ServiceAccount with proper Role/ClusterRole bindings.
