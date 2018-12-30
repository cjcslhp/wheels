import sys

def powerEncode(m):
    res = ""
    for cha in m:
        cha = bin(ord(cha)-ord('A')+1)[:1:-1]
        for i in range(len(cha)):
            if cha[i] == '1':
                res += str(i)

        res += ','

    return res[:-1]


print(powerEncode(sys.argv[1]))