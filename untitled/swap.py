import sys
def get_pos(n, list, x):
    for i in range(n):
        if list[i] == x:
            return i


def run(list, n):
    a = []
    for i in range(n):
        a[i] = list[i]
    count = 0
    pos = 0

    for i in range(n):
        if i+1 !=a[i]:
            pos = get_pos(a, i+1, n)
            a[i],a[pos] = a[pos],a[i]
            count+=1


    return count

l = []
for line in sys.stdin:
    l.append(line)

print(l)