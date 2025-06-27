import subprocess
import os

def launch_jarvis():
    ui_path = os.path.join("ui", "main_ui.py")
    if os.path.exists(ui_path):
        subprocess.run(["python3", ui_path])
    else:
        print("Error: UI file not found.")

if __name__ == "__main__":
    launch_jarvis()
