# 📁 JarvisAI/core/scheduler.py

import threading
import time
from voice.talker import speak

scheduled_tasks = []

def schedule_task(text, delay_seconds):
    t = threading.Thread(target=_delayed_speak, args=(text, delay_seconds))
    t.start()
    scheduled_tasks.append(t)
    return f"Reminder set in {delay_seconds} seconds."

def _delayed_speak(text, delay):
    time.sleep(delay)
    speak(f"⏰ Reminder: {text}")

def parse_schedule_command(command):
    command = command.lower()
    if "remind me in" in command and "to" in command:
        try:
            part = command.split("remind me in")[1].strip()
            time_part, task = part.split("to", 1)
            task = task.strip()

            # Time parser
            delay = 0
            if "second" in time_part:
                delay = int(time_part.split("second")[0].strip())
            elif "minute" in time_part:
                delay = int(time_part.split("minute")[0].strip()) * 60
            elif "hour" in time_part:
                delay = int(time_part.split("hour")[0].strip()) * 3600
            else:
                return "Invalid time format."

            return schedule_task(task, delay)
        except:
            return "Sorry, couldn't understand the reminder format."
    return None
