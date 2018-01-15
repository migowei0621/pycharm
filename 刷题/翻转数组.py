# 方法1
n=int(raw_input())
a=[int(i) for i in raw_input().split()]
b=sorted(a)
rev_a = [a[i] for i in range(n) if a[i]!=b[i]]
rev_b = [b[i] for i in range(n) if a[i]!=b[i]]
rev_a.reverse()
if rev_a == rev_b:
    print 'yes'
else:
    print 'no'

#方法2
# def IsListSorted_sorted(lst):
#     return sorted(lst) == lst or sorted(lst, reverse=True) == lst
#
#
# n = int(input())
# l = list(raw_input().strip(" ").split(" "))
# l = [int(i) for i in l]
#
#
# snippet = []
# index = 0
# len1 = 0
# flagE =0
# flagS =0
# for val in l:
#     if index+1 <= n-2 and l[index] > l[index+1]:
#         flagS = index
#         flagE = index
#         while flagE+1 <= n-2 and l[flagE] > l[flagE+1]:
#             flagE += 1
#         index = flagE + 1
#         for i in range(flagS,index):
#             snippet.append(l[i])
#
#         len1 = flagE - flagS + 1
#     else:
#         index += 1
#
# if len(snippet) == 0 :
#     print "no"
# if len(snippet) > len1:
#     print "no"
# else:
#     snippet.reverse()
#     for i in snippet:
#         l[flagS] = i
#         flagS +=1
#     if IsListSorted_sorted(l):
#         print "yes"
#     else:
#         print "no"

