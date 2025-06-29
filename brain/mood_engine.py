import json
import os

MOOD_FILE = "brain/mood.json"

DEFAULT_MOOD = "neutral"
VALID_MOODS = ["neutral", "happy", "sad", "angry", "funny", "alert"]

def load_mood():
    if not os.path.exists(MOOD_FILE):
        return DEFAULT_MOOD
    with open(MOOD_FILE, "r") as f:
        data = json.load(f)
        return data.get("current_mood", DEFAULT_MOOD)

def save_mood(mood):
    if mood not in VALID_MOODS:
        return f"❌ Invalid mood: {mood}"
    with open(MOAD_FILE, "w") as f:
        json.dump({"current_mood": mood}, f)
    return f"✅ Mood set to {mood}"

def modify_reply_by_mood(reply, mood):
    if mood == "happy":
        return reply + " 😄 I'm feeling great today!"
    elif mood == "sad":
        return reply + " ...I hope things get better. 😔"
    elif mood == "angry":
        return "Listen. " + reply.upper() + " ⚠️"
    elif mood == "funny":
        return reply + " 😂 Just kidding. Or am I?"
    elif mood == "alert":
        return "⚠️ [Alert Mode] " + reply
    else:
        return reply  # Neutral
