#!/usr/bin/python3 
import random
import os 
from randcrack import RandCrack
from pwn import * 

rc = RandCrack()
context.log_level = "debug"
# p = process(['python3', 'chall.py'])
p = remote('chals.bitskrieg.in', 7007)

def get_number(idx):
    p.sendlineafter(b'> ', b'0')
    p.recvuntil(b'Access Denied! You are ')
    x = int(p.recvuntil(b' ')[:-1], 10)
    x //= 2969596945
    x //= (idx ^ 195894762 ^ 322420958)
    return x 

def generate_password(i):
    password = rc.predict_getrandbits(32) * (i ^ 195894762 ^ 322420958) * 2969596945
    return password

for i in range(624):
    rc.submit(get_number(i + 1))

p.sendlineafter(b'> ', str(generate_password(625)))
p.interactive()
