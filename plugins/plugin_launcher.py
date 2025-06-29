import os
import importlib

# Plugin keyword mapping
PLUGIN_KEYWORDS = {
    "calculator": "calculator_plugin",
    "scan": "camera_scan",
    "camera": "camera_scan",
    "network": "network_checker",
    "internet": "network_checker",
    "file": "file_explorer",
    "explorer": "file_explorer",
    "game": "mini_games",
    "riddle": "mini_games",
    "education": "edu_tools",
    "dictionary": "edu_tools",
}

def launch_plugin(query, speak=None):
    query = query.lower()
    
    for keyword, module_name in PLUGIN_KEYWORDS.items():
        if keyword in query:
            try:
                plugin = importlib.import_module(f"plugins.{module_name}")
                if hasattr(plugin, "run"):
                    if speak:
                        speak(f"🔌 Launching {module_name.replace('_', ' ')}...")
                    plugin.run()
                    return f"[✅] {module_name} launched."
                else:
                    return f"[⚠️] {module_name} plugin has no run() function."
            except Exception as e:
                return f"[❌ Error] Failed to load {module_name}: {e}"

    return "❓ I couldn’t find a plugin matching your request."
