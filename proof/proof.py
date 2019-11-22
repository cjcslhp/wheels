from pwn import *
from hashlib import sha1,sha256,md5

IP, PORT = ip,port

def force(msg):
    
    if msg.startswith("md5"):
        hasher, post, tar = md5, msg[9:-37], msg[-32:]
    elif msg.startswith("sha1"):
        hasher, post, tar = sha1, msg[10:-45], msg[-40:]
    else:
        hasher, post, tar = sha256, msg[12:-69], msg[-64:]
        
    return iters.bruteforce(lambda x:hasher(x+post).hexdigest()==tar, string.ascii_letters+string.digits, 4)

c = connect(IP, PORT)

for i in range(1):
    c.sendline(force(c.recvuntil("XXXX:").split("\n")[-2]))

c.interactive()