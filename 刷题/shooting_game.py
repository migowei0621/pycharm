import math

def rotate(monster, sin, cos):
    lst = []
    for i in monster:
        x = int(i[0]*cos - i[1]*sin)
        y = int(i[0]*sin + i[1]*cos)
        lst.append([x,y])
    return lst
def move(monster, a, direction):
    lst = []
    if direction == 0:
        for i in monster:
            x = i[0] - a
            y = i[1]
            lst.append([x,y])
    elif direction == 1:
        for i in monster:
            y = i[1] - a
            x = i[0]
            lst.append([x,y])
    elif direction == 2:
        for i in monster:
            x = i[0] - a
            y = i[1] - a
            lst.append([x,y])
    return lst

def count(monster):
    num = 0
    for i in monster:
        if i[0] == 0 or i[1] == 0:
            num += 1
    return num

n = int(input())
monster = []
x = [int(i) for i in raw_input().strip().split(' ')]
y = [int(i) for i in raw_input().strip().split(' ')]
for i in range(n):
    monster.append([x[i], y[i]])
num = count(monster)
for i in monster:
    a = move(monster, i[0],0)
    if num < count(a):
        num = count(a)
    a = move(monster,i[1],1)
    if num < count(a):
        num = count(a)

    l = math.sqrt(i[0]**2+i[1]**2)
    sin = i[0]/l
    cos = i[1]/l
    a = rotate(monster,sin,cos)
    if num <count(a):
        num = count(a)
print num

