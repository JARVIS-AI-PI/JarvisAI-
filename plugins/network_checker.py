# 📁 JarvisAI/plugins/network_checker.py

import socket
import subprocess
import platform

def check_internet():
    try:
        host = socket.gethostbyname("www.google.com")
        sock = socket.create_connection((host, 80), 2)
        sock.close()
        return True
    except:
        return False

def ping_site(site="8.8.8.8"):
    param = "-n" if platform.system().lower()=="windows" else "-c"
    cmd = ["ping", param, "2", site]
    try:
        out = subprocess.check_output(cmd)
        return out.decode()
    except Exception as e:
        return f"[❌ Ping Error] {e}"

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "❌ Unable to retrieve IP"

def run():
    print("🌐 Network Checker Started")
    while True:
        cmd = input("Network cmd (or 'exit'): ").lower()
        if "internet" in cmd:
            print("✅ Online" if check_internet() else "❌ Offline")
        elif "ping" in cmd:
            site = cmd.replace("ping", "").strip() or "8.8.8.8"
            print(ping_site(site))
        elif "ip" in cmd:
            print("💻 IP:", get_ip())
        elif cmd == "exit":
            break
        else:
            print("❓ Try: internet / ping <host> / ip / exit")
