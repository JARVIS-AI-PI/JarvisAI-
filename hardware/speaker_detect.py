import os
import subprocess

def is_speaker_connected():
    try:
        output = subprocess.check_output("aplay -l", shell=True).decode()
        return "card" in output.lower()
    except:
        return False

def speak(text):
    if not text:
        return

    if is_speaker_connected():
        os.system(f'espeak "{text}" 2>/dev/null')
    else:
        print(f"[SPEAK-TXT]: {text}")
