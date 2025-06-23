import json
import os
import importlib
from voice.listener import listen
from voice.talker import speak

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        return {"voice_mode": True, "language": "en", "secure_pin": "0000", "plugins_enabled": []}

def load_plugins():
    plugins = {}
    plugin_dir = "plugins"
    for file in os.listdir(plugin_dir):
        if file.endswith(".py") and not file.startswith("__"):
            name = file[:-3]
            module = importlib.import_module(f"plugins.{name}")
            plugins[name] = module
    return plugins

def main():
    config = load_config()
    plugins = load_plugins()
    print("Jarvis is ready!")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        for name, plugin in plugins.items():
            if hasattr(plugin, "can_handle") and plugin.can_handle(user_input):
                response = plugin.handle(user_input, config)
                print("Jarvis:", response)
                if config.get("voice_mode", True):
                    speak(response)
                break
        else:
            response = "I don’t understand that yet."
            print("Jarvis:", response)
            if config.get("voice_mode", True):
                speak(response)

if __name__ == "__main__":
    main()
