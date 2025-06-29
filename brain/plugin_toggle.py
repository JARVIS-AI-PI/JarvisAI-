import os
import json

PLUGIN_DIR = "plugins"
PLUGIN_STATE_FILE = "plugins/plugin_state.json"

if not os.path.exists(PLUGIN_STATE_FILE):
    with open(PLUGIN_STATE_FILE, "w") as f:
        json.dump({}, f)

def list_plugins():
    return [f.replace(".py", "") for f in os.listdir(PLUGIN_DIR) if f.endswith(".py") and f != "__init__.py"]

def get_enabled_plugins():
    with open(PLUGIN_STATE_FILE, "r") as f:
        return json.load(f)

def enable_plugin(plugin_name):
    state = get_enabled_plugins()
    state[plugin_name] = True
    with open(PLUGIN_STATE_FILE, "w") as f:
        json.dump(state, f)
    return f"Plugin '{plugin_name}' enabled."

def disable_plugin(plugin_name):
    state = get_enabled_plugins()
    state[plugin_name] = False
    with open(PLUGIN_STATE_FILE, "w") as f:
        json.dump(state, f)
    return f"Plugin '{plugin_name}' disabled."

def is_plugin_enabled(plugin_name):
    state = get_enabled_plugins()
    return state.get(plugin_name, False)
