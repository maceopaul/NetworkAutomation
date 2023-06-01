#!/bin/env python
#-*- coding: utf-8 -*-

from cli import *
import datetime
from interface_data_variation import *
    
def get_max_rate() :
    sh_int_data = cli("show interface ethernet 1/1")        # 
    keyword = "full-duplex, "                               # 'full-duplex, '
    index = sh_int_data.find(keyword) + len(keyword)
    if index < 0 :
        max_rate = 0
        unit = ""
        return (max_rate, unit)
        
    max_rate_line = sh_int_data[index : sh_int_data.find(",", index)]   # 1000 Mb/s 
    datas = max_rate_line.split()                       # 
    max_rate = int(datas[0])                            # 
    unit = datas[1][0]                                  # 
    return (max_rate, unit)
    
def draw_graph(start_pk_list, end_pk_list, chang_pk_list, port_types, max_value, unit_str):
    # 
    if max_value == 0 :
        return ""    
    
    str_list = []
    str_list.append("MAX = %i%s\n"% (max_value, unit_str))
    
    measure = max_value / 10
    i = max_value / measure
    while i > 0 :
        # 
        str_list.append(print_mark(i, start_pk_list, end_pk_list, chang_pk_list, unit_str, measure))
        i = i-1

    # 
    str_list.append(print_port(port_types, unit_str))

    # 
    str_list.append(print_x_label(len(chang_pk_list), unit_str))
    return ''.join(str_list)
    
def print_mark(i, start_pk_list, end_pk_list, chang_pk_list, unit_str, measure):        
    str_list = []
    # 
    num = i * measure

   # 
    if num >= 1000 :
        str_list.append("%i%s "%(num, unit_str))
    elif num >= 100 :
        str_list.append(" %i%s "%(num, unit_str))
    elif num >= 10 :
        str_list.append("  %i%s "%(num, unit_str))
    else :
        str_list.append("   %i%s "%(num, unit_str))

    # 
    for i, change_pk in enumerate(chang_pk_list):
        display_pk = 0
        if change_pk > 0 :
            display_pk = end_pk_list[i]
            if(display_pk >= num) :
                if(start_pk_list[i] >= num) :
                    str_list.append("# ")
                else :
                    str_list.append("+ ")
            else :
                str_list.append("  ")
        else :
            display_pk = (-1 * change_pk)+ end_pk_list[i]
            if(display_pk >= num) :
                if(end_pk_list[i] >= num) :
                    str_list.append("# ")
                else :
                    str_list.append("- ")
            else :
                str_list.append("  ")
    str_list.append("\n")
    return ''.join(str_list)

def print_port(port_types, unit_str):       # 
    str_list = []

    # 
    str_list.append("   0")
    str_list.append(unit_str)
    str_list.append(" ")

    #port 
    for port in port_types:
        str_list.append(port[0])
        str_list.append(" ")
    str_list.append("\n")
    return ''.join(str_list)

def print_x_label(largest_value, unit_str) :    # 
    str_list = []
    i = 1
    
    # 
    # 
    str_list.append("     ")
    str_list.append(" "* len(unit_str))
    
    while i <= largest_value :
        if i < 10 :
            str_list.append("%i " % i)      # 
        else :
            str_list.append("%i "%(i/10))   # 
        i = i + 1
    str_list.append("\n")
    str_list.append("      ")
    i = 1
    while i <= largest_value :
        if i < 10 :
            str_list.append("  ")           # 
        elif i < 20 :
            str_list.append("%i " % (i%10))
        else :
            str_list.append("%i " % (i%20))
        i = i + 1
    str_list.append("\n")
    return ''.join(str_list)

if __name__ == "__main__":
    print "data."
    interface_num = input()
    seconds = input()
    minutes = input()
    end_time = datetime.datetime.now() + datetime.timedelta(minutes = minutes)

    cnt = 1
    while True :
        (max_rate, unit) = get_max_rate()
        
        start_time = datetime.datetime.now()
        (port_types,start_input_pks, end_input_pks, change_input_pks,
            start_output_pks, end_output_pks, change_output_pks) = get_rate_change(
                interface_num, get_byte_num(unit), seconds)

        print cnt, "data time:", start_time, "~", datetime.datetime.now()

        # 그래프 작성
        title = "Input Rate(bps)"
        print " " * (interface_num -len(title)/2 + 5), title
        print draw_graph(
            start_input_pks, end_input_pks, change_input_pks, port_types, max_rate, unit)

        title = "Output Rate(bps)"
        print " " * (interface_num -len(title)/2 + 5), title
        print draw_graph(
            start_output_pks,end_output_pks, change_output_pks, port_types, max_rate, unit)
        if datetime.datetime.now() >= end_time :
            break

        cnt = cnt + 1
