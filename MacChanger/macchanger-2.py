#!/usr/bin/python

import subprocess

interface = input("Interface> ")
macaddr = input("MacAddr> ")

print ("[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr))


subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
subprocess.call(["ifconfig",interface,"up"])