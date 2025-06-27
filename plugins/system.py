import os

def can_handle(text):
    keywords = ["open", "create", "terminal", "file", "shutdown", "reboot"]
    return any(word in text.lower() for word in keywords)

def handle(text, config):
    text = text.lower()

    if "open terminal" in text:
        os.system("lxterminal &")
        return "Opening terminal."

    elif "create file" in text:
        try:
            filename = text.split("create file")[-1].strip()
            if filename:
                with open(filename, "w") as f:
                    f.write("")  # Empty file
                return f"Created file: {filename}"
            else:
                return "Please specify a filename."
        except Exception as e:
            return f"Error creating file: {e}"

    elif "shutdown" in text:
        os.system("sudo shutdown now")
        return "Shutting down..."

    elif "reboot" in text:
        os.system("sudo reboot")
        return "Rebooting..."

    return "Command recognized, but not fully supported yet."
