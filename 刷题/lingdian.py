from datetime import datetime,timedelta

start = raw_input().strip()
end = raw_input().strip()

year1,mon1,day1 = start.split(' ')[0].split('/')
h1,min1,sec1 = start.split(' ')[1].split(':')
time1 = datetime(int(year1),int(mon1),int(day1),int(h1),int(min1),int(sec1))

year2,mon2,day2 = end.split(' ')[0].split('/')
h2,min2,sec2 = end.split(' ')[1].split(':')
time2 = datetime(int(year2),int(mon2),int(day2),int(h2),int(min2),int(sec2))
count_day = (time2-time1).days-1

begin = time1
count = 0
while begin+timedelta(days=1)< time2:
    if begin.weekday()==4:
        count+=1
    begin += timedelta(days=1)


print("%d,%d"%(count_day,count))


