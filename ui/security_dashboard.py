import json
import os

SCAN_LOG = "plugins/scan_logs.json"

def get_scan_data():
    if not os.path.exists(SCAN_LOG):
        return {"timestamp": "No Scan Found", "devices": []}
    
    with open(SCAN_LOG, "r") as f:
        data = json.load(f)
    return data

def format_dashboard():
    data = get_scan_data()
    output = f"🔐 Jarvis Security Dashboard\n\n🕒 Last Scan: {data['timestamp']}\n\n"
    
    if not data["devices"]:
        output += "No devices found.\n"
        return output

    for idx, device in enumerate(data["devices"], 1):
        output += f"{idx}. IP: {device['ip']} — MAC: {device['mac']}\n"

    return output
