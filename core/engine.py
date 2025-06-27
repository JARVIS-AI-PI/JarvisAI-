from jarvis import load_plugins, load_config
from voice.talker import speak
from core.mode import get_mode
from core.commands import run_core_command
from core.memory import remember, recall

plugins = load_plugins()
config = load_config()

def respond_to(text):
    if not text or text.strip() == "":
        return "I didn't catch that."

    text = text.strip()

    # Check for mode switch (e.g., hacking mode, dev mode)
    if get_mode(text):
        return get_mode(text)

    # Check for core command (like 'go silent')
    core_response = run_core_command(text)
    if core_response:
        return core_response

    # Save what user says
    remember("last_input", text)

    # Search through plugins
    for name, plugin in plugins.items():
        try:
            if hasattr(plugin, "can_handle") and plugin.can_handle(text):
                result = plugin.handle(text, config)
                remember("last_output", result)
                if config.get("voice_mode", True):
                    speak(result)
                return result
        except Exception as e:
            return f"Error in plugin {name}: {e}"

    fallback = "Sorry, I don't understand yet."
    remember("last_output", fallback)
    return fallback
