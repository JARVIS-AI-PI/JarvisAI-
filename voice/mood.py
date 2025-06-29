import pyttsx3

engine = pyttsx3.init()

MOODS = {
    "normal": {"rate": 160, "volume": 1.0},
    "calm": {"rate": 130, "volume": 0.8},
    "fast": {"rate": 200, "volume": 1.0}
}

def set_mood(mood_name):
    mood = MOODS.get(mood_name, MOODS["normal"])
    engine.setProperty('rate', mood["rate"])
    engine.setProperty('volume', mood["volume"])

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[Voice Error] {e}")
