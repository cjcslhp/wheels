import base64

key = 'a2V5'
message = "ZglVjFfoHg=="

key = [ord(i) for i in base64.b64decode(key)]
message = [ord(i) for i in base64.b64decode(message)]

s = [i for i in range(256)]
t = [key[i % len(key)] for i in range(256)]
j = 0

for i in range(256):
    j = (j + s[i] + t[i]) % 256
    s[i], s[j] = s[j], s[i]

i, j = 0, 0
for m in range(len(message)):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i]
    x = s[(s[i] + s[j]) % 256]
    message[m] ^= x

cipher = base64.b64encode("".join([chr(i) for i in message]))
print(cipher)


