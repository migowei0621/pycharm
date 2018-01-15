lst = [int(i) for i in raw_input().strip().split(' ')]
n = lst[0]
lst = lst[1:]

del lst[-1]

min = 9999999
max = 0
for i in lst:
    if min >i:
        min = i
    if max <i:
        max = i

print("%d,%d"%(max,min))