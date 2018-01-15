n = int(input())

lst = []
lst.append(1)
lst.append(1)
lst.append(1)

for i in range(3,n):
    lst.append(lst[i-1]+lst[i-3])
print lst[n-1]
