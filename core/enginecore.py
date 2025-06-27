from jarvis import load_plugins, load_config
from voice.talker import speak
from core.mode import get_mode
from core.commands import run_core_command
from core.memory import remember, recall
from core.scheduler import parse_schedule_command
from core.ui_state import apply_command

plugins = load_plugins()
config = load_config()

def respond_to(text):
    if not text or text.strip() == "":
        return "I didn't catch that."

    text = text.strip()

    # 1. Check for mode switch
    mode_response = get_mode(text)
    if mode_response:
        speak(mode_response)
        return mode_response

    # 2. Handle instant commands (mute, exit)
    core_response = run_core_command(text)
    if core_response:
        speak(core_response)
        return core_response

    # 3. Scheduler (reminders)
    schedule_response = parse_schedule_command(text)
    if schedule_response:
        speak(schedule_response)
        return schedule_response

    # 4. UI Control (theme, font, fullscreen)
    ui_response = apply_command(text)
    if ui_response:
        speak(ui_response)
        return ui_response

    # 5. Save input
    remember("last_input", text)

    # 6. Try all plugins
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
