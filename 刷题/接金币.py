# def func():
#     while 1:
#         initVal = raw_input().split()
#         n = int(initVal[0])
#         if n == 0:
#             return
#         x = []
#         t = []
#         for i in range(1, 2 * n, 2):
#             x.append(int(initVal[i]))
#             t.append(int(initVal[i + 1]))
#         dp = [([0] * 11) for i in range(2)]
#         print dp
#         gold = [([0] * 11) for i in range(max(t) + 1)]
#         maxDP = -1
#         maxT = max(t)
#         for i in range(n):
#             gold[t[i]][x[i]] += 1
#         k = 0
#         res = 0
#         for i in range(1, maxT + 1):
#             for j in range(11):
#                 if abs(j - 5) <= i:
#                     left = -1
#                     right = -1
#                     if j > 0:
#                         left = dp[1 - k][j - 1]
#                     if j < 10:
#                         right = dp[1 - k][j + 1]
#                     maxDP = max(dp[1 - k][j], left, right)
#                     dp[k][j] = maxDP + gold[i][j]
#                     res = max(res, dp[k][j])
#             k = 1 - k
#         print res
#
# if __name__ == '__main__':
#     func()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
y =[]
y.append(input())
n = y[0]
for i in range(n):
    line = [int(s) for s in raw_input().split()]
    y.append(line[0])
    y.append(line[1])

x=[]
T=[]
for p in range(1, n + 1):
    x.append(y[2*p - 1])
    T.append(y[2*p])
M=[]
for i in range(max(T)):
    k=[]
    for j in range(n):
        if T[j]==i+1:
            k.append(x[j])
    M.append(k)


left_flag=-1
right_flag=+1
keep=0
print M
site=5
count=0

for i in range(max(T)):
    for j in M[i]:
        #print i,site
        print j,site,site+i,site-i

        if j==site:
            site=site+keep
            count=count+1
            break
        elif j==site+1:
            site=site+right_flag
            count = count + 1
            break
        elif j==site-1:
            site = site + left_flag
            count = count + 1
            break

        count=count
print count
