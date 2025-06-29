# 📁 JarvisAI/brain/memory.py

import json
import os

MEMORY_FILE = "brain/memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def remember(key, value):
    mem = load_memory()
    mem[key.lower()] = value
    save_memory(mem)

def recall(key):
    mem = load_memory()
    return mem.get(key.lower(), "I don’t remember that.")

def forget(key):
    mem = load_memory()
    if key.lower() in mem:
        del mem[key.lower()]
        save_memory(mem)
        return f"I forgot '{key}'."
    return f"I didn't remember '{key}'."
