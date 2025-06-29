dangerous_keywords = [
    "hack", "crack", "bypass", "delete all", "format", "shutdown others", 
    "keylogger", "spy", "remote access", "disable firewall", "ddos"
]

def is_safe_command(command):
    lowered = command.lower()
    for word in dangerous_keywords:
        if word in lowered:
            return False
    return True

def check_command(command):
    if not is_safe_command(command):
        warning = (
            "⚠️ WARNING: This action seems potentially unethical or illegal.\n"
            "Jarvis will not proceed without confirmation.\n"
            "This tool is for educational and personal testing only.\n"
            "Do you want to continue? (yes/no)"
        )
        print(warning)
        confirm = input("> ").strip().lower()
        if confirm != "yes":
            print("❌ Command cancelled.")
            return False
    return True

def run():
    print("🛡️ Guardian Layer is Active. Monitoring for unsafe requests...")
