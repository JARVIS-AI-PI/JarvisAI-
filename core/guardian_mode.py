RISKY_COMMANDS = [
    "rm", "delete", "format", "shutdown", "reboot",
    "mkfs", "rmdir", "halt", "poweroff", "passwd"
]

def is_risky(text):
    text = text.lower()
    return any(cmd in text for cmd in RISKY_COMMANDS)

def warn_if_risky(text):
    if is_risky(text):
        return "⚠️ This looks risky. Are you sure you want to do that?"
    return None
