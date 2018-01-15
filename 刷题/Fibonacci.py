

# 非递归
# def fibon(n):
#     f = []
#     f.append(1)
#     f.append(1)
#     print(f[0])
#     print(f[1])
#     for i in range(2,n):
#         f.append(f[i-1]+f[i-2])
#         print(f[i])
#
#
#
# def fibo(n):
#     if(n<3):
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)


# m = int(input("aaaaaa"))
#
# for i in range(1,m):
#     print(fibo(i))


# fibon(10)

# num = [0,1,2]
# for i in range(5):
#     num.append(num[-1] + num[-2])
#     print(num[i])
#
# for i in num:
#     print(i)


def fibonacci(m):
    f = []
    f.append(1)
    f.append(2)
    for i in range(2,m):
        f.append(f[i-1]+f[i-2])
    return f[m]

if __name__=='main':
    n = int(input())
    for i in range(n):
        m = input()
        re = fibonacci(m)
        print re