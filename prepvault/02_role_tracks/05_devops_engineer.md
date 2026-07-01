---
type: role
tags: [role/devops, track]
created: 2024-06-10
---

# DevOps / Site Reliability Engineer (SRE) Interview Track

## 1. Role Overview
DevOps and SRE roles are about building the platforms that allow developers to ship code quickly and safely. While "DevOps" often refers to the culture and toolset for automation, "SRE" (a term coined by Google) is a specific implementation of DevOps that applies software engineering mindsets to system operations.

### The Interview Philosophy
DevOps interviews aren't just about knowing tools (like Docker or Terraform); they are about:
-   **Reliability:** Can you build systems that don't break?
-   **Automation:** If you have to do it twice, can you script it?
-   **Scalability:** How do you manage 10,000 servers as easily as one?
-   **Crisis Management:** How do you react when the site is down and every second costs money?

### Typical Interview Stages
1.  **Linux & Networking Deep Dive (60 min):** Testing your knowledge of the "under-the-hood" OS and network layers.
2.  **Coding for Automation:** Writing scripts (Python/Go/Bash) to solve operational tasks (e.g., "Parse this log file and find unique error codes").
3.  **System Design (Infrastructure focus):** Designing a "Highly Available" architecture on the cloud (AWS/GCP/Azure).
4.  **Hands-on Troubleshooting:** A "Live Debugging" session where you are given a broken system and must find the root cause.
5.  **Behavioral Round:** Focus on "Post-mortems," collaboration with developers, and handling on-call stress.

---

## 2. Foundational Prerequisites
A DevOps engineer must be a master of the environment:

-   **[[01_foundations/04_operating_systems|Operating Systems]]:** Deep knowledge of Linux (Kernel, Namespaces, Cgroups, File Systems, LVM).
-   **[[01_foundations/05_networking|Networking]]:** DNS, BGP, Load Balancing (L4 vs L7), Firewalls (IPTables/NFTables), and VPCs.
-   **[[01_foundations/02_sdlc|SDLC]]:** Version control (Git branching), CI/CD theory, and Automated Testing.
-   **[[01_foundations/03_system_design|System Design]]:** Focus on availability, disaster recovery, and global scalability.

---

## 3. 2026-27 Ecosystem Focus: Platform Engineering
Classic DevOps is transitioning into **Platform Engineering**.
- **Self-Service Platforms**: Building internal platforms so developers can self-provision without raw cloud access.
- **GitOps**: Declarative continuous delivery with tools like ArgoCD.
- **Observability**: Beyond logs—focus on tracing and automated incident response (Grafana/Prometheus).

## 4. 12-Week Learning Pathway
- **Week 1-3: Systems, Scripting & Containers**: Master Linux CLI, Bash/Python automation, and Docker.
- **Week 4-7: IaC & CI/CD Systems**: Terraform infrastructure and GitHub Actions pipelines.
- **Week 8-12: Kubernetes & Monitoring**: Deploying to K8s, ArgoCD, and Grafana dashboards.

## 5. Core Competencies

### A. Infrastructure as Code (IaC)
"Treating your infrastructure like your application code."
-   **Terraform:** Declarative infrastructure. Know state management (Local vs. Remote), Providers, Modules, and Lifecycle rules.
-   **Ansible:** Imperative/Procedural configuration management. Good for "day-two" operations and server hardening.
-   **Pulumi / Cloud Development Kit (CDK):** Using real programming languages (Python, TS, Go) to define infrastructure.
-   **Immutable Infrastructure:** The idea that you never "patch" a running server; you replace it with a new one (AMI/Container).

### B. Containerization & Orchestration
-   **Docker:** How containers work (Namespaces for isolation, Cgroups for resource limiting). Writing efficient, multi-stage Dockerfiles. Image security (Scanning).
-   **Kubernetes (K8s):** 
    -   **Control Plane:** API Server, Etcd, Scheduler, Controller Manager.
    -   **Data Plane:** Kubelet, Kube-proxy, Container Runtime.
    -   **Objects:** Pods, Services, Deployments, ConfigMaps, Secrets, Ingress, CRDs.
    -   **Helm:** Package management for K8s.

### C. CI/CD (Continuous Integration / Continuous Deployment)
-   **Pipelines:** Automating the Build -> Test -> Deploy flow.
-   **Deployment Strategies:** 
    -   **Blue/Green:** Two identical environments. Switch traffic once Green is ready.
    -   **Canary:** Roll out to 5% of users. Monitor metrics. If stable, roll out to 100%.
    -   **Rolling Update:** Update instances one-by-one.
    -   **A/B Testing:** Routing traffic based on user attributes to test features.
-   **Tools:** Jenkins, GitLab CI, GitHub Actions, ArgoCD (GitOps), Spinnaker.

### D. Observability & Monitoring
"You can't fix what you can't see."
-   **The Three Pillars:** Metrics (Numbers), Logs (Strings), and Traces (Context).
-   **Prometheus & Grafana:** The standard for metrics collection and visualization.
-   **ELK Stack (Elasticsearch, Logstash, Kibana):** For centralized logging.
-   **OpenTelemetry:** A vendor-neutral standard for collecting observability data.

---

## 4. Role-Specific Deep Dives

### Deep Dive 1: SRE Principles (The Google Way)
-   **SLIs (Service Level Indicators):** What you measure (e.g., Latency, Error Rate).
-   **SLOs (Service Level Objectives):** The target for that measure (e.g., Latency < 200ms).
-   **SLAs (Service Level Agreements):** The business contract (e.g., "We owe you money if we are down > 0.1%").
-   **Error Budgets:** The allowed amount of unreliability. If the budget is spent, focus shifts from features to stability.
-   **Toil:** Manual, repetitive, automatable work. SREs aim to spend < 50% of their time on toil.

### Deep Dive 2: Kubernetes Networking & Security
**Problem:** How does traffic flow securely in a cluster?
1.  **CNI (Container Network Interface):** Provides the networking layer (Calico, Flannel, VPC-native).
2.  **Network Policies:** Firewalls for Pods. "Only Pod A can talk to Pod B."
3.  **Service Mesh (Istio/Linkerd):** Providing mTLS (encryption), observability, and advanced traffic routing between services.
4.  **RBAC:** Role-Based Access Control. Defining who can do what in the K8s API.

### Deep Dive 3: Disaster Recovery (DR) & Backup
-   **RPO (Recovery Point Objective):** How much data can we afford to lose?
-   **RTO (Recovery Time Objective):** How long can we afford to be down?
-   **Strategies:** 
    -   **Backup & Restore:** (High RTO).
    -   **Pilot Light:** Minimal resources running in a second region. (Lower RTO).
    -   **Warm Standby:** Functional but scaled-down version in a second region.
    -   **Multi-Site Active-Active:** High cost, but zero/minimal downtime failover.

### Deep Dive 4: Cloud-Native Architecture & FinOps
- **Serverless vs. Containers**: When to use AWS Lambda (Event-driven, bursty traffic) vs. EKS/Fargate (Consistent load, complex dependencies). Understanding "Cold Starts" and how to mitigate them in production.
- **FinOps (Cloud Cost Optimization)**: Understanding Reserved Instances, Savings Plans, and Spot Instances. How to build a "cost-aware" infrastructure using tools like Kubecost and AWS Cost Explorer.
- **Edge Computing**: Using CloudFront Functions and Lambda@Edge to run code closer to the user for ultra-low latency. Managing global state and consistency at the edge.

### Deep Dive 5: DevSecOps & The Secure Supply Chain
Security is no longer a separate team; it's a DevOps responsibility.
- **Secrets Management**: Using HashiCorp Vault or AWS Secrets Manager with dynamic credentials and automatic rotation. Implementing "Least Privilege" access via IAM roles.
- **SBOM (Software Bill of Materials)**: Generating and scanning SBOMs to detect vulnerable dependencies (Log4j style). Using tools like Syft and Grype in the CI pipeline.
- **Zero Trust Networking**: Implementing mTLS and identity-based access instead of relying on IP allowlists. Using Service Meshes like Istio for transparent encryption.
- **Policy as Code**: Using OPA (Open Policy Agent) or Kyverno to enforce security and compliance rules in Kubernetes clusters (e.g., "no privileged containers").

### Deep Dive 6: Site Reliability Engineering (SRE) Advanced
- **Error Budgets**: Tactical use of error budgets to prioritize stability over features. If the budget is exhausted, new feature releases are halted until stability is restored.
- **Post-mortems**: Writing blameless post-mortems that focus on process failure rather than human error. Cultivating a "psychologically safe" engineering culture.
- **Chaos Engineering**: Using tools like LitmusChaos or AWS Fault Injection Simulator to proactively test system resilience. "Breaking things on purpose" to find hidden weaknesses.

---

## 5. Platform Engineering & Internal Developer Portals (IDP)
The shift from "DevOps as a team" to "DevOps as a platform."
- **Backstage (Spotify)**: Building a centralized portal for service discovery, documentation, and scaffolding new projects.
- **Golden Paths**: Creating standard, "paved" routes for developers to deploy common services (e.g., a "Spring Boot on K8s" template).
- **Infrastructure Self-Service**: Allowing developers to provision DBs, queues, or S3 buckets via a UI or simple YAML without needing deep Terraform expertise.
- **Developer Experience (DX)**: Measuring and improving the time it takes for a developer to go from "code complete" to "running in production."

---

## 6. Common Interview Questions & Detailed Walkthroughs

### Troubleshooting Scenario: "A Linux server is slow."
**Steps to diagnose:**
1.  **Check CPU:** `top` or `htop`. Look for high `wa` (Wait) — indicates I/O issues. Look for high `si` (Soft IRQ) — indicates network issues.
2.  **Check Memory:** `free -m`. Is the system swapping? (Swap kills performance).
3.  **Check Disk:** `df -h` and `iostat`. Is the disk full? Is the I/O throughput saturated?
4.  **Check Network:** `mtr` or `ping`. Is there packet loss?
5.  **Check Logs:** `/var/log/syslog` or `journalctl -u my-service`.
6.  **Check Open Files/Ports:** `lsof` and `netstat -tunlp`.

### Coding for DevOps: "Log Parser"
**Problem:** Write a Python script to find the top 5 IPs that are causing 5xx errors in an Nginx access log.
**Strategy:**
-   Read the file line by line (don't load it all in memory).
-   Use a regex or string splitting to extract the IP and the Status Code.
-   Use a `Counter` or dictionary to store counts for each IP where code starts with '5'.
-   Print the top 5.

### System Design: "Highly Available Web App"
-   **Global:** Route53 (Geo-DNS) -> CloudFront (CDN).
-   **Regional:** ALB (Load Balancer) -> Auto Scaling Group (EC2) or EKS (K8s).
-   **Database:** Multi-AZ RDS with Read Replicas.
-   **Storage:** S3 with Cross-Region Replication.

---

## 9. Top 10 Essential DevOps/SRE Concepts
1. **Infrastructure as Code (IaC):** Managing infrastructure through declarative files rather than manual configuration.
2. **CI/CD Pipelines:** The automated process of building, testing, and deploying code.
3. **Containerization (Docker):** Isolating applications and their dependencies into portable units.
4. **Orchestration (Kubernetes):** Automating the deployment, scaling, and management of containerized applications.
5. **Observability (The 3 Pillars):** Metrics, Logs, and Traces to understand system health.
6. **Immutable Infrastructure:** Deploying new versions of infrastructure instead of modifying existing ones.
7. **Service Level Objectives (SLOs):** Measurable targets for service reliability.
8. **Error Budgets:** Managing the tradeoff between innovation (new features) and reliability.
9. **Zero Trust Security:** Moving beyond the "castle-and-moat" model to per-request authentication.
10. **The SDLC:** Understanding how code moves from a developer's machine to a production server.

---

## 10. Success Patterns for DevOps Interviews
- **Think in Automation:** Whenever asked how to do something, start with "I would automate this by..."
- **Prioritize Reliability:** Always mention how your solution handles failures (e.g., "I'd use a Multi-AZ deployment for redundancy").
- **Know Your Fundamentals:** Tools change, but Linux and Networking stay the same. Focus on the *why*, not just the *how*.
- **Be a Good "Incident Manager":** In troubleshooting rounds, communicate clearly, stay calm, and document your steps.
- **Focus on the Developer Experience:** A good DevOps engineer builds tools that developers *want* to use.

---

## 11. Recommended Reading List
- *Site Reliability Engineering* (The Google SRE Book) by Betsy Beyer, et al.
- *The Phoenix Project* by Gene Kim, Kevin Behr, and George Spafford.
- *The DevOps Handbook* by Gene Kim, et al.
- *Continuous Delivery* by Jez Humble and David Farley.
- *Terraform: Up & Running* by Yevgeniy Brikman.

---

## 12. DevOps Glossary & Security Terms
-   **mTLS (Mutual TLS):** Both client and server verify each other's certificates.
-   **Shift Left:** Incorporating security/testing earlier in the development process.
-   **Secret Management:** Using HashiCorp Vault or AWS Secrets Manager instead of environment variables.
-   **SAST/DAST:** Static/Dynamic Application Security Testing.
-   **Container Breakout:** An attack where a process inside a container gains access to the host machine.

---

## 7. Company-Specific Patterns

### Google
-   **Focus:** SRE principles and deep Linux coding. Be ready for "Wheels down" questions about the Linux kernel.
-   **Tip:** Read the Google SRE Book and understand the concept of "Software engineering for operations."

### Amazon (AWS)
-   **Focus:** AWS services and "Ownership." You are expected to be an expert in VPCs, IAM, and CloudFormation.
-   **Tip:** Master the "Shared Responsibility" model.

### Netflix
-   **Focus:** "Chaos Engineering." How do you build a system that can survive a whole region failing?
-   **Tip:** Understand how "Chaos Monkey" works.

---

## 8. Detailed Roadmap: How to Prepare
1.  **Phase 1 (Weeks 1-2):** Linux Internals (Filesystems, Processes, Networking). Master Bash and Python.
2.  **Phase 2 (Weeks 3-5):** Cloud (AWS/GCP) and IaC (Terraform). Get a certification (e.g., AWS SAA).
3.  **Phase 3 (Weeks 6-8):** Docker and Kubernetes. Learn K8s objects and how to troubleshoot them.
4.  **Phase 4 (Weeks 9-10):** CI/CD and Observability. Set up a full pipeline with Prometheus and ArgoCD.
5.  **Phase 5 (Mocks):** Practice troubleshooting broken systems and designing for 99.99% uptime.

## Related Topics
-   [[01_foundations/04_operating_systems|Linux and OS Internals]]
-   [[01_foundations/05_networking|Advanced Networking for DevOps]]
-   [[03_interview_formats/03_behavioral_rounds|Handling Incidents and Post-mortems]]
