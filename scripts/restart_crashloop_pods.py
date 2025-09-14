#!/usr/bin/env python3
import subprocess, sys, json

def get_pods(namespace):
    cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "json"]
    out = subprocess.check_output(cmd, text=True)
    return json.loads(out).get('items', [])

def is_crashloop(pod):
    for cs in pod.get('status', {}).get('containerStatuses', []):
        reason = cs.get('state', {}).get('waiting', {}).get('reason') or cs.get('lastState', {}).get('terminated', {}).get('reason')
        if reason and 'CrashLoopBackOff' in reason:
            return True
    return False

def restart_pod(namespace, name):
    print(f"Restarting pod {name} in namespace {namespace}")
    subprocess.run(["kubectl", "delete", "pod", name, "-n", namespace], check=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python restart_crashloop_pods.py <namespace>")
        sys.exit(1)
    ns = sys.argv[1]
    pods = get_pods(ns)
    crash_pods = [p for p in pods if is_crashloop(p)]
    if not crash_pods:
        print("No CrashLoopBackOff pods found.")
    for p in crash_pods:
        restart_pod(ns, p['metadata']['name'])
