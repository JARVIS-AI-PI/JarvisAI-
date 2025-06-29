import scapy.all as scapy
from datetime import datetime

def scan(ip_range="192.168.1.1/24"):
    print(f"📡 Scanning network: {ip_range}")
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast/arp_request
    result = scapy.srp(arp_packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices

def save_scan(devices, filename="plugins/scan_logs.json"):
    import json
    with open(filename, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "devices": devices
        }, f, indent=2)

def run_network_scan():
    try:
        devices = scan()
        save_scan(devices)
        print("🛡️ Network scan complete.")
        return devices
    except Exception as e:
        return f"❌ Scan failed: {e}"
