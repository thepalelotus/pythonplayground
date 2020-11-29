#!/usr/bin/python3.8

from scapy.all import *
import time

ap_list = []
iface = "wlan0"

def PacketHandler(pkt) :
	if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 8 :
			if pkt.addr2 not in ap_list :
				ap_list.append(pkt.addr2)
				print("[+] AP MAC: %s With SSID: %s " %(pkt.addr2, pkt.info.decode()))

def changeChannel():
	ch = 1
	while True:
		os.system("iwconfig wlan0 channel %s " % ch)
		# switch channgek frin 1 to 14 each 0.5s
		ch = ch % 14 + 1
		time.sleep(0.5)

def setMonitor(iface):
	print("[+] Configuring interface...\n")
	os.system(' ifconfig ' + iface + ' down ')
	try:
		print("[+] Attempting to change interface to monitor mode...\n")
		os.system(' iwconfig ' + iface + ' mode monitor ')
		print("[*] Interface set to monitor mode! Listening for AP's...\n")
	except:
		print("[-] Failed to setup monitor mode...")
		sys.exit(1)
	os.system(' ifconfig ' + iface + ' up ')
	return iface

setMonitor(iface)

channelChanger = Thread(target=changeChannel)
channelChanger.daemon = True
channelChanger.start()

if __name__ == "__main__":
	sniff(iface="wlan0", prn = PacketHandler)
