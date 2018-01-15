
class Node:
    def __init__(self):
        self.x =0

# a = [[0 for i in range(51)] for j in range(51)]
a = []
next = [[0,1],[1,0],[0,-1],[-1,0]]

n,m = [int(i) for i in raw_input().strip().split(' ')]

for i in range(n):
    a.append([int(j) for j in raw_input().strip().split(' ')])

startx, starty = [int(i) for i in raw_input().strip().split(' ')]

head = 1
tail = 1

a = Node()

#python struct 怎么实现？？ 还是用c吧




