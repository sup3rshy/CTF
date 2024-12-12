#!/usr/bin/python3 
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from pwn import * 

mp = {}
def disassemble_code(binary_code) -> None:
    disassembler = Cs(CS_ARCH_X86, CS_MODE_64)
    
    for instruction in disassembler.disasm(binary_code, 0x1224000):
    	mp[f'0x{instruction.address:07x}'] = f'{instruction.mnemonic} {instruction.op_str}'
        # print(f"0x{instruction.address:08x}: {instruction.mnemonic} {instruction.op_str}")
    return None


opcode = open("opcode", "rb").read()
disassemble_code(opcode)
chain = open("chain", "rb").read()
for i in range(len(chain) // 8):
	x = hex(u64(chain[8 * i: 8 * i + 8]))
	print(hex(0x1225000 + 8 * i), end = ": ")
	print(x, end = "")
	if x in mp:
		print(':', end = "")
		idx = u64(chain[8 * i: 8 * i + 8])
		while True:
			if hex(idx) in mp:
				asm_code = mp[hex(idx)]
				print(f' {asm_code};', end = "")
				if "ret" in asm_code:
					break
			idx += 1 
		print()
	else:
		value = u64(chain[8 * i: 8 * i + 8])
		print()
