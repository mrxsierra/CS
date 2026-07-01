import os

base_path = "/home/team/shared/prepvault"

# Folder Structure
folders = [
    "01_Foundations",
    "01_Foundations/01_DSA",
    "01_Foundations/01_DSA/Arrays & Hashing",
    "01_Foundations/01_DSA/Two Pointers",
    "01_Foundations/01_DSA/Sliding Window",
    "01_Foundations/01_DSA/Stack",
    "01_Foundations/01_DSA/Binary Search",
    "01_Foundations/01_DSA/Linked Lists",
    "01_Foundations/01_DSA/Trees",
    "01_Foundations/01_DSA/Tries",
    "01_Foundations/01_DSA/Heap & Priority Queue",
    "01_Foundations/01_DSA/Graphs",
    "01_Foundations/01_DSA/Dynamic Programming",
    "01_Foundations/01_DSA/Greedy",
    "01_Foundations/01_DSA/Intervals",
    "01_Foundations/01_DSA/Math & Geometry",
    "01_Foundations/01_DSA/Bit Manipulation",
    "02_Role_Tracks",
    "03_Interview_Formats",
    "04_Company_Guides",
]

for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Helper to create stub files
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
    with open(os.path.join(base_path, file_path), 'w') as f:
        f.write(content)

# 00_Getting_Started.md
create_stub(
    "00_Getting_Started.md",
    "Getting Started with PrepVault",
    "Welcome to PrepVault! This vault is designed to help you prepare for tech interviews efficiently.",
    ["How to navigate", "Tagging system", "Template usage"],
    ["01_Foundations/01_DSA", "02_Role_Tracks/01_General_SWE"],
    "['getting-started']"
)

# 01_Foundations stubs
foundations = [
    ("01_Foundations/01_DSA.md", "Data Structures & Algorithms", "Core DSA concepts for technical interviews.", ["Arrays", "Trees", "Graphs", "DP"], ["01_Foundations/01_DSA/Arrays & Hashing", "02_Role_Tracks/01_General_SWE"], "['foundations/dsa']"),
    ("01_Foundations/02_SDLC.md", "Software Development Lifecycle", "Foundational knowledge of how software is built.", ["Agile", "CI/CD", "Testing"], ["02_Role_Tracks/05_DevOps_Engineer"], "['foundations/sdlc']"),
    ("01_Foundations/03_System_Design.md", "System Design Fundamentals", "Core components and trade-offs in large scale systems.", ["Load Balancing", "Sharding", "Caching"], ["02_Role_Tracks/03_Backend_Engineer"], "['foundations/system-design']"),
    ("01_Foundations/04_Operating_Systems.md", "Operating Systems", "OS concepts relevant for interviews.", ["Processes & Threads", "Memory Management", "Concurrency"], ["02_Role_Tracks/03_Backend_Engineer", "02_Role_Tracks/05_DevOps_Engineer"], "['foundations/os']"),
    ("01_Foundations/05_Networking.md", "Computer Networking", "Network protocols and architecture.", ["TCP/IP", "HTTP/HTTPS", "DNS"], ["02_Role_Tracks/03_Backend_Engineer", "02_Role_Tracks/02_Frontend_Engineer"], "['foundations/networking']"),
]

for file_path, title, desc, concepts, links, tags in foundations:
    create_stub(file_path, title, desc, concepts, links, tags)

# 02_Role_Tracks stubs
roles = [
    ("02_Role_Tracks/01_General_SWE.md", "General Software Engineer", "Preparation track for general SWE roles.", ["DSA", "System Design", "Behavioral"], ["01_Foundations/01_DSA"], "['role/general-swe']"),
    ("02_Role_Tracks/02_Frontend_Engineer.md", "Frontend Engineer", "Deep-dive into frontend interview topics.", ["React/Vue", "CSS/HTML", "Web Performance"], ["01_Foundations/05_Networking"], "['role/frontend']"),
    ("02_Role_Tracks/03_Backend_Engineer.md", "Backend Engineer", "Deep-dive into backend interview topics.", ["Scalability", "Databases", "APIs"], ["01_Foundations/03_System_Design"], "['role/backend']"),
    ("02_Role_Tracks/04_ML_Engineer.md", "Machine Learning Engineer", "Preparation for ML-specific interviews.", ["Model Training", "Math for ML", "ML Systems"], ["01_Foundations/01_DSA"], "['role/ml']"),
    ("02_Role_Tracks/05_DevOps_Engineer.md", "DevOps Engineer", "Infrastructure and automation interview prep.", ["Kubernetes", "Terraform", "Cloud Platforms"], ["01_Foundations/02_SDLC"], "['role/devops']"),
    ("02_Role_Tracks/06_Data_Engineer.md", "Data Engineer", "Data pipelines and processing interview prep.", ["ETL", "Spark/Flink", "SQL Optimization"], ["01_Foundations/03_System_Design"], "['role/data-engineering']"),
    ("02_Role_Tracks/07_Product_Manager.md", "Product Manager", "Tech-focused PM interview preparation.", ["Product Sense", "Execution", "Technical Fluency"], ["01_Foundations/02_SDLC"], "['role/pm']"),
]

for file_path, title, desc, concepts, links, tags in roles:
    create_stub(file_path, title, desc, concepts, links, tags)

# 03_Interview_Formats stubs
formats = [
    ("03_Interview_Formats/01_Coding_Rounds.md", "Coding Rounds", "What to expect in technical coding interviews.", ["Whiteboarding", "Pair Programming"], ["01_Foundations/01_DSA"], "['interview/coding']"),
    ("03_Interview_Formats/02_System_Design_Rounds.md", "System Design Rounds", "How to approach high-level design interviews.", ["Scalability", "Availability"], ["01_Foundations/03_System_Design"], "['interview/system-design']"),
    ("03_Interview_Formats/03_Behavioral_Rounds.md", "Behavioral Rounds", "Soft skills and experience-based interviews.", ["STAR Method", "Conflict Resolution"], ["02_Role_Tracks/07_Product_Manager"], "['interview/behavioral']"),
    ("03_Interview_Formats/04_HR_Rounds.md", "HR Rounds", "Cultural fit and logistics.", ["Compensation", "Company Values"], [], "['interview/hr']"),
]

for file_path, title, desc, concepts, links, tags in formats:
    create_stub(file_path, title, desc, concepts, links, tags)

# 06_Tag_Index.md
create_stub(
    "06_Tag_Index.md",
    "Tag Index",
    "Central index for navigating the vault via tags.",
    ["#foundations", "#role", "#interview"],
    ["00_Getting_Started"],
    "['index']"
)

# DSA Subfolders - create index files for each
dsa_subfolders = [
    "Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search",
    "Linked Lists", "Trees", "Tries", "Heap & Priority Queue", "Graphs",
    "Dynamic Programming", "Greedy", "Intervals", "Math & Geometry", "Bit Manipulation"
]

for folder in dsa_subfolders:
    create_stub(
        f"01_Foundations/01_DSA/{folder}/Index.md",
        f"{folder} Overview",
        f"Key patterns and problems for {folder}.",
        ["Common Patterns", "Interview Variations"],
        ["01_Foundations/01_DSA"],
        f"['foundations/dsa/{folder.lower().replace(' & ', '-').replace(' ', '-')}' ]"
    )
