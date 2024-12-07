#!/usr/bin/python3 
from z3 import * 

cmp = [91, 55, 1, 36, 227, 244, 135, 156, 227, 212, 71, 182, 246, 126, 195, 86, 117, 38, 247, 116, 194, 7, 150, 115, 231, 244, 53, 17, 246, 231, 164, 1, 81, 230, 133, 229, 82, 183, 16, 18, 24, 18, 2, 8, 23, 18, 194, 247]

a = cmp
    
def do_func2():
    for i in range(0, 48, 2):
        v1 = (a[i] & 0xAA) | (a[i + 1] & 0x55)
        a[i] = (a[i] & 0x55) | (a[i + 1] & 0xAA)
        a[i + 1] = v1 
        
def rev_func2():
    for i in range(0, 48, 2):
        v1 = a[i + 1] 
        a[i + 1] = (v1 & 0x55) | (a[i] & 0xaa)
        a[i] = (a[i] & 0x55) | (v1 & 0xaa)
        
def do_func3():
    for i in range(0, 48, 4):
        v2 = (a[i + 1] << 24) | (a[i] << 16) | (a[i + 2]) | (a[i + 3] << 8)
        v3 = (v2 >> 12) | (v2 << 20)
        a[i] = v3
        v3 >>= 8 
        a[i + 1] = v3 
        v3 >>= 8 
        a[i + 2] = v3 
        v3 >>= 8 
        a[i + 3] = v3 

def rev_func3():
    for i in range(0, 48, 4):
        v3 = (a[i + 3] << 24) | (a[i + 2] << 16) | (a[i + 1] << 8) | (a[i])
        v2 = (v3 << 12) | (v3 >> 20)
        a[i + 2] = v2 & 0xff 
        a[i + 1] = (v2 >> 24) & 0xff 
        a[i] = (v2 >> 16) & 0xff 
        a[i + 3] = (v2 >> 8) & 0xff
        
rev_func3()
rev_func2()
# flag[2] = flag[2] + flag[12]
# flag[3] = flag[3] ^ flag[40]
# flag[8] = flag[8] ^ flag[5]
# flag[13] = flag[13] + flag[0] 
# flag[7] = flag[7] + flag[1]
# flag[16] = flag[16] + flag[22]
# flag[31] = flag[31] ^ flag[37]
# flag[42] = flag[42] + flag[9] 
# flag[46] = flag[46] ^ flag[25]
# flag[14] = flag[14] ^ flag[27]
# flag[18] = flag[18] ^ flag[33] 
# flag[6] = flag[6] + flag[11]
# flag[43] = flag[43] + flag[36]
# flag[23] = flag[23] ^ flag[28]
# flag[24] = flag[24] ^ flag[47] 
# flag[34] = flag[34] ^ flag[4] 
# flag[35] = flag[35] ^ flag[17]

a[35] ^= a[17] 
a[34] ^= a[4] 
a[24] ^= a[47]
a[23] ^= a[28]
a[43] -= a[36] 
a[6] -= a[11] 
a[18] ^= a[33] 
a[14] ^= a[27] 
a[46] ^= a[25]
a[42] -= a[9]
a[31] ^= a[37]
a[16] -= a[22]
a[7] -= a[1]
a[13] -= a[0]
a[8] ^= a[5]
a[3] ^= a[40]
a[2] -= a[12]
print(''.join(chr(x) for x in a))
