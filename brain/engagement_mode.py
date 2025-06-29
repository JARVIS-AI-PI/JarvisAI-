import time
from threading import Thread
from brain.mood_engine import load_mood
from brain.personal_notes import search_notes
from random import choice

class EngagementJarvis(Thread):
    def __init__(self, delay_minutes=5, speak_callback=None):
        super().__init__()
        self.delay = delay_minutes * 60  # Convert to seconds
        self.speak_callback = speak_callback
        self.active = True

    def run(self):
        while self.active:
            time.sleep(self.delay)
            if not self.active:
                break

            msg = self.generate_engagement()
            if self.speak_callback:
                self.speak_callback(msg)
            else:
                print(f"[Engagement] {msg}")

    def generate_engagement(self):
        mood = load_mood()
        notes = search_notes()
        tips = [
            "Tip: You can ask me to teach a task or take a note.",
            "You can say 'Jarvis, update yourself' if I’m outdated.",
            "Remember, you’re doing great! 💪"
        ]
        actions = [
            f"I'm still here with a {mood} mood. 😊",
            choice(tips),
            "Would you like to continue working or take a break?",
            f"You have {len(notes)} personal notes. Want me to read one?"
        ]
        return choice(actions)

    def stop(self):
        self.active = False
