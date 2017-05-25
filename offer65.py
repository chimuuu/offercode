# -*- coding:utf-8 -*-
'''
面试题65：滑动窗口的最大值
'''
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size <= 0:
            return []

        if len(num) < size:
            return []
        else:
            index = []
            for i in range(len(num)-size+1):
                index.append(max(num[i:i+size]))
        return index

test = [2, 3, 4, 2, 6, 2, 5, 1]
test1 = [10,14,12,11]
s = Solution()
print(s.maxInWindows(test, 3))
print(s.maxInWindows(test1, 5))