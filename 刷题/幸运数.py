n = long(input())
m = n
print n%10e9
num = []
lst = []
count = 0
while(m):
    num.append(m%10)
    m = m/10
    count+=1


for i in range(-1,-len(num)-1,-1):
    lst.append(num[i])


