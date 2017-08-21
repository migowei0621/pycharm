

#非递归
def fibon(n):
    f = []
    f.append(1)
    f.append(1)
    print(f[0])
    print(f[1])
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
        print(f[i])



def fibo(n):
    if(n<3):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# m = int(input("aaaaaa"))
#
# for i in range(1,m):
#     print(fibo(i))


fibon(10)