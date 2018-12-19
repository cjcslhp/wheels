import gmpy


n = int(input("n:"))
c1 = int(input("c1:"))
c2 = int(input("c2:"))
e1 = int(input("e1:"))
e2 = int(input("e2:"))

_, s1, s2 = gmpy.gcdext(e1, e2)

if s1 < 0:
    s1 = - s1
    c1 = gmpy.invert(c1, n)
elif s2 < 0:
    s2 = - s2
    c2 = gmpy.invert(c2, n)

m = (pow(c1,s1,n)*pow(c2,s2,n)) % n

print(m)