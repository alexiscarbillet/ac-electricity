import os

# Path to your MkDocs docs folder
docs_path = "docs"

for root, _, files in os.walk(docs_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)

            # Read file content
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Skip first 7 lines
            new_lines = lines[7:]

            # Write back updated content
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

            print(f"Updated: {file_path}")

print("✅ Done — first 7 lines removed from all Markdown files.")
