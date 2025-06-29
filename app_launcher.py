import subprocess
import os
import sys

def start_jarvis():
    try:
        print("🚀 Launching Jarvis AI interface...")
        subprocess.Popen([sys.executable, "ui/main_ui.py"])
    except Exception as e:
        print(f"[Launcher Error] {e}")

if __name__ == "__main__":
    start_jarvis()
