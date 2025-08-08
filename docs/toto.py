import os

# 👇 Customize this:
INSERT_TEXT = '<meta name="google-adsense-account" content="ca-pub-9364684337389377">'  # Change this to the text or HTML you want to insert

def insert_into_head(file_path, insert_text):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Skip if already inserted
    if insert_text in content:
        return

    # Look for <head> tag
    head_open_index = content.find('<head>')
    if head_open_index == -1:
        print(f"⚠️ No <head> tag found in: {file_path}")
        return

    # Inject just after the opening <head> tag
    insert_position = head_open_index + len('<head>')
    new_content = content[:insert_position] + '\n    ' + insert_text + content[insert_position:]

    # Save changes
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"✅ Updated: {file_path}")

def process_repo(insert_text):
    root_path = os.getcwd()  # Automatically use the current working directory
    for foldername, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(foldername, filename)
                insert_into_head(file_path, insert_text)

# 🔃 Run the script
if __name__ == "__main__":
    process_repo(INSERT_TEXT)
