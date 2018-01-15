lst = []
while True:
    try:
        n, m = [int(i) for i in raw_input().strip().split(' ')]
        n = n + m
        lst.append(n)
    except:
        break

for i in lst:
    print i


