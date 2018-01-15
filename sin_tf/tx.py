n = int(input())

lst = []

for i in range(n):
    lst.append(i+1)

index = 0

while len(lst)>1:
    index +=2
    index = index %len(lst)
    del lst[index]

print(lst[0])
