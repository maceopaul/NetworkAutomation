#!/bin/env python
#-*- coding: utf-8 -*-

from cli import *

def get_port_type(interface_num) :
    str = cli("show interface ethernet 1/%i"%interface_num)
    title_idx = str.find("Port mode is ")
    port_type = "None"
    if title_idx >= 0 :
        enter_idx = str.find("\n", title_idx)   
        
        # 'Port mode is access'
        # line_str: 'Port mode is access'
        # str[title_idx : enter_idx].split() ['Port', 'mode', 'is', 'access']
        line_str = str[title_idx : enter_idx].split()       
        port_type = line_str[len(line_str)-1]
    return port_type


if __name__ == "__main__":
    interface_num = 24                          # digit number 24
    port_types = []

    i = 1
    while i <= interface_num :
        port_types.append(get_port_type(i))     # command run
        i = i + 1

    print port_types
