#!/usr/bin/env bash

echo -e "Operation time and run queue confirm"
uptime

echo -e "\nCPU each usage percent"
mpstat -P ALL

echo -e "\nSort 20 processors with high memory usage"
ps aux --sort -pmem | head -n 20

echo -e "\nVirtual memory usage"
vmstat -s

echo -e "\nUsage and errors by network interface"
netstat -i

echo -e "\nDisk mout status and capacity"
netstat -s

echo -e "\nDisplay disk utilization information"
lsblk

echo -e "\n��ũ ���� ���� ǥ��"
iostat -x