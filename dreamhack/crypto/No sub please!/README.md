Ngồi test một chút thì AES without sub bytes nó có những tính chất này:
- enc[a ^ b] ^ enc[0] = enc[a] ^ enc[b]
- dec[a ^ b] ^ dec[0] = dec[a] ^ dec[b]
