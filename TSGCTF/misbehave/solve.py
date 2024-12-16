#!/usr/bin/python3
from pwn import * 

arr = '''
0x43475354
0x687b4654
0x33646431
0x75665f6e
0x6937636e
0x345f6e30
0x735f646e
0x5f663133
0x5f373067
0x72657630
0x37317277
0x7d33 
'''
arr = arr.split('\n')[1:-1]
flag = b''
for x in arr:
    flag += pack(int(x, 16), "all")
print(flag)
