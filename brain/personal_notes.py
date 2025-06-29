import json
import os
from datetime import datetime

NOTES_FILE = "brain/personal_notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(data):
    with open(NOTES_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_note(content, tag="note"):
    data = load_notes()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data[now] = {"tag": tag, "content": content}
    save_notes(data)
    return f"📝 Saved note at {now}"

def search_notes(keyword=None, tag=None):
    data = load_notes()
    result = []
    for timestamp, entry in data.items():
        if (not keyword or keyword.lower() in entry["content"].lower()) and \
           (not tag or tag.lower() == entry["tag"].lower()):
            result.append(f"{timestamp}: {entry['content']}")
    return result if result else ["🔍 No notes found."]
