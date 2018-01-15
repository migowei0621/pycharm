import re
str = raw_input()
global k
if "RED" in str:
    str = str.replace("RED","")
# r的意思是不转义，即\表示原样的\。否则有可能被视图按\d为一个字符解析转义。
# \d是0-9的数字 \D是非数字
lst = re.findall(r'\d+', str)

if len(lst)==0:
    print -1
else:
    max = 0
    lst2 = []
    for index,i in enumerate(lst):
        if max <= len(i):
            max =len(i)
            lst2.append(i)
            k = index

    m = long(lst2[0])
    for i in lst2:
        if m< long(i):
            m = long(i)
    print m
