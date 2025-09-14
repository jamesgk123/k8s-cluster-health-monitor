#!/bin/bash
set -euo pipefail
echo "== Nodes =="
kubectl get nodes -o wide
echo
echo "== Pods =="
kubectl get pods --all-namespaces -o wide
echo
echo "== Deployments =="
kubectl get deployments --all-namespaces -o wide
echo
echo "== Events (last 100) =="
kubectl get events --all-namespaces --sort-by=.metadata.creationTimestamp | tail -n 100
