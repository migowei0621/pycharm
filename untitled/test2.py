n = int(input())
m = input()
num =[]
for i in range(n):
    num.append(int(m.split(" ")[i]))
new_num = []
conum = []
count = 0;
for i in num:
    if i not in new_num:
        new_num.append(i)
    elif i not in conum:
        conum.append(i)
        count = count + 1
count = n - count
new_num = sorted(new_num)
print(int(count))
# line = str(new_num)
l = [str(i) for i in new_num]
line =" ".join(l)
# line = line.replace(","," ").strip('[').strip(']')
print(line)