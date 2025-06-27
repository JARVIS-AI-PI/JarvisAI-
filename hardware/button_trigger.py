import RPi.GPIO as GPIO
import time
import threading
from voice.listener import listen_and_process

BUTTON_PIN = 4  # You can use any free GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def on_button_press(channel):
    print("🔘 Button pressed! Starting voice input...")
    listen_and_process()

def start_button_listener():
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=on_button_press, bouncetime=300)
    print(f"🟢 Button trigger active on GPIO {BUTTON_PIN}")

# Run this in a separate thread to avoid blocking
threading.Thread(target=start_button_listener, daemon=True).start()
