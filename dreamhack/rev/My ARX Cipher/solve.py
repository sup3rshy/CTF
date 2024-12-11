#!/usr/bin/python3 
from pwn import * 
         
encrypt = open("flag.enc", "rb").read()
key = 'SuP3RSaFeK3Y'.encode()
ans = b''
for i in range(len(encrypt) // 4):
    x = (encrypt[i * 4 + 1] << 8) | (encrypt[i * 4])
    y = (encrypt[i * 4 + 3] << 8) | (encrypt[i * 4 + 2])
    v3 = x 
    v4 = y 
    v5 = 0
    for j in range(2, -1, -1):
        a1 = (key[j * 4 + 1] << 8) | key[j * 4]
        a2 = (key[j * 4 + 3] << 8) | key[j * 4 + 2]
        v5 = v4 & 0xffff
        t = v3 ^ a2 
        v4 = (t >> 7) | (t << 9)
        v4 &= 0xffff
        t = v5 ^ a1 
        t -= v4 
        t &= 0xffff
        v3 = (t >> 7) | (t << 9)
        v3 &= 0xffff
    ans += p16(v3 & 0xffff)
    ans += p16(v4 & 0xffff)
# print(encrypt)
print(ans)
