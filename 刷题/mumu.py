n =  int(input())
lstA = []
lstB = []
for i in range(n):
    lstA.append(int(raw_input()))
    lstB.append(0)
for i in range(-1,-n-1,-1):
    print i
    if i == -1:
        lstB[i]=lstA[i]
        # print lstB
    else:
        lstB[i]=lstA[i]+lstA[i+1]

print lstB
