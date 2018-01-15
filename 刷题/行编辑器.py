

n = input()
s = []
for i in range(int(n)):
    line = raw_input()
    s.append(line)

for line in s:
    new_line = []
    for index,i in enumerate(line):
        if len(new_line) !=0:
            if i=="#":
                new_line.pop()
            elif i=="@":
                new_line=[]
            else:
                new_line.append(i)
        else:
            if i=="#":
                pass
            elif i=="@":
                pass
            else:
                new_line.append(i)
    print "".join(list(new_line))
