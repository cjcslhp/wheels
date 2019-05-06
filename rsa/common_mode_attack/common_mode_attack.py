from Crypto.Util.number import long_to_bytes
import gmpy

def common_mode_attack(n, e1, e2, c1, c2):
    print("[*] Try common mode attack")
    _, s1, s2 = gmpy.gcdext(e1, e2)
    if s1 < 0:
        s1 = - s1
        c1 = gmpy.invert(c1, n)
    elif s2 < 0:
        s2 = - s2
        c2 = gmpy.invert(c2, n)

    m = (pow(c1,s1,n)*pow(c2,s2,n)) % n
    print("[*] Maybe success")
    print("[!] flag:",long_to_bytes(m))
    return 1

def main(n,e1,e2,c1,c2):
    if common_mode_attack(n, e1, e2, c1, c2):
        print("[-] Thanks, bye~")
        return

    print("[-] Sorry, it's not easy~")
    return

if __name__ == "__main__":
    exec(open("nec.txt").read())
    main(n, e1, e2, c1, c2)