#!/usr/bin/python3
from pwn import * 

tmp = b'\x00' * 16

# p = process(['python3', 'chall.py'])
p = remote('host3.dreamhack.games', 24535)
p.recvuntil(b'enc(secret) = ')
enc_secret = bytearray(bytes.fromhex(p.recvline()[:-1].decode()))
arr = []
for i in range(4):
    tmp = bytearray(b'\x00' * 16)
    tmp[i * 4 : i * 4 + 4] = enc_secret[i * 4 : i * 4 + 4]
    p.sendlineafter(b'decrypt: ', b'2')
    p.sendlineafter(b'hex: ', tmp.hex())
    p.recvuntil(b'dec(ciphertext) = ')
    arr.append(bytes.fromhex(p.recvline()[:-1].decode())[i * 4 : i * 4 +4])

secret = b''
for x in arr:
    secret += x
p.sendlineafter(b'decrypt: ', b'1')
p.sendlineafter(b'hex: ', secret.hex())

p.interactive()
