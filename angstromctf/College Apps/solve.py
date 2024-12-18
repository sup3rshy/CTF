#!/usr/bin/python3
from pwn import * 
from ctypes import * 

txt = open("admissions-database.txt", "r").read().split(' ')[:-1]
arr = []
idx = 0
for i in range(len(txt)):
    x = txt[i].split(':')
    if len(x) < 2:
        continue
    x = int(x[1], 8)
    x ^= 0x4A72B18C
    if ((x & 0xff000000) == 0xbc000000) and ((x & 0xff) == len(arr)):
        arr.append((x >> 16) & 0xff)

print(bytes(arr))
while arr[-1] != ord('}'):
    for i in range(len(txt)):
        x = txt[i].split(':')
        if len(x) < 2:
            continue
        x = int(x[1], 8)
        x ^= 0x4A72B18C
        if ((x & 0xff000000) == 0xbc000000) and ((x & 0xff) == len(arr)):
            arr.append((x >> 16) & 0xff)
    print(bytes(arr))
# actf{now_fork_over_your_100k_annual_tuition}
