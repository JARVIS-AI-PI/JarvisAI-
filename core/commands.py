import sys
import os
from voice.talker import speak

def run_core_command(text):
    t = text.lower()

    if "go silent" in t or "mute yourself" in t:
        return _toggle_voice(False)

    elif "speak again" in t or "unmute" in t:
        return _toggle_voice(True)

    elif "exit jarvis" in t or "shutdown jarvis" in t:
        speak("Goodbye.")
        sys.exit(0)

    elif "minimize" in t:
        return "Sorry, minimize is only supported in desktop GUI mode for now."

    elif "clear memory" in t:
        if os.path.exists("memory.db"):
            os.remove("memory.db")
        return "Memory cleared."

    return None

def _toggle_voice(state: bool):
    from jarvis import load_config, save_config
    config = load_config()
    config["voice_mode"] = state
    save_config(config)
    return "Voice mode on." if state else "Voice muted."
