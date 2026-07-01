import os
import re

root_dir = "/home/team/shared/prepvault"
exclude_dirs = {".obsidian", ".git"}

for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for f in files:
        if not f.endswith(".md"):
            continue
        
        abs_path = os.path.join(root, f)
        with open(abs_path, "r") as file:
            content = file.read()
        
        def lowercase_link(match):
            inner = match.group(1)
            # Split by | (alias) and # (anchor)
            # We want to lowercase the path part, which is before | or #
            
            # Find first occurrence of | or #
            split_idx = len(inner)
            m = re.search(r'[|#]', inner)
            if m:
                split_idx = m.start()
            
            path_part = inner[:split_idx]
            rest = inner[split_idx:]
            
            # Lowercase path part and replace spaces with underscores
            new_path = path_part.lower().replace(" ", "_")
            # Special case for Index -> index
            new_path = new_path.replace("index", "index") # already lower
            
            return "[[" + new_path + rest + "]]"

        new_content = re.sub(r'\[\[(.*?)\]\]', lowercase_link, content)
        
        if new_content != content:
            with open(abs_path, "w") as file:
                file.write(new_content)
                print(f"Updated links in {abs_path}")
