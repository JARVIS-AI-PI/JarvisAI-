import json
import os

UI_STATE_FILE = "ui_state.json"

# Default state
state = {
    "theme": "dark",
    "font_size": 10,
    "fullscreen": False
}

def load_state():
    global state
    if os.path.exists(UI_STATE_FILE):
        with open(UI_STATE_FILE, "r") as f:
            state.update(json.load(f))
    return state

def save_state():
    with open(UI_STATE_FILE, "w") as f:
        json.dump(state, f)

def apply_command(text):
    global state
    t = text.lower()

    if "green theme" in t:
        state["theme"] = "green"
    elif "dark theme" in t:
        state["theme"] = "dark"
    elif "make text bigger" in t:
        state["font_size"] += 1
    elif "make text smaller" in t:
        state["font_size"] = max(8, state["font_size"] - 1)
    elif "go fullscreen" in t:
        state["fullscreen"] = True
    elif "exit fullscreen" in t:
        state["fullscreen"] = False
    else:
        return None

    save_state()
    return f"UI updated: {state}"
