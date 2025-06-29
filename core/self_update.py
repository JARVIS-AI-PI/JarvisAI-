import os
import datetime
from brain.chatgpt import ask_chatgpt

LOG_FILE = "jarvis.log"

def get_recent_logs(n=30):
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    return "".join(lines[-n:])

def suggest_improvements():
    logs = get_recent_logs()
    if not logs:
        return "No logs found. Nothing to improve."
    
    prompt = f"""
    You are the core AI of Jarvis.
    Based on these logs and recent activity, suggest improvements or bug fixes:
    ```
    {logs}
    ```
    Then provide full updated Python code snippets if needed.
    Only return code, no explanations.
    """
    return ask_chatgpt(prompt)

def apply_suggestions():
    suggestions = suggest_improvements()
    if "def " in suggestions or "import " in suggestions:
        print("[🛠️ Suggestion Generated]")
        filename = f"improvement_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        with open(f"plugins/{filename}", "w") as f:
            f.write(suggestions)
        return f"[✅ Improvement saved to {filename}]"
    return "[ℹ️ No actionable code in suggestions.]"

def run():
    print("🧠 Self-Update & Optimization Running...")
    result = apply_suggestions()
    print(result)
