from brain.mood_engine import save_mood

def analyze_and_react(user_input):
    emotion = detect_emotion(user_input.lower())

    if emotion:
        save_mood(emotion)
        return f"🤖 I sensed you’re {emotion}. I’ll adjust my mood."

    return None

def detect_emotion(text):
    if any(word in text for word in ["i'm sad", "depressed", "unhappy", "feeling down"]):
        return "sad"
    elif any(word in text for word in ["i'm happy", "feeling great", "awesome", "love"]):
        return "happy"
    elif any(word in text for word in ["angry", "mad", "annoyed", "frustrated"]):
        return "angry"
    elif any(word in text for word in ["haha", "funny", "joke", "lol"]):
        return "funny"
    elif any(word in text for word in ["danger", "alert", "help", "hurry", "urgent"]):
        return "alert"
    return None
