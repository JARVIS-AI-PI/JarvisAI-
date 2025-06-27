from picamera2 import Picamera2
from datetime import datetime
import os

SAVE_DIR = "snapshots"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

picam = Picamera2()
picam.configure(picam.create_still_configuration())

def take_picture():
    try:
        filename = f"{SAVE_DIR}/jarvis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        picam.start()
        picam.capture_file(filename)
        picam.stop()
        return f"📸 Picture taken and saved to {filename}"
    except Exception as e:
        return f"Camera error: {e}"
