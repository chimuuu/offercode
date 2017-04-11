# -*- coding:utf-8 -*-

'''
面试29：数组中出现次数超过一半的数字

'''

class Solution:
	# pythoner版
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        L = len(numbers)
        num = sorted(numbers)
        if num.count(num[L/2]) > L/2:
        	return num[L/2]
        else:
        	return 0
        

numbers = [2,2,2,2,2,1,3,4,5]

A = Solution()
print A.MoreThanHalfNum_Solution(numbers)