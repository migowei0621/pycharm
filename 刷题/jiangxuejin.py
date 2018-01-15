import sys
all = []
def solution(n,r,avg,lista, listb):
    nn = n*avg
    rest = nn - sum(lista)
    if rest <=0:
        return 0
    num =0
    j = sorted(range(n),key = lambda k:listb[k])
    for u in j :
        if(lista[u]<r and rest<=r-lista[u]):
            num = num + listb[u]*rest
            return num
        else:
            num = num + listb[u]*(r - listb[u])
            rest = rest - (r - lista[u])

for line in sys.stdin:
    all.append(line.strip())

i = 0
while i < len(all):
    n,r,avg = [int(x) for x in all[i].split(' ')]
    i +=1
    j=0
    A = []
    B = []
    while j<n:
        a,b =[int(x) for x in all[i].split(' ')]
        A.append(a)
        B.append(b)
        i +=1
        j +=1
    print(solution(n,r,avg,A,B))