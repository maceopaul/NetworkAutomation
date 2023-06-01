#!/bin/env python
#-*- coding: utf-8 -*-

from interface_get_data import *
import time

def get_rate_change(interface_num, measure, seconds) :
    # 
    port_types = []
    i = 1
    while i <= interface_num :
        # 
        port_types.append(get_port_type(i))
        i = i + 1
        
    # 
    (start_input_pks, start_output_pks) = get_rate_list(interface_num, measure)
    
    time.sleep(seconds)
    
    (input_pks, output_pks) = get_rate_list(interface_num, measure)
    
    return (port_types,
        start_input_pks, input_pks, subtract(start_input_pks, input_pks),
        start_output_pks, output_pks, subtract(start_output_pks, output_pks))

def get_rate_list(interface_num, measure):
    input_pks = []
    output_pks = []
    i = 1
    while i <= interface_num :
        # 
        input_pk = get_rate("input rate", i) / measure
        output_pk = get_rate("output rate", i) / measure
        
        # 
        input_pks.append(input_pk)
        output_pks.append(output_pk)
        i = i + 1
        
    return (input_pks, output_pks)

def subtract(start_rate_list, end_rate_list):
    i = 0
    change_list = []
    while i < len(start_rate_list) :
        change_list.append(end_rate_list[i] - start_rate_list[i])
        i = i + 1
    return change_list

if __name__ == "__main__":
    print "select data rate ."
    interface_num = input("how many interface check? : ")
    seconds = input("check value after second ? : ")
    (port_types,start_input_pks, end_input_pks, change_input_pks,
     start_output_pks, end_output_pks, change_output_pks) = get_rate_change(
         interface_num, get_byte_num("M"), seconds)
    
    print "Input Rate(bps)"
    print "start value : ", start_input_pks
    print "end value : ", end_input_pks
    print "raise rate : ", change_input_pks
    print "=" * 70
    
    print "Output Rate(bps)"
    print "start value : ", start_input_pks
    print "end value : ", end_input_pks
    print "raise rate : ", change_input_pks
    print "=" * 70
    print "port type : ", port_types
