
#AC
s,k = [i for i in raw_input().strip().split(' ')]
lst = list(s)
k = int(k)
m = 2*k
index = 0
result = []
while index <= len(lst):
    l = list(reversed(lst[index:index+k]))
    result.append(''.join(l))
    result.append(''.join(lst[index+k:index+m]))
    index += m
print ''.join(result)