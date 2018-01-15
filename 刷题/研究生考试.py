n = int(input())
for i in range(n):
    line = [int(s) for s in raw_input().split(" ")]
    sum = line[0]+line[1]+line[2]+line[3]
    if line[0]>=60 and line[1]>=60 and line[2]>=90 and line[3]>=90 and sum>=310:
        if sum >= 350:
            print "Gongfei"
        else:
            print "Zifei"
    else:
        print "Fail"
