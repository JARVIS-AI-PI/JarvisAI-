# 📁 JarvisAI/core/memory.py

import json
import os

MEMORY_FILE = "memory.db"

def _load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def _save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f)

def remember(key, value):
    mem = _load_memory()
    mem[key] = value
    _save_memory(mem)

def recall(key, default=""):
    mem = _load_memory()
    return mem.get(key, default)
