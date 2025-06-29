import os
import time
import hashlib
import psutil
from datetime import datetime

WATCHED_FILES = ["main_ui.py", "config.json", "enginecore.py"]
LOG_FILE = "guardian/guard_log.txt"

def get_file_hash(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_integrity(previous_hashes):
    alerts = []
    for f in WATCHED_FILES:
        new_hash = get_file_hash(f)
        if previous_hashes.get(f) != new_hash:
            alerts.append(f"⚠️ File changed: {f}")
    return alerts

def detect_suspicious_processes():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        name = proc.info['name']
        if name and ("nmap" in name or "aircrack" in name):
            suspicious.append(f"⚠️ Suspicious process: {name}")
    return suspicious

def run_guard_check():
    # Hash snapshot
    previous = {f: get_file_hash(f) for f in WATCHED_FILES}
    time.sleep(5)  # Wait before checking again (simulate live check)
    
    changes = check_integrity(previous)
    risks = detect_suspicious_processes()
    
    log_entries = changes + risks
    if log_entries:
        with open(LOG_FILE, "a") as f:
            for entry in log_entries:
                f.write(f"[{datetime.now()}] {entry}\n")
        return "\n".join(log_entries)
    return "✅ System secure. No intrusion detected."
