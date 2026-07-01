import os

base_path = "/home/team/shared/prepvault"

def create_stub(file_path, title, description, key_concepts, links, tags):
    content = f"""---
title: {title}
tags: {tags}
---

# {title}

## Description
{description}

## Key Concepts
{chr(10).join([f"- {concept}" for concept in key_concepts])}

## Related Topics & Applications
{chr(10).join([f"- [[{link}]]" for link in links])}
"""
    os.makedirs(os.path.dirname(os.path.join(base_path, file_path)), exist_ok=True)
    with open(os.path.join(base_path, file_path), 'w') as f:
        f.write(content)

# 1. Rust Language Internals
create_stub(
    "01_Foundations/07_Language_Internals/Rust.md",
    "Rust Language Internals",
    "Deep dive into Rust's memory safety, ownership model, and concurrency primitives.",
    ["Ownership & Borrowing", "Lifetime system", "Traits & Generics", "Concurrency (Send/Sync)", "Unsafe Rust"],
    ["01_Foundations/07_Language_Internals/Index", "01_Foundations/04_Operating_Systems"],
    "['foundations/internals/rust']"
)

# 2. New Role Tracks
create_stub(
    "02_Role_Tracks/09_Data_Scientist.md",
    "Data Scientist Interview Track",
    "Preparation path for Data Science roles, covering statistics, ML, and business intuition.",
    ["Interview process for DS roles", "Statistics & Probability", "Machine Learning Theory", "A/B testing", "SQL for Data Science", "Python Data Stack", "Data Visualization"],
    ["01_Foundations/01_DSA", "01_Foundations/09_SQL_Database_Deep_Dive", "01_Foundations/08_AI_for_Engineers"],
    "['role/data-scientist']"
)

create_stub(
    "02_Role_Tracks/10_Data_Analyst.md",
    "Data Analyst Interview Track",
    "Focused track for Data Analysis, emphasizing SQL, visualization, and business metrics.",
    ["Interview process for DA roles", "SQL Mastery", "Excel for Analytics", "BI Tools (Tableau/PowerBI)", "Python/Pandas for Analysis", "Statistics & Metrics"],
    ["01_Foundations/09_SQL_Database_Deep_Dive", "01_Foundations/02_SDLC"],
    "['role/data-analyst']"
)

# 3. Stack Deep Dives
stacks = {
    "01_Frontend_Stack": [
        ("01_HTML_CSS.md", "HTML & CSS Deep Dive", ["Semantics", "Flexbox/Grid", "CSS Variables", "Accessibility"]),
        ("02_JavaScript_TS.md", "JavaScript & TypeScript Deep Dive", ["ES6+", "Asynchronous JS", "TypeScript Types", "Generics"]),
        ("03_React.md", "React Mastery", ["Hooks", "Fiber Architecture", "Server Components", "State Management"]),
        ("04_Next_JS.md", "Next.js & Server Side Patterns", ["App Router", "SSR/SSG/ISR", "Middleware", "Data Fetching"]),
        ("05_Vite_Build_Tools.md", "Vite & Modern Build Tools", ["HMR", "Bundling", "Rollup/ESBuild", "Module Federation"]),
    ],
    "02_Backend_Stack": [
        ("01_Node_JS.md", "Node.js Internals & Frameworks", ["Event Loop", "Streams", "NestJS", "Fastify"]),
        ("02_Python_FastAPI.md", "FastAPI & Modern Python", ["Pydantic", "Dependency Injection", "Async/Await", "Uvicorn"]),
        ("03_Flask_Django.md", "Django & Flask Patterns", ["ORM", "MVT", "Middleware", "Django Rest Framework"]),
        ("04_Rust_Systems.md", "Rust for Systems & Backend", ["Axum/Actix", "Tokio", "Serde", "Memory Performance"]),
        ("05_API_Design.md", "API Design & Patterns", ["REST", "GraphQL", "gRPC", "WebSockets"]),
    ],
    "03_Data_AI_Stack": [
        ("01_Python_Data_Analytics.md", "Python for Data Analytics", ["Pandas", "NumPy", "Matplotlib", "Seaborn"]),
        ("02_Python_Data_Science.md", "Python for Data Science", ["Scikit-Learn", "SciPy", "Statsmodels"]),
        ("03_Machine_Learning.md", "Machine Learning Mastery", ["Supervised/Unsupervised", "Trees/Forests", "XGBoost", "SVMs"]),
        ("04_Deep_Learning.md", "Deep Learning Foundations", ["Neural Networks", "Backpropagation", "PyTorch/TensorFlow", "CNNs/RNNs"]),
        ("05_LLMs_LangChain.md", "LLMs & AI Orchestration", ["RAG", "LangChain", "LlamaIndex", "Prompt Engineering"]),
        ("06_MLflow_Deployment.md", "MLOps & Model Deployment", ["MLflow", "FastAPI Serving", "Model Monitoring", "Drift Detection"]),
        ("07_Spark_Big_Data.md", "Apache Spark & Big Data", ["RDDs/Dataframes", "Spark SQL", "Distributed Processing", "Optimizations"]),
    ],
    "04_DevOps_Cloud_Stack": [
        ("01_Docker_Containerization.md", "Docker & Container Mastery", ["Dockerfiles", "Multi-stage builds", "Networking", "Security"]),
        ("02_Kubernetes.md", "Kubernetes Orchestration", ["Control Plane", "Pods/Services", "Ingress", "Helm/Kustomize"]),
        ("03_Terraform_IaC.md", "Terraform & Infrastructure as Code", ["HCL", "State Management", "Providers/Modules", "Plan/Apply"]),
        ("04_GitHub_Actions_CI_CD.md", "GitHub Actions & CI/CD", ["Workflows", "Runners", "Secrets", "Deployment Strategies"]),
        ("05_Cloud_Native_Architecture.md", "Cloud Native & Platform Engineering", ["Serverless", "Service Mesh", "Observability", "Reliability"]),
    ],
    "05_Databases_Stack": [
        ("01_SQL_PostgreSQL.md", "PostgreSQL & SQL Mastery", ["ACID", "Indexing", "Query Tuning", "Window Functions"]),
        ("02_MongoDB_NoSQL.md", "MongoDB & NoSQL Patterns", ["Document Store", "Aggregation", "Sharding", "Indexes"]),
        ("03_Redis_Caching.md", "Redis & Caching Strategies", ["Data Types", "Persistence", "Pub/Sub", "Eviction Policies"]),
    ]
}

for folder, files in stacks.items():
    create_stub(f"08_Stack_Deep_Dives/{folder}/Index.md", f"{folder.replace('_', ' ')} Index", f"Overview of the {folder.replace('_', ' ')} module.", ["Introduction", "Module Goals"], ["08_Stack_Deep_Dives/Index"], f"['stack/{folder.lower().split('_')[1]}']")
    for file_name, title, concepts in files:
        create_stub(f"08_Stack_Deep_Dives/{folder}/{file_name}", title, f"Deep dive into {title}.", concepts, [f"08_Stack_Deep_Dives/{folder}/Index"], f"['stack/{folder.lower().split('_')[1]}']")

# 4. Skill Maps
roadmaps = [
    ("01_Frontend_Roadmap.md", "Frontend Engineering Roadmap"),
    ("02_Backend_Roadmap.md", "Backend Engineering Roadmap"),
    ("03_Data_AI_Roadmap.md", "Data & AI Roadmap"),
    ("04_DevOps_Roadmap.md", "DevOps & Cloud Roadmap"),
    ("05_Cybersecurity_Roadmap.md", "Cybersecurity Roadmap"),
]

for file_name, title in roadmaps:
    create_stub(f"09_Skill_Maps/{file_name}", title, f"Visual skill tree and learning path for {title}.", ["Beginner Path", "Advanced Path", "Specialization"], ["00_Getting_Started"], "['roadmap']")

# 5. Top level Index for Stacks
create_stub("08_Stack_Deep_Dives/Index.md", "Stack Deep Dives Index", "Central hub for technology-specific deep dives.", list(stacks.keys()), ["00_Getting_Started"], "['index', 'stack']")
