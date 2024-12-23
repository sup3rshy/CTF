#!/usr/bin/python3
from Crypto.Cipher import AES 
from pwn import * 

key = bytes.fromhex('61 5F 6D 65 72 72 79 5F 63 68 72 69 73 74 6D 61 73 5F 66 6F 72 5F 79 6F 75 EF 91 5F CC 9C 9D E8 00 AF F4 EF 81 73 DB 99 8E F2 2C BD F6 FC AD 55 D2 83 78 6F E8 22 2E E5 87 E8 8D DA 0A 06 9B 56 43 84 F4 B7 EB B5 78 59 E2 39 36 B7 F3 FE 23 96 52 74 16 AE 4C 58 72 8D F8 0F DC 86 3A 13 BA A4 DF D8 2A 8C 21 9A 13 4F D7 73 EE 05 E1 9B 2B 9C 88 19 94 F7 1A B2 0A 2E 53 C5 6A 20 A2 97 88 B4 65 2A E4 66 B1 84 B1 CF FA 39 9D 25 38 E0 8B 97 0B 6B 25 E1 B7 A9 88 50 3D 96 75 6C 36 8C 12 C4 A3 CC B5 8F E1 9B 2C 3E 18 EA F0 09 DF AF 43 C9 8E 04 CC B9 A5 B8 88 DE 7D 06 74 3D 51 9C 9D 58 03 49 76 6D 51 DC E6 35 98 88 0A DA 05 3D 30 82 04 78 3B 44 BF 55 E4 A6 1C BC 1C 92 CB 4D 60 FA A7 60 43 3C 9D 01 5D 73 BE 99 79 66 37 01 CC 9D C0 2B BD D0 0F 0B 66 DD 2A A8 65 B4 EF 69 1C 38 C7 51 F0 65 5E F0 50 3C F8 9E DB ED EC F7 95 BD 30 C6 5F 00 00 00 00 00 11 04 00 00 00 00 00 00 69 6E 70 75 74 20 70 61 73 73 77 6F 72 64')
cmp_arr = bytes.fromhex('37 A6 B2 27 AA BE DA 06 D8 0F 4B 36 49 95 88 32 75 80 66 A2 D1 EA 68 E2 0E 00 00 00 00 00 00 00')[:25]
cmp_arr = bytearray(cmp_arr)
sbox = bytearray(bytes.fromhex('63 7C 77 7B F2 6B 6F C5 30 01 67 2B FE D7 AB 76 CA 82 C9 7D FA 59 47 F0 AD D4 A2 AF 9C A4 72 C0 B7 FD 93 26 36 3F F7 CC 34 A5 E5 F1 71 D8 31 15 04 C7 23 C3 18 96 05 9A 07 12 80 E2 EB 27 B2 75 09 83 2C 1A 1B 6E 5A A0 52 3B D6 B3 29 E3 2F 84 53 D1 00 ED 20 FC B1 5B 6A CB BE 39 4A 4C 58 CF D0 EF AA FB 43 4D 33 85 45 F9 02 7F 50 3C 9F A8 51 A3 40 8F 92 9D 38 F5 BC B6 DA 21 10 FF F3 D2 CD 0C 13 EC 5F 97 44 17 C4 A7 7E 3D 64 5D 19 73 60 81 4F DC 22 2A 90 88 46 EE B8 14 DE 5E 0B DB E0 32 3A 0A 49 06 24 5C C2 D3 AC 62 91 95 E4 79 E7 C8 37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08 BA 78 25 2E 1C A6 B4 C6 E8 DD 74 1F 4B BD 8B 8A 70 3E B5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E E1 F8 98 11 69 D9 8E 94 9B 1E 87 E9 CE 55 28 DF 8C A1 89 0D BF E6 42 68 41 99 2D 0F B0 54 BB 16'))
sbox_inv = [0] * 256
for i in range(len(sbox)):
    sbox_inv[sbox[i]] = i 

def rev_func1():
    for i in range(25):
        cmp_arr[i] = sbox_inv[cmp_arr[i]]
        
def rev_func2():
    for i in range(5):
        for j in range(i):
            v1 = cmp_arr[i]    
            v2 = cmp_arr[i + 5]
            v3 = cmp_arr[i + 10]
            v4 = cmp_arr[i + 15]
            v5 = cmp_arr[i + 20]
            cmp_arr[i] = v5 
            cmp_arr[i + 5] = v1 
            cmp_arr[i + 10] = v2 
            cmp_arr[i + 15] = v3 
            cmp_arr[i + 20] = v4 
    
def rev_func3(idx):
    for i in range(25):
        cmp_arr[i] ^= key[25 * idx + i]

for i in range(0xa, 0, -1):
    rev_func3(i)
    rev_func2()
    rev_func1()

rev_func3(0)
print(''.join(chr(x) for x in cmp_arr))
