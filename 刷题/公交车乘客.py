n = int(input())
num = 0
now = 0
for i in range(n):
    line = [int(i) for i in raw_input().split(" ")]
    now = now + line[1] - line[0]
    if num < now:
        num = now
print num