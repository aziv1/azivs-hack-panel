import platform as plat
import os
import time
from scapy.all import *

#ENSURE THAT YOU ARE ON LINUX
platform_system = plat.system()
if platform_system != "Linux":
    print("Unsuppoted OS, Quitting Now")
    quit()
else:
    os.system("airmon-ng check kill")
    time.sleep(5)
    os.system("airmon-ng start wlan0")
    
################
# Start Script #
################

from scapy.all import *

# interface to use to send beacon frames, must be in monitor mode
iface = "wlan0mon"
# generate a random MAC address (built-in in scapy)
sender_mac = RandMAC()
# SSID (name of access point)
ssid = "TELSTRA-C5865"
# 802.11 frame
dot11 = scapy.all.Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender_mac, addr3=sender_mac)
# beacon layer
beacon = scapy.all.Dot11Beacon()
# putting ssid in the frame
essid = scapy.all.Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
# stack all the layers and add a RadioTap
frame = scapy.all.RadioTap()/dot11/beacon/essid
# send the frame in layer 2 every 100 milliseconds forever
# using the `iface` interface
sendp(frame, inter=0.1, iface=iface, loop=1)