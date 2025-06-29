import json
import os

TASK_FILE = "brain/custom_tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return {}
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(data):
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=2)

def teach_task(name, steps):
    data = load_tasks()
    data[name.lower()] = steps
    save_tasks(data)
    return f"✅ Task '{name}' learned."

def get_task(name):
    data = load_tasks()
    return data.get(name.lower(), None)

def execute_task(task):
    print(f"🤖 Executing custom task:")
    for step in task:
        print(f"➡️ {step}")
        # You can expand this to run commands automatically
