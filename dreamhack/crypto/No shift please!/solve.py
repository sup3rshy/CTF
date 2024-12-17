#!/usr/bin/python3
from pwn import * 

tmp = b'\x00' * 16

# p = process(['python3', 'chall.py'])
p = remote('host3.dreamhack.games', 9085)
p.recvuntil(b'enc(secret) = ')
enc_secret = bytearray(bytes.fromhex(p.recvline()[:-1].decode()))
arr = []
for i in range(2):
    tmp = bytearray(b'\x00' * 16)
    tmp[i * 8 : i * 8 + 8] = enc_secret[i * 8 : i * 8 + 8]
    p.sendlineafter(b'decrypt: ', b'2')
    p.sendlineafter(b'hex: ', tmp.hex())
    p.recvuntil(b'dec(ciphertext) = ')
    arr.append(bytes.fromhex(p.recvline()[:-1].decode())[i * 8 : i * 8 + 8])

secret = b''
for x in arr:
    secret += x
p.sendlineafter(b'decrypt: ', b'1')
p.sendlineafter(b'hex: ', secret.hex())

p.interactive()
