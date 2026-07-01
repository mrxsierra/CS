import os

base_dir = "/home/team/shared/prepvault/08_Stack_Deep_Dives"

for root, dirs, files in os.walk(base_dir):
    if "Index.md" in files:
        index_path = os.path.join(root, "Index.md")
        # Get all other .md files in the same directory
        topic_files = [f for f in files if f.endswith(".md") and f != "Index.md"]
        
        if topic_files:
            with open(index_path, 'r') as f:
                lines = f.readlines()
            
            new_lines = []
            skip = False
            for line in lines:
                if line.startswith("## Key Concepts"):
                    new_lines.append(line)
                    for topic in sorted(topic_files):
                        # Convert filename to title-ish string
                        title = topic.replace(".md", "").replace("_", " ")
                        new_lines.append(f"- [[{topic}|{title}]]\n")
                    skip = True
                elif line.startswith("## ") and skip:
                    skip = False
                    new_lines.append(line)
                elif not skip:
                    new_lines.append(line)
            
            with open(index_path, 'w') as f:
                f.writelines(new_lines)

print("Indices updated successfully.")
