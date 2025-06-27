import json
import os
from core.memory import remember, recall
from datetime import datetime

LEARN_FILE = "learn_log.json"

def log_learning(input_text, output_text):
    log = []
    if os.path.exists(LEARN_FILE):
        with open(LEARN_FILE, "r") as f:
            log = json.load(f)

    log.append({
        "time": str(datetime.now()),
        "input": input_text,
        "response": output_text
    })

    with open(LEARN_FILE, "w") as f:
        json.dump(log, f)

    remember("last_learning", input_text)

def suggest_improvement():
    try:
        with open(LEARN_FILE, "r") as f:
            log = json.load(f)
        if len(log) < 5:
            return "I need more interaction data to suggest improvements."

        # Sample pattern detection (later: ML integration)
        suggestions = []

        if all("?" in entry["input"] for entry in log[-5:]):
            suggestions.append("People are asking many questions — add Q&A plugin or search module.")

        return "\n".join(suggestions) if suggestions else "No suggestions yet."
    except:
        return "Learning system not ready yet."
