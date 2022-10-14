import os
import platform as plat
from scapy.all import *
from scapy import *
from threading import Thread
import pandas
import time

operating_sys = plat.system()

if operating_sys == "Linux":
    try:
        os.system("sudo airmon-ng start wlan0")
    except:
        os.system("sudo apt-get install aircrack-ng")
        print("Please Restart The System and Re launch the Script")
else:
    print("OS NOT CURRENTLY SUPPORTED, PLEASE USE LINUX")

# initialize the networks dataframe that will contain all access points nearby
networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
# set the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)

def callback(packet):
    if packet.haslayer(scapy.Dot11Beacon):
        # extract the MAC address of the network
        bssid = packet[scapy.Dot11].addr2
        # get the name of it
        ssid = packet[scapy.Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        # extract network stats
        stats = packet[scapy.Dot11Beacon].network_stats()
        # get the channel of the AP
        channel = stats.get("channel")
        # get the crypto
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)

def print_all():
    while True:
        #os.system("clear")
        print(networks)
        time.sleep(0.5)

if __name__ == "__main__":
    # interface name, check using iwconfig
    interface = "wlan0"
    # start the thread that prints all the networks
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
    # start sniffing
    sniff(prn=callback, iface=interface)