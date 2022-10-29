#!/usr/bin/python

# python macchanger.py --interface wlan0 --mac 11:aa:dd:ff:gg:hh

import subprocess
import optparse
import re


def macchanger(interface,macaddr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
	subprocess.call(["ifconfig",interface,"up"])

	print ("[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr))

def get_argument():

	parser=optparse.OptionParser()	
	parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
	parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")
	(options,arguments) = parser.parse_args()

	if not options.interface:
		parser.error("[-] Specify an Interface use python macchanger --help for more details")
	elif not options.new_mac:
		parser.error("[-] Specify an MacAddr use python macchanger --help for more details")

	return options

def getmac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	print(ifconfig_result)
	current_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result.decode('utf-8'))
			
	if current_mac:
		print(current_mac.group(0))
		return current_mac.group(0)
	else:
		return None

options= get_argument()
macchanger(options.interface,options.new_mac)
final_mac = getmac(options.interface)
# final_mac = getmac('eth0')

if final_mac == options.new_mac :
	print ("Mac Address Successfully Chaged with new one %r"%final_mac)
else:
	print ("Error Occured Fix It")
