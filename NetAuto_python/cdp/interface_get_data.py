#!/bin/env python
#-*- coding: utf-8 -*-

from interface_get_port_type import *

def get_rate(rate, interface_num) :
    # 
    ret = cli("show interface ethernet 1/%i | in rate"%interface_num)
    last_str = ret.split("\n")[2]
    rate_index = last_str.find(rate) + len(rate)
    rate_end_index =last_str.find("bps", rate_index)
    rate_str = last_str[rate_index : rate_end_index].strip()
    str_list = rate_str.split()         # 

    # 
    rate_num = round(float(str_list[0]), 0)
    unit = ""
    if len(str_list) > 1 :
        unit = str_list[1]
    return rate_num * get_byte_num(unit)

def get_byte_num(unit):
    # 
    if unit == "":
        return 1
    elif unit == "K" :
        return pow(2, 10)
    elif unit == "M" :
        return pow(2, 20)
    elif unit == "G" :
        return pow(2, 30)

if __name__ == "__main__":
    interface_num = 24      # 

    port_types = []
    input_pks= []
    output_pks= []

    # 
    i = 1
    while i <= interface_num :
        input_pk = get_rate("input rate", i)
        output_pk = get_rate("output rate", i)
        
        port_types.append(get_port_type(i))
        input_pks.append(input_pk)
        output_pks.append(output_pk)
        i = i + 1
        
    # 
    print port_types
    print input_pks
    print output_pks
