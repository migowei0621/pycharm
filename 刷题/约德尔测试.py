


line = raw_input()

l = []
for i in line:
    if i.isalnum():
        l.append('1')
    else:
        l.append('0')

m = raw_input()
n = "".join(list(l))
count = 0
for index, i in enumerate(n):
    if i == m[index]:
        count += 1
count = float(count)
al = float(len(m))
print "%.2f%%" % (count/al*100)