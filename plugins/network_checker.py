import os
import socket
import platform
import subprocess

def check_internet():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        return False

def ping_site(site="8.8.8.8"):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "2", site]
    try:
        output = subprocess.check_output(command)
        return output.decode()
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
        return "❌ Unable to get IP"

def run():
    print("🌐 Network Checker Started.")
    while True:
        command = input("Check network (or 'exit'): ").lower()
        
        if "internet" in command:
            online = check_internet()
            print("✅ Internet is available." if online else "❌ No internet.")

        elif "ping" in command:
            site = command.replace("ping", "").strip() or "8.8.8.8"
            print(ping_site(site))

        elif "ip" in command:
            print("💻 Your IP:", get_ip())

        elif "exit" in command:
            print("👋 Exiting Network Checker.")
            break

        else:
            print("❓ Unknown command. Try: internet, ping, ip, exit.")
