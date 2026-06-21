---
type: concept
tags: [stack, devops, kubernetes, k8s, orchestration, cloud]
created: 2026-06-10
---

# DevOps Stack: Kubernetes (K8s) Deep Dive

Kubernetes is the industry-standard container orchestration platform. It automates the deployment, scaling, and management of containerized applications.

---

## 1. Kubernetes Architecture (Control Plane vs. Nodes)
- **Control Plane**: Manages the cluster.
    - **API Server**: The entry point for all REST commands.
    - **Etcd**: A distributed key-value store for cluster state.
    - **Scheduler**: Decides which node a pod should run on.
    - **Controller Manager**: Maintains cluster state (e.g., ensuring the right number of pods are running).
- **Worker Nodes**: Run the actual applications.
    - **Kubelet**: An agent that ensures containers are running in a pod.
    - **Kube-proxy**: Handles network communication.
    - **Container Runtime**: (e.g., Docker, containerd).

---

## 2. Core Objects
- **Pod**: The smallest deployable unit. Can contain one or more containers.
- **Service**: An abstract way to expose an application running on a set of Pods as a network service. (ClusterIP, NodePort, LoadBalancer).
- **Deployment**: Provides declarative updates for Pods and ReplicaSets. Handles rolling updates and rollbacks.
- **ReplicaSet**: Ensures that a specified number of pod replicas are running at any given time.
- **Namespace**: A virtual cluster within a physical cluster.

---

## 3. Configuration & Secrets
- **ConfigMap**: Used to store non-confidential data in key-value pairs.
- **Secret**: Used to store sensitive data like passwords, tokens, or keys (encoded in Base64).

---

## 4. Workload Types
- **StatefulSet**: For stateful applications (e.g., databases) that require stable network IDs and persistent storage.
- **DaemonSet**: Ensures that all (or some) Nodes run a copy of a Pod (e.g., for logging or monitoring agents).
- **Job / CronJob**: For short-lived or scheduled tasks.

---

## 5. Key Concepts in Interviews
- **Self-healing**: K8s restarts containers that fail, replaces pods, and kills pods that don't respond to user-defined health checks.
- **Horizontal Pod Autoscaling (HPA)**: Automatically scales the number of pods in a deployment based on CPU utilization or other metrics.
- **Ingress**: Manages external access to the services in a cluster, typically HTTP. Provides load balancing, SSL termination, and name-based virtual hosting.

## Common Interview Questions
- **"What is a 'Sidecar' container?"**: A container that runs in the same pod as the main application container to extend its functionality (e.g., a logging agent).
- **"Explain the Pod Lifecycle."**: Pending -> Running -> Succeeded/Failed -> Unknown.
- **"How does K8s handle rolling updates?"**: It creates new pods with the new version and gradually terminates the old ones, ensuring zero downtime.

## Related Topics
- [[01_Foundations/03_System_Design|System Design (Load Balancing)]]
- [[08_Stack_Deep_Dives/04_DevOps_Cloud_Stack/01_Docker_Containerization|Docker]]
