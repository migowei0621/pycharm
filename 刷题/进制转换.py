n = str(input()).strip()
m = bin(int(n))
m = m[2:]
new = m[::-1]
new = ''.join(('0b',new))
new = hex(int(new,2))
print new
