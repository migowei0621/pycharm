n = int(input())
lst  = [int(i) for i in raw_input().strip().split()]

def change(index,lst):
    if lst[index] == 1:
        lst[index] = 0
    elif lst[index] == 0:
        lst[index] = 1
    return lst

count = 0
tmp = lst[:]
if 1 not in tmp:
    print 'Alice'
while(1 in tmp):
    index = tmp.index(1)
    for j in range(index,n):
        tmp = change(j, tmp)
    count +=1



# for index,num in enumerate(tmp):
#     if 1 not in tmp:
#         count +=1
#         break
#     if num == 1:
#         for j in range(index,n):
#             tmp = change(j,tmp)
#         count += 1
#         if 1 not in tmp:
#             break

if count%2==0 and count!=0:
    print 'Bob'
elif count%2==1 and count>0:
    print 'Alice'