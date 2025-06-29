import os
from brain.chatgpt import ask_chatgpt

def format_plugin_code(name, description):
    prompt = f"""
    Create a Python plugin for a Jarvis AI assistant.
    Plugin name: {name}
    Purpose: {description}
    The plugin must include a `run()` function.
    Use only Python standard libraries. Avoid GUI.
    Output only valid Python code. Don't explain anything.
    """
    return ask_chatgpt(prompt)

def create_plugin(name, description):
    plugin_code = format_plugin_code(name, description)
    if not plugin_code:
        return "[❌] Failed to generate plugin code."

    filename = f"{name.lower().replace(' ', '_')}.py"
    path = os.path.join("plugins", filename)

    try:
        with open(path, "w") as f:
            f.write(plugin_code)
        return f"[✅] Plugin '{filename}' created."
    except Exception as e:
        return f"[❌] Error writing plugin: {e}"

def run():
    print("🛠️ Plugin Builder Started")
    while True:
        cmd = input("Say: 'create plugin to <do something>' (or 'exit'): ").lower()
        if "create" in cmd and "plugin" in cmd:
            try:
                parts = cmd.split("plugin to")
                name = parts[1].strip().split()[0]
                desc = parts[1].strip()
                result = create_plugin(name, desc)
                print(result)
            except:
                print("⚠️ Format: 'create plugin to shutdown Pi'")
        elif "exit" in cmd:
            print("👋 Exiting Plugin Builder.")
            break
        else:
            print("❓ Say: create plugin to <do something>")
