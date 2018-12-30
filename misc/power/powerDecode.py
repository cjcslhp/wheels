import sys

def powerDecode(m):
	return "".join([chr(ord('A')+sum(2**int(j) for j in i)-1) for i in m.split(',')])

print(powerDecode(sys.argv[1]))