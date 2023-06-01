#!/bin/env python3
#-*- coding: utf-8 -*-

from subprocess import *
from xlsxwriter import *

cmd = "vmstat 1 5 | awk '{now=strftime(\"%Y-%m-%d %T \"); print now $0}'"
p = Popen(cmd, shell=True, stdout=PIPE)
#print(cmd)

(ret, err) = p.communicate()
print(type(ret))
ret= str(ret)
print(type(ret))

workbook = Workbook('vmstat.xlsx')
worksheet = workbook.add_worksheet()

# 데이터를 줄 단위로 만듭니다.
#rows = ret.split("\n")
rows = ret.split("\\")
#print(rows)
for row_idx, row in enumerate(rows) :
    print(row_idx, row)
    columns = row.split()
    #print(columns)
    for col_idx, col in enumerate(columns) :
        print('row:', row_idx, 'col:', col_idx)
        worksheet.write(row_idx, col_idx, col)

workbook.close()
