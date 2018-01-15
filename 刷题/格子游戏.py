n,m = [int(i) for i in raw_input().split()]

grid = []
for i in range(n):
    grid.append(int(raw_input()))

def modification(grid,i,val):
    grid[i] = val
    return grid

def add(grid,start,end):

    sum = 0
    for i in range(start-1, end):
        sum = sum + grid[i]

    print sum

def max(grid,start,end):
    max = 0
    for i in range(start-1, end):
        if max < grid[i]:
            max = grid[i]

    print max



for i in range(m):
    line = [int(s) for s in raw_input().split()]
    if line[0] == 1:
        modification(grid,line[1]-1,line[2])
    elif line[0] == 2:
        add(grid,line[1],line[2])
    elif line[0] == 3:
        max(grid,line[1],line[2])

