# -*- coding:utf-8 -*-

'''
不用加减乘除做加法
'''

class Solution:
    def Add(self, num1, num2):
        # write code here     
        while num2 != 0:
        	Sum = num1^num2
        	Carry = (num1&num2) << 1
        	num1 = Sum
        	num2 = Carry
      	return num1

    def Add2(self, num1, num2):
    	return sum([num1, num2])

n = Solution()
print(n.Add(4,5))
print(n.Add2(4,5))