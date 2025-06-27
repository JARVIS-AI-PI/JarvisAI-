import os

def can_handle(text):
    keywords = ["scan network", "port scan", "mac address", "ping device"]
    return any(kw in text.lower() for kw in keywords)

def handle(text, config):
    pin = input("Enter security PIN to continue: ").strip()
    if pin != config.get("secure_pin", "0000"):
        return "Incorrect PIN. Access denied."

    if "scan network" in text:
        return os.popen("arp -a").read()

    elif "port scan" in text:
        target = input("Enter IP to scan: ").strip()
        return os.popen(f"nmap {target}").read()

    elif "mac address" in text:
        return os.popen("ifconfig").read()

    elif "ping device" in text:
        ip = input("Enter IP to ping: ").strip()
        return os.popen(f"ping -c 4 {ip}").read()

    return "No matching command found in guardian module."
