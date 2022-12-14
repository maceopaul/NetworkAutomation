#!/usr/bin/python3

import scapy.all as scapy

def scan(ip):
	
	arp_request = scapy.ARP(pdst = ip)
	#creating arp_request object with dst_ip=user_input_ip

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	#create a broadcast object to have Ether frame property with dst_mac = ff:ff:ff:ff:ff:ff

	arp_request_broadcast = broadcast/arp_request
	#combine the Ether frame to arp_request to send

	answered_list = scapy.srp(arp_request_broadcast,timeout=1)[0]
	#scapy.srp to send the packet in layer2 Ether fram which returns 2 value answered,unanswered
	#timeout=1 specify wait for 1 sec not till you getting replay	

	print ("IpAdrr\t\t\tMacAddr")
	print ("------------------------------------------")
	for elements in answered_list:
		print (elements[1].psrc ,"\t\t", elements[1].hwsrc)
	

scan("192.168.253.1/24")