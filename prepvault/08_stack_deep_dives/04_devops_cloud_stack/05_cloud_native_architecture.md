---
type: concept
tags: [stack, devops, cloud-native, microservices, reliability, patterns]
created: 2026-06-10
---

# DevOps Stack: Cloud Native Architecture

Cloud native is an approach to building and running applications that exploits the advantages of the cloud computing delivery model.

---

## 1. The Twelve-Factor App
A methodology for building SaaS applications that are portable, resilient, and scalable. Key factors include:
- **Codebase**: One codebase tracked in version control, many deploys.
- **Dependencies**: Explicitly declare and isolate dependencies.
- **Config**: Store config in the environment.
- **Backing services**: Treat backing services (DBs, caches) as attached resources.
- **Build, release, run**: Strictly separate build and run stages.
- **Processes**: Execute the app as one or more stateless processes.
- **Port binding**: Export services via port binding.
- **Concurrency**: Scale out via the process model.
- **Disposability**: Maximize robustness with fast startup and graceful shutdown.

---

## 2. Microservices Patterns
- **API Gateway**: A single entry point for all clients.
- **Service Mesh (e.g., Istio, Linkerd)**: A dedicated infrastructure layer for handling service-to-service communication, providing features like observability, traffic management, and security.
- **Circuit Breaker**: Prevents a service from trying to execute an operation that is likely to fail, allowing the system to recover from failure.
- **Sidecar Pattern**: Attaching a helper container to a primary container to provide additional functionality (e.g., logging, monitoring).

---

## 3. Serverless Computing
Building and running applications without managing infrastructure.
- **FaaS (Function as a Service)**: e.g., AWS Lambda, Google Cloud Functions.
- **BaaS (Backend as a Service)**: e.g., Firebase, Supabase.
- **Pros**: Pay-per-use, automatic scaling, no server management.
- **Cons**: Cold starts, limited execution time, vendor lock-in.

---

## 4. Observability (Three Pillars)
1. **Metrics**: Numerical data over time (e.g., CPU usage, error rate).
2. **Logging**: Record of events that happened in the application.
3. **Tracing**: Tracking the path of a request through multiple services (Distributed Tracing).

---

## 5. Resilience Engineering
- **Chaos Engineering**: Disciplined experimentation on a distributed system to build confidence in its capability to withstand turbulent conditions.
- **High Availability (HA)**: Designing systems to be operational for long periods with minimal downtime.

## Common Interview Questions
- **"What is the difference between Cloud-Native and Cloud-Agnostic?"**: Cloud-Native uses cloud-specific services to maximize efficiency; Cloud-Agnostic avoids vendor lock-in by using generic tools.
- **"Explain the Circuit Breaker pattern."**: Describe how it monitors for failures and "trips" to prevent further requests, giving the downstream service time to recover.
- **"What are the benefits of a Service Mesh?"**: Centralized control over traffic, security (mTLS), and observability without changing application code.

## Related Topics
- [[01_foundations/03_system_design|System Design (Microservices)]]
- [[08_stack_deep_dives/04_devops_cloud_stack/02_kubernetes|Kubernetes]]
