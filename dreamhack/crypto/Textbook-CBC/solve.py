#!/usr/bin/python3
from pwn import * 
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad

context.log_level = "debug"
tmp = b'\x00' * 16 

# p = process(['python3', 'challenge.py'])
p = remote('host3.dreamhack.games', 17486)
p.sendlineafter(b'Flag\n', b'1')
p.sendlineafter(b'(hex): ', tmp.hex())
enc_tmp = bytes.fromhex(p.recvline()[:-1].decode())

p.sendlineafter(b'Flag\n', b'2')
p.sendlineafter(b'(hex): ', (tmp + enc_tmp).hex())
iv = bytes.fromhex(p.recvline()[:-1].decode())[16:32]

p.sendlineafter(b'Flag\n', b'3')
p.recvuntil(b'flag = ')
flag = bytes.fromhex(p.recvline()[:-1].decode())
cipher = AES.new(iv, AES.MODE_CBC, iv)
log.info(cipher.decrypt(flag))
p.interactive()
