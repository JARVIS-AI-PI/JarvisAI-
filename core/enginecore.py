from jarvis import load_plugins, load_config
from voice.talker import speak
from core.mode import get_mode
from core.commands import run_core_command
from core.memory import remember, recall
from core.scheduler import parse_schedule_command
from core.ui_state import apply_command
from core.self_train import log_learning
from core.plugin_builder import create_plugin

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
        log_learning(text, mode_response)
        return mode_response

    # 2. Handle instant commands
    core_response = run_core_command(text)
    if core_response:
        speak(core_response)
        log_learning(text, core_response)
        return core_response

    # 3. Scheduler
    schedule_response = parse_schedule_command(text)
    if schedule_response:
        speak(schedule_response)
        log_learning(text, schedule_response)
        return schedule_response

    # 4. UI control
    ui_response = apply_command(text)
    if ui_response:
        speak(ui_response)
        log_learning(text, ui_response)
        return ui_response

    # 5. Plugin builder (detect pattern like: create plugin ...)
    if "create plugin" in text.lower():
        try:
            parts = text.split("create plugin")[1].strip().split(" that responds to ")
            name = parts[0].strip()
            phrase_part = parts[1].strip().split(" with ")
            trigger = phrase_part[0].strip()
            response = phrase_part[1].strip()
            result = create_plugin(name, trigger, response)
            speak(result)
            log_learning(text, result)
            return result
        except:
            msg = "Couldn't understand plugin creation format."
            speak(msg)
            return msg

    # 6. Save input
    remember("last_input", text)

    # 7. Run plugins
    for name, plugin in plugins.items():
        try:
            if hasattr(plugin, "can_handle") and plugin.can_handle(text):
                result = plugin.handle(text, config)
                remember("last_output", result)
                if config.get("voice_mode", True):
                    speak(result)
                log_learning(text, result)
                return result
        except Exception as e:
            return f"Error in plugin {name}: {e}"

    fallback = "Sorry, I don't understand yet."
    remember("last_output", fallback)
    log_learning(text, fallback)
    return fallback
