import os
import json
from core.plugin_toggle import enable_plugin, disable_plugin, list_plugins, get_enabled_plugins

PLUGIN_DIR = "plugins"
PLUGIN_STATE_FILE = "plugins/plugin_state.json"

def show_plugin_status():
    all_plugins = list_plugins()
    status = get_enabled_plugins()
    result = []

    for plugin in all_plugins:
        is_on = status.get(plugin, False)
        result.append({
            "plugin": plugin,
            "status": "🟢 Enabled" if is_on else "🔴 Disabled"
        })

    return result

def toggle_plugin(plugin_name, turn_on=True):
    if turn_on:
        return enable_plugin(plugin_name)
    else:
        return disable_plugin(plugin_name)

def task_summary():
    tasks = show_plugin_status()
    output = "\n".join([f"{t['plugin']} → {t['status']}" for t in tasks])
    return f"🧠 Jarvis Plugin Center:\n\n{output}"
