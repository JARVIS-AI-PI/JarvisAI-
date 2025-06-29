import os
import re
from datetime import datetime

PLUGIN_FOLDER = "plugins"

if not os.path.exists(PLUGIN_FOLDER):
    os.makedirs(PLUGIN_FOLDER)

def sanitize_name(text):
    return re.sub(r'\W+', '_', text).lower()

def create_plugin(name, description, code_block):
    filename = f"{PLUGIN_FOLDER}/{sanitize_name(name)}.py"
    if os.path.exists(filename):
        return f"Plugin '{name}' already exists."
    
    try:
        with open(filename, "w") as f:
            f.write(f"# Auto-generated Plugin\n")
            f.write(f"# Name: {name}\n")
            f.write(f"# Description: {description}\n")
            f.write(f"# Created on: {datetime.now()}\n\n")
            f.write(f"def run():\n")
            for line in code_block.strip().splitlines():
                f.write(f"    {line}\n")
        return f"✅ Plugin '{name}' created."
    except Exception as e:
        return f"Error: {e}"

# Example usage inside voice:
# create_plugin("greet", "Say hello every time Jarvis starts", 'print("Hello from plugin!")')
