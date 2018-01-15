lst = [2,1]

result = []
def dfs(lst,index,aim):
    res = 0
    re = []
    if(index == len(lst)):
        if(aim==0):
            res = 1
        else:
            res = 0
            del re[:]
        return res,re
    else:
        i = 0
        while(lst[index]*i<=aim):
            a,re = dfs(lst,index+1,aim-lst[index]*i)
            res +=a
            re.append([lst[index],i])
            result.append(re)
            i+=1
        return res,re

n,re = dfs(lst,0,4)

for i in result:
    if len(i) == 2:
        print i

