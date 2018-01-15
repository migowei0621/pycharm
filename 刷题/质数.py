n = int(input())
lst = []
lst.append(2)
for i in range(3,1000+1):
    flag = 0
    for j in range(2,1000):
        if i==j:
            continue
        if i % j == 0:
            flag = 1
            break
    if flag==0:
        lst.append(i)
print lst[:n-1]