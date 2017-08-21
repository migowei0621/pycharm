# -*- coding:utf-8 -*-
class Solution:

    def maxInWindows(self, num, size):
        # write code here
        if size < 0:
            return []

        if len(num) < size:
            return [max(num)]
        res = []
        for i in range(0,len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res



lt =[2,3,4,5,6,7,8,9]
l = Solution()
print(l.maxInWindows(num=lt, size=3))
