---
type: concept
tags: [stack, devops, docker, containerization, linux]
created: 2026-06-10
---

# DevOps Stack: Docker & Containerization

Docker revolutionized software delivery by allowing developers to package applications and their dependencies into a single, portable unit.

---

## 1. What is a Container?
A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.

### Container vs. Virtual Machine (VM)
- **VM**: Includes a full copy of an operating system, the application, necessary binaries, and libraries - taking up tens of GBs. Uses a **Hypervisor**.
- **Container**: Shares the host OS kernel and isolates the application process. Much lighter (MBs) and starts almost instantly. Uses **Namespaces** and **Cgroups**.

---

## 2. Docker Architecture
- **Docker Engine**: The client-server application.
- **Dockerfile**: A text document that contains all the commands a user could call on the command line to assemble an image.
- **Image**: A read-only template with instructions for creating a Docker container.
- **Container**: A runnable instance of an image.
- **Registry (e.g., Docker Hub)**: A service that stores and distributes Docker images.

---

## 3. Key Dockerfile Instructions
- `FROM`: Sets the Base Image.
- `RUN`: Executes commands in a new layer (used for installing packages).
- `COPY / ADD`: Copies files from host to container.
- `CMD`: The default command to run when the container starts.
- `ENTRYPOINT`: The main executable for the container.

### Image Layering & Optimization
Docker images are built in layers.
- **Layer Caching**: Docker caches layers to speed up subsequent builds. Order matters! Put things that change frequently (like source code) at the bottom.
- **Multi-stage Builds**: Used to create small production images by using one stage for building (with all tools) and another for running (with only the binary).

---

## 4. Networking and Storage
- **Volumes**: Persistent data storage that exists outside the container lifecycle.
- **Bind Mounts**: Mapping a specific host path to a container path.
- **Bridge Network**: The default network driver for standalone containers.

---

## 5. Security Best Practices
- **Run as non-root user**: Use the `USER` instruction.
- **Use official base images**: Reduces vulnerability risk.
- **Scan images**: Use tools like `docker scout` or Snyk.
- **Multi-stage builds**: To keep build tools out of the final image.

## Common Interview Questions
- **"Explain the difference between CMD and ENTRYPOINT."**: CMD sets default arguments that can be easily overridden; ENTRYPOINT sets the main command that is harder to override.
- **"How do you reduce the size of a Docker image?"**: Use Alpine base images, combine RUN commands to reduce layers, and use multi-stage builds.
- **"What are Namespaces and Cgroups?"**: Namespaces provide isolation (PID, Network, Mount); Cgroups provide resource limiting (CPU, Memory).

## Related Topics
- [[01_foundations/04_operating_systems|OS (Virtualization)]]
- [[08_stack_deep_dives/04_devops_cloud_stack/02_kubernetes|Kubernetes]]
