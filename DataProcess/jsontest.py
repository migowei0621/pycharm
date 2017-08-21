import json as js

# f = open("/Users/migowei/Documents/实验数据/road_info.json")
# a= []
# a=js.load(f)
# print(a[0])
# print(a[0]['from'])

map = {}

data = ['a,1','b,2','c,3','a,4']

# for i in data:
#     key = i.split(',')[0]
#     value = i.split(',')[1]
#     if key not in map.keys():
#         map[key] = [value]
#     else:
#         map[key].append(value)
#
# for i in map:
#     print('i:'+str(map[i]))


import os

pathdir = os.listdir("/Users/migowei/Documents/实验数据/C")
all_file = []
for ech in pathdir:
     f = os.path.join("/Users/migowei/Documents/实验数据/C",ech)
     all_file.append(f)


for i in all_file[:31]:
    print(i)


