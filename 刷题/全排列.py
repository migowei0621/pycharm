# global a, book ,n
n = int(input())
a = []
book = []

for i in range(n+1):
    book.append(0)
    a.append(-1)

def dfs(step):
    if step == n+1:
        print a[1:]
        return

    for i in range(1,n+1):
        if book[i] == 0:
            a[step] = i
            book[i] = 1
            dfs(step+1)
            book[i] = 0

  


if __name__ =='__main__':
    dfs(1)
