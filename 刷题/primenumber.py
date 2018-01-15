
import math
n = int(input())

flag = False
count = 0
num = 0
while(count<n):
    for i in range(2,10000):
        j=2
        for j in range(2,math.sqrt(i)):
            if( i % j == 0):
                break
        if(j>math.sqrt(i)):
            count = count +1
            num = i
            if(count == n):
                break

print(num)