n = int(input())
lst = [int(i) for i in raw_input().strip().split()]


count = 0

def compute(num):
    lst = long(str(num)[0:-1])
    re = lst - long(str(num)[-1])*2
    if re % 7 == 0:
        return True
    else:
        return False
for index, pre  in enumerate(lst):
    for j in range(index+1,n):
        last = lst[j]
        new1= long(''.join((str(pre),str(last))))
        new2 =long(''.join((str(last),str(pre))))
        # if new1 % 7 == 0:
        #     count+=1
        # if new2 % 7 ==0:
        #     count+=1
        if compute(new1):
            count+=1
        if compute(new2):
            count+=1
print count