from Crypto.Util.number import long_to_bytes
from factordb.factordb import FactorDB
from gmpy import invert


def factor(n,e,c):
    print("[*] Try factor",n)
    f = FactorDB(n)
    print("[*] Try connect")
    if f.connect().status_code != 200:
        print("[-] Connect Failed")
        return 0

    lst = f.get_factor_list()
    if len(lst) == 1:
        print("[-] Factor Failed")
        return 0

    print("[*] the factor result:",lst)
    lst = set(lst)
    tn = n
    for i in lst:
        tn = tn // i * (i-1)
    
    d = invert(e, tn)
    print("[?] Maybe success")
    print("[!] flag:",long_to_bytes(pow(c,d,n)))
    return 1

def main(n,e,c):
    if factor(n,e,c):
        go = input("[*] Continue? (y/n)")
        if go != 'y':
            print("[-] Thanks, bye~")
            return
    
    print("[*] Building~")
    print("[-] Thanks, bye~")

if __name__ == "__main__":
    n = int(open("n.txt",'r').read())
    e = int(open("e.txt",'r').read())
    c = int(open("c.txt",'r').read())
    main(n,e,c)