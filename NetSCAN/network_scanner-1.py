#!/usr/bin/python3

import scapy.all as scapy
''
def scan(ip):
	scapy.arping(ip)
	#Well defined method to do the arp resquest respond work with a single line


scan("192.168.253.1/24")