import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Example pin layout — modify as needed
PIN_MAP = {
    "light": 17,
    "fan": 27,
    "motor": 22
}

# Setup all pins
for pin in PIN_MAP.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def control_device(device, state):
    pin = PIN_MAP.get(device.lower())
    if pin is None:
        return f"No such device '{device}' connected."
    
    GPIO.output(pin, GPIO.HIGH if state == "on" else GPIO.LOW)
    return f"{device.capitalize()} turned {state}."
