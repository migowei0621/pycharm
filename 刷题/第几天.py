#!  -*- coding:UTF-8-*
from datetime import datetime

def Leap(year):
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
    pass


def DateNumber(year, months, days):
    day = 0
    month = 1
    if Leap(year):
        L1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in L1:
            if month < months:
                day += i
                month += 1
        return day
    else:
        L1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in L1:
            if month < months:
                day += i
                month += 1
        day += days
        return day


y,m,d = [int(i) for i in raw_input().strip().split(' ')]
dt = datetime(y, m, d)
dt_ =DateNumber(y,m,d)
print dt.strftime("%j")
print dt_

