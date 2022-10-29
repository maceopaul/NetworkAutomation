#!/usr/bin/python

import subprocess
import re

ifconf = subprocess.check_output(["ifconfig","eth0"])
print (ifconf)

mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconf.decode('utf-8'))

print (mac.group(0))