import pyttsx3
from brain.mood_engine import load_mood

def get_engine_by_mood():
    engine = pyttsx3.init()
    mood = load_mood()

    # Default properties
    rate = 160
    volume = 1.0

    # Customize voice parameters based on mood
    if mood == "happy":
        rate = 190
    elif mood == "sad":
        rate = 120
        volume = 0.8
    elif mood == "angry":
        rate = 180
        volume = 1.0
    elif mood == "funny":
        rate = 175
    elif mood == "alert":
        rate = 200
        volume = 1.0

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    return engine

def speak(text):
    try:
        engine = get_engine_by_mood()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[Adaptive Voice Error] {e}")
