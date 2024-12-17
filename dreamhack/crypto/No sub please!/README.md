Ngồi test một chút thì AES without sub bytes nó có những tính chất này:
- enc[a ^ b] ^ enc[0] = enc[a] ^ enc[b]
- dec[a ^ b] ^ dec[0] = dec[a] ^ dec[b]

Đề bài nó cho mình sẵn enc(secret), nhưng nó không cho mình decrypt(secret). 
Với tính chất trên thì mình sẽ tính dec(secret) gián tiếp, cho tmp là 16 bytes bất kì.
dec[enc(secret) ^ enc(tmp)] ^ dec[0] = dec[enc(secret)] ^ dec[enc(tmp)] 
Tính ba cái trên, rồi là có secret rồi :D 
