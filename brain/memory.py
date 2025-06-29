import json
import os

MEMORY_FILE = "brain/memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def remember(key, value):
    memory = load_memory()
    memory[key.lower()] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key.lower(), "I don’t remember that.")

def forget(key):
    memory = load_memory()
    if key.lower() in memory:
        del memory[key.lower()]
        save_memory(memory)
        return f"I forgot '{key}'."
    else:
        return f"I didn't remember '{key}' anyway."
