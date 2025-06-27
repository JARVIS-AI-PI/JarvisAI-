# 📁 JarvisAI/voice/talker.py

import platform
import os
import subprocess

# Try pyttsx3 if available (for desktop)
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    use_pyttsx3 = True
except:
    use_pyttsx3 = False

def is_speaker_connected():
    try:
        output = subprocess.check_output("aplay -l", shell=True).decode().lower()
        return "card" in output
    except:
        return False

def speak(text):
    if not text:
        return

    try:
        if use_pyttsx3 and platform.machine() != "armv6l":  # Avoid on Pi Zero 2 W
            engine.say(text)
            engine.runAndWait()
        elif is_speaker_connected():
            os.system(f'espeak "{text}" 2>/dev/null')
        else:
            print(f"[SPEAK-TXT]: {text}")
    except Exception as e:
        print(f"[Voice Error] {e}")
