#!/bin/env python
#-*- coding: utf-8 -*-

from cli import *
import re

def get_cdp_info() :
    str = cli("show cdp neighbors detail")
    cdp_list = []

    # 
    p = re.compile("Interface: .*,")         
    interface_list = p.findall(str)         
    # 
    p = re.compile("Device ID:.*")
    device_list = p.findall(str)

    # 정규식으로 추출한 리스트를 (interface, Device ID) 튜플 형태의 리스트로 반환
    i = 0
    while i < len(interface_list):
        interface_id = interface_list[i].split(':')[1].strip()
        if interface_id.find("Ethernet1/") >= 0 :
            interface_id = interface_id.replace(",", "")
            platform_id = device_list[i].split(':')[1].strip()
            cdp_list.append((interface_id, platform_id))
        i = i + 1
    return cdp_list

def add_description(cdp_list):
    # cdp 인터페이스 리스트 개수만큼 반복해서 설명 정보를 조회합니다.
    for (interface_id, platform_id) in cdp_list :
        cli("configure terminal ; interface %s ; description *auto* %s"% (interface_id, platform_id))

def show_description(cdp_list):
    for (interface_id, platform_id) in cdp_list :
        print cli("show interface %s description" % interface_id)

if __name__ == "__main__":
    cdp_list = get_cdp_info()
    add_description(cdp_list)
    show_description(cdp_list)
