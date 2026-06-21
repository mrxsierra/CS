---
type: concept
tags: [stack, devops, terraform, iac, infrastructure, automation]
created: 2026-06-10
---

# DevOps Stack: Terraform & Infrastructure as Code (IaC)

Terraform allows you to build, change, and version infrastructure safely and efficiently using a declarative configuration language.

---

## 1. What is IaC?
Infrastructure as Code is the managing and provisioning of infrastructure through code instead of through manual processes.
- **Declarative**: You define the *desired state* (e.g., "I want 3 servers"), and the tool handles how to get there.
- **Imperative**: You define the *steps* to take (e.g., "Run this command, then that one"). Terraform is Declarative.

---

## 2. Core Concepts of Terraform
- **HCL (HashiCorp Configuration Language)**: The language used to write configuration.
- **Providers**: Plugins that allow Terraform to interact with cloud providers (AWS, Azure, GCP) or SaaS platforms.
- **Resources**: The individual components of your infrastructure (e.g., an EC2 instance, an S3 bucket).
- **Data Sources**: Allows data to be fetched or computed for use elsewhere in Terraform configuration.
- **State File (`terraform.tfstate`)**: Terraform keeps track of the IDs and properties of the resources it created in a state file. This allows it to map real-world resources to your configuration.

---

## 3. The Terraform Workflow
1. **`terraform init`**: Initializes the working directory and downloads necessary providers.
2. **`terraform plan`**: Creates an execution plan, showing what actions Terraform will take to reach the desired state.
3. **`terraform apply`**: Executes the plan to create/modify infrastructure.
4. **`terraform destroy`**: Removes all resources managed by the configuration.

---

## 4. State Management
- **Local State**: Stored on your machine (bad for teams).
- **Remote State**: Stored in a shared backend (e.g., S3 with DynamoDB locking). Prevents conflicts and allows collaboration.

---

## 5. Terraform Modules
Modules are containers for multiple resources that are used together. They allow you to package and reuse infrastructure code.

---

## Common Interview Questions
- **"What is the difference between Terraform and Ansible?"**: Terraform is primarily for provisioning infrastructure (IaC); Ansible is primarily for configuration management (installing software on existing servers).
- **"Explain the importance of the State file."**: It acts as a source of truth for the managed infrastructure and is used to determine what changes need to be applied.
- **"What is a 'Resource Dependency' in Terraform?"**: Terraform automatically handles dependencies between resources, but you can use `depends_on` to explicitly define them.

## Related Topics
- [[01_Foundations/03_System_Design|System Design (Infrastructure)]]
- [[08_Stack_Deep_Dives/04_DevOps_Cloud_Stack/04_GitHub_Actions_CI_CD|CI/CD]]
