#!/bin/env python3
#-*- coding: utf-8 -*-

# import mylog_ver1
import mylog_ver2

def main():
	# mylog_ver1.printlog("/var/log/messages", "fail")
	mylog_ver2.printlog("/var/log/boot.log", "fail")
	
	
if __name__ == '__main__':
	main()
