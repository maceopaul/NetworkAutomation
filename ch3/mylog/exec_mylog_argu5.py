#!/bin/env python
#-*- coding: utf-8 -*-

import mylog_ver5
import os

# logfile = "/var/log/messages"
logfile = "/var/log/boot.log"
file_length = os.path.getsize(logfile)

# mylog_ver5.printlog("/var/log/boot.log", "fail", int(file_length/2), 3, 5)
mylog_ver5.printlog(logfile, "fail", int(file_length/2), 3, 5)
