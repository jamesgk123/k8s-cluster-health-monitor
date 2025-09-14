#!/bin/bash
NAMESPACE=${1:-default}
echo "Collecting events for namespace: $NAMESPACE"
kubectl get events -n $NAMESPACE --sort-by=.metadata.creationTimestamp
