import os
import json
import random
import re
from datetime import datetime
from google import genai
from ruamel.yaml import YAML

# 1. Configuration & Client Setup
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Initialize YAML with strict formatting to prevent line-breaks
yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096  # CRITICAL: Prevents breaking long lines
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.allow_unicode = True

CONFIG_PATH = 'mkdocs.yml'
HISTORY_PATH = 'topic_history.json'
ALLOWED_CATEGORIES = ["Market & Buying Guides", "Future Tech & Smart Home", "Projects & DIY"]

def sanitize_title(title_text):
    """Removes hashes and colons; MkDocs handles quotes if we use yaml.dump properly."""
    return title_text.replace('#', '').replace(':', '').strip()

def slugify(text):
    """Creates an alphanumeric + underscore filename."""
    temp = text.lower().replace(" ", "_").replace("-", "_")
    return re.sub(r'[^a-z0-9_]', '', temp)

def get_new_content():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r') as f:
            history = json.load(f)
    else:
        history = []

    category = random.choice(ALLOWED_CATEGORIES)
    
    prompt = f"""
    Write a technical but accessible markdown article about Electricity (a specific aspect), a specific electrical component or provider, etc.
    Category: {category}
    Avoid these previous topics: {', '.join(history[-10:])}
    
    Requirements:
    - Use a descriptive H1 title.
    - Include a 'Comparison' or 'Technical Specs' table.
    - Output ONLY the markdown content. Do not wrap in ```markdown fences.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    
    raw_content = response.text.strip()
    
    # Clean up accidental fences
    if raw_content.startswith("```"):
        raw_content = re.sub(r'^```[a-z]*\n', '', raw_content)
        raw_content = re.sub(r'\n```$', '', raw_content)

    # Extract and Clean Title
    lines = raw_content.split('\n')
    raw_title = lines[0].replace('# ', '').strip()
    clean_title = sanitize_title(raw_title)
    
    lines[0] = f"# {clean_title}"
    final_content = "\n".join(lines)
    
    filename = f"{slugify(clean_title)}.md"
    
    return category, filename, final_content, clean_title

def update_nav(category_name, file_path, title):
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = yaml.load(f)

    nav = config.get('nav', [])
    
    for item in nav:
        if isinstance(item, dict) and category_name in item:
            if not isinstance(item[category_name], list):
                item[category_name] = []
            
            # Use the original ruamel.yaml logic to add the entry
            # The yaml.width setting will handle the long string formatting
            item[category_name].append({title: file_path})
            break

    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(config, f)

# --- Execution ---
cat, fname, content, title = get_new_content()

folder_map = {
    "Market & Buying Guides": "market",
    "Future Tech & Smart Home": "smart_home",
    "Projects & DIY": "projects"
}
folder = folder_map[cat]
os.makedirs(f"docs/{folder}", exist_ok=True)

full_path = f"docs/{folder}/{fname}"
with open(full_path, "w", encoding='utf-8') as f:
    f.write(content)

update_nav(cat, f"{folder}/{fname}", title)

# Update history
if os.path.exists(HISTORY_PATH):
    with open(HISTORY_PATH, 'r') as f: history = json.load(f)
else:
    history = []
history.append(title)
with open(HISTORY_PATH, 'w') as f: json.dump(history, f)

print(f"Successfully generated: {title} -> {full_path}")