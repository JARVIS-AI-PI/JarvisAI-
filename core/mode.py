current_mode = "default"

def get_mode(text):
    global current_mode
    text = text.lower()

    if "hacking mode" in text:
        current_mode = "hacking"
        return "Hacking mode activated. Ethical use only."

    elif "developer mode" in text:
        current_mode = "developer"
        return "Developer mode activated."

    elif "safe mode" in text or "normal mode" in text:
        current_mode = "default"
        return "Returned to safe mode."

    elif "what is my mode" in text:
        return f"You are currently in {current_mode} mode."

    return None

def current():
    return current_mode
