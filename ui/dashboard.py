import os
import time
import socket
import psutil
import platform
import subprocess
from datetime import datetime

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "No Internet"

def get_memory():
    mem = psutil.virtual_memory()
    return f"{int(mem.used/1024/1024)}MB / {int(mem.total/1024/1024)}MB"

def get_uptime():
    seconds = time.time() - psutil.boot_time()
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    return f"{hours}h {minutes%60}min"

def get_cpu_temp():
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
        return temp.replace("temp=", "").strip()
    except:
        return "N/A"

def get_status():
    return {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Date": datetime.now().strftime("%d %B %Y"),
        "IP Address": get_ip(),
        "RAM Usage": get_memory(),
        "Uptime": get_uptime(),
        "CPU Temp": get_cpu_temp(),
        "Platform": platform.system() + " " + platform.machine()
    }
