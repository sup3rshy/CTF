#!/usr/bin/python3
from pwn import * 

tmp = b'\x00' * 16

# p = process(['python3', 'chall.py'])
p = remote('host3.dreamhack.games', 16825)
p.recvuntil(b'enc(secret) = ')
enc_secret = bytes.fromhex(p.recvline()[:-1].decode())
p.sendlineafter(b'decrypt: ', b'1')
p.sendlineafter(b'hex: ', tmp.hex())
p.recvuntil(b'enc(plaintext) = ')
enc_tmp = bytes.fromhex(p.recvline()[:-1].decode())

p.sendlineafter(b'decrypt: ', b'2')
p.sendlineafter(b'hex: ', enc_tmp.hex())
p.recvuntil(b'dec(ciphertext) = ')
dec_tmp = bytes.fromhex(p.recvline()[:-1].decode())

p.sendlineafter(b'decrypt: ', b'2')
p.sendlineafter(b'hex: ', (b'\x00' * 16).hex())
p.recvuntil(b'dec(ciphertext) = ')
dec_0 = bytes.fromhex(p.recvline()[:-1].decode())

enc_secret_tmp = b''
for i in range(len(enc_secret)):
    enc_secret_tmp += p8(enc_secret[i] ^ enc_tmp[i])

p.sendlineafter(b'decrypt: ', b'2')
p.sendlineafter(b'hex: ', enc_secret_tmp.hex())
p.recvuntil(b'dec(ciphertext) = ')
dec_secret_tmp = bytes.fromhex(p.recvline()[:-1].decode())

dec_secret = b''
for i in range(16):
    dec_secret += p8(dec_secret_tmp[i] ^ dec_0[i] ^ dec_tmp[i])
p.sendlineafter(b'decrypt: ', b'1')
p.sendlineafter(b'hex: ', dec_secret.hex())
# p.recvuntil(b'enc(ciphertext) = ')

p.interactive()
