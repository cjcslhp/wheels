#!/usr/bin/python

def cbc_bit_attack_mul(c,m,position,target):
    l = len(position)
    r=c
    for i in range(l):
        change=position[i]-16
        tmp=chr(ord(m[position[i]])^ord(target[i])^ord(c[change]))
        r=r[0:change]+tmp+r[change+1:]
    return r

if __name__ == "__main__":
    import base64
    c = base64.b64decode(raw_input("c(base64):"))
    m = raw_input("m:")
    position = [int(i) for i in raw_input("position(exp: 1 2 3):").split()]
    target = [i for i in raw_input("target(exp: A B C)").split()]
    print(base64.b64encode(cbc_bit_attack_mul(c,m,position,target)))