k,n = [int(i) for i in raw_input().strip().split(' ')]

a = []
book = []
current = []
for i in range(10):
    book.append(0)
    a.append(-1)

def sum(lst):
    all = 0
    for i in lst:
        all += i
    return all

def eq(lst,current):
    for line in current:
        flag = 0
        for i in range(len(lst)):
            if lst[i] in line:
                flag += 1
        if flag >= len(lst):
            return True
    return False

def dfs(step):
    if step == k+1:
        if sum(a[1:k+1]) == n:
            if eq(a[1:k+1],current):
                pass
            else:
                current.append(a[1:k+1])
                print str(a[1:k+1]).strip('[').strip(']').replace(',',' ')
            return

    for i in range(1,10):
        if book[i] == 0:
            a[step] = i
            book[i] = 1
            dfs(step+1)
            book[i] = 0


if __name__ =='__main__':
    dfs(1)
    if len(current)==0:
        print None
