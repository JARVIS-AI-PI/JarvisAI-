# 📁 JarvisAI/brain/logbook.py

import json
import os
from datetime import datetime

LOG_FILE = "brain/logs.json"

def log_entry(user_input, jarvis_reply):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user_input,
        "jarvis": jarvis_reply
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def get_last_logs(count=5):
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    return logs[-count:]
