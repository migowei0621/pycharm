# JSON : test json load and dump

# import json as js
# f = open("/Users/migowei/Documents/实验数据/road_info.json")
# a= []
# a=js.load(f)
# print(a[0])
# print(a[0]['from'])


# map = {}
# data = ['a,1','b,2','c,3','a,4']
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


# DIR: test for  dirfile input

# import os
# pathdir = os.listdir("/Users/migowei/Documents/实验数据/C")
# all_file = []
# for ech in pathdir:
#      f = os.path.join("/Users/migowei/Documents/实验数据/C",ech)
#      all_file.append(f)
#
#
# for i in all_file[1:2]:
#     print(i)


# from datetime import datetime,timedelta
# t1 = datetime.strptime("2015-12-01 09:15:02 111","%Y-%m-%d %H:%M:%S %f")
# t2 = datetime.strptime("2015-12-01 09:16:04 211","%Y-%m-%d %H:%M:%S %f")
# t3 = (t2-t1).total_seconds()
# print(t3)


import time
import sys

for i in range(1000000):
    sys.stdout.write('\r')
    sys.stdout.write("%s%% |%s" % (int(i % 101), int(i % 101) * '#'))
    sys.stdout.flush()
    time.sleep(0.05)

sys.stdout.write('\n')