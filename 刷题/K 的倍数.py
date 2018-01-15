n = int(input())
num = [int(s) for s in raw_input().split()]
k = int(input())

def all(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum
leg = 0
for index,i in enumerate(num):
    if i % k==0 and leg == 0:
        leg =1
    sub_num = []
    sub_num.append(i)
    for j in range(index+1,n):

        if (all(sub_num)+num[j])%k==0:
            sub_num.append(num[j])
            if leg < len(sub_num):
                leg = len(sub_num)
            if len == len(num):
                break
            # print sub_num
        else:
            sub_num.append(num[j])
print leg

