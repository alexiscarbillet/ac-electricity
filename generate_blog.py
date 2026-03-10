import os
import json
import random
from datetime import datetime
from google import genai
from ruamel.yaml import YAML

# 1. Configuration & Client Setup
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

CONFIG_PATH = 'mkdocs.yml'
HISTORY_PATH = 'topic_history.json'
ALLOWED_CATEGORIES = ["Market & Buying Guides", "Future Tech & Smart Home", "Projects & DIY"]

def get_new_content():
    # Load history to ensure we don't repeat topics
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r') as f:
            history = json.load(f)
    else:
        history = []

    # Pick a random category to write for this week
    category = random.choice(ALLOWED_CATEGORIES)
    
    prompt = f"""
    Write a technical but accessible markdown article about Electricity.
    Category: {category}
    Avoid these previous topics: {', '.join(history[-10:])}
    
    Requirements:
    - Use a catchy H1 title.
    - Include a 'Comparison' or 'Technical Specs' table.
    - Focus on 2026 trends.
    - Output ONLY the markdown content.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    
    # Simple slugify for filename
    title = response.text.split('\n')[0].replace('# ', '').strip()
    filename = "".join(x for x in title if x.isalnum() or x in " -").replace(" ", "_").lower() + ".md"
    
    return category, filename, response.text, title

def update_nav(category_name, file_path, title):
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.load(f)

    # Find the navigation section
    nav = config.get('nav', [])
    
    for item in nav:
        if isinstance(item, dict) and category_name in item:
            # item[category_name] is the [] list you added
            if not isinstance(item[category_name], list):
                item[category_name] = []
            
            # Append the new page: {"Title": "folder/file.md"}
            item[category_name].append({title: file_path})
            break

    with open(CONFIG_PATH, 'w') as f:
        yaml.dump(config, f)

# Execute
cat, fname, content, title = get_new_content()

# Determine folder based on category
folder_map = {
    "Market & Buying Guides": "market",
    "Future Tech & Smart Home": "smart_home",
    "Projects & DIY": "projects"
}
folder = folder_map[cat]
os.makedirs(f"docs/{folder}", exist_ok=True)

full_path = f"docs/{folder}/{fname}"
with open(full_path, "w") as f:
    f.write(content)

# Update the YAML 'nav'
update_nav(cat, f"{folder}/{fname}", title)

# Update history
history = []
if os.path.exists(HISTORY_PATH):
    with open(HISTORY_PATH, 'r') as f: history = json.load(f)
history.append(title)
with open(HISTORY_PATH, 'w') as f: json.dump(history, f)