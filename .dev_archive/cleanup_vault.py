import os
import re

def standardize_name(name):
    if name == "README.md":
        return name
    # Lowercase
    name = name.lower()
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    # Replace multiple underscores with one
    name = re.sub(r'_+', '_', name)
    return name

root_dir = "/home/team/shared/prepvault"
rename_map = {}

# Exclude .obsidian
exclude_dirs = {".obsidian", ".git"}

# First pass: collect renames
for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    # Process files
    for f in files:
        if not f.endswith(".md"):
            continue
        old_path = os.path.join(root, f)
        new_name = standardize_name(f)
        new_path = os.path.join(root, new_name)
        if old_path != new_path:
            rename_map[old_path] = new_path

    # Process dirs (in reverse to rename children first? no, walk top-down but record)
    # Actually we should rename directories too.
    for d in dirs:
        old_path = os.path.join(root, d)
        new_name = standardize_name(d)
        new_path = os.path.join(root, new_name)
        if old_path != new_path:
            rename_map[old_path] = new_path

# To handle directory renames, we need to sort the paths by length (deepest first)
# to avoid invalidating parent paths while renaming children? 
# Actually, if we rename parents first, children's "old_path" changes.
# If we rename children first, parent path remains valid.
sorted_paths = sorted(rename_map.keys(), key=len, reverse=True)

# Actually, I'll just rename everything to a temporary name first or just do it carefully.
# Better: rename children, then parents.

# Let's refine the rename_map to be absolute paths.
# And let's update links in all files.

all_md_files = []
for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for f in files:
        if f.endswith(".md"):
            all_md_files.append(os.path.join(root, f))

# Mapping for link replacement
# We need to map the "Obsidian path" (relative to root, no extension if possible)
def get_obsidian_path(abs_path):
    rel = os.path.relpath(abs_path, root_dir)
    if rel.endswith(".md"):
        rel = rel[:-3]
    return rel

link_map = {}
for old_p, new_p in rename_map.items():
    old_link = get_obsidian_path(old_p)
    new_link = get_obsidian_path(new_p)
    link_map[old_link] = new_link

# Add mappings for directories
# (If we rename a directory, links starting with that directory need update)
# Link map should be sorted by length reverse to replace longer paths first.
sorted_link_map = sorted(link_map.items(), key=lambda x: len(x[0]), reverse=True)

# Rename files and directories
for old_p in sorted_paths:
    new_p = rename_map[old_p]
    print(f"Renaming {old_p} -> {new_p}")
    os.rename(old_p, new_p)

# Update links in all md files
# New list of md files since paths changed
all_md_files_new = []
for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for f in files:
        if f.endswith(".md"):
            all_md_files_new.append(os.path.join(root, f))

for md_file in all_md_files_new:
    with open(md_file, "r") as f:
        content = f.read()
    
    new_content = content
    for old_l, new_l in sorted_link_map:
        # Regex for wikilinks: [[old_l]] or [[old_l|alias]] or [[old_l#anchor]] or [[old_l#anchor|alias]]
        # We replace old_l with new_l but only if it's the exact path part.
        # This is tricky with regex. 
        # Simpler: replace inside [[ ]]
        def replace_link(match):
            inner = match.group(1)
            # Split by | and #
            parts = re.split(r'([|#])', inner)
            path_part = parts[0].strip()
            if path_part == old_l:
                parts[0] = new_l
            return "[[" + "".join(parts) + "]]"

        new_content = re.sub(r'\[\[(.*?)\]\]', replace_link, new_content)
    
    if new_content != content:
        with open(md_file, "w") as f:
            f.write(new_content)
