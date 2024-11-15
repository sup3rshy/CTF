#!/usr/bin/python3 
from Crypto.Cipher import AES
from ctypes import CDLL
import datetime 

libc = CDLL('libc.so.6')

def gen_random_bytes(seed, size):
    libc.srand(seed)
    ans = []
    for i in range(size):
        ans.append(libc.rand() & 0xff)
    return bytearray(ans)

time = datetime.datetime(2024, 10, 24, 7, 59, 4)
time = round(time.timestamp())
key = gen_random_bytes(time, 32)
iv = gen_random_bytes(time, 16)
enc = open("flag.txt.enc", "rb").read()
cipher = AES.new(key, AES.MODE_CBC, iv)
print(cipher.decrypt(enc).decode())
