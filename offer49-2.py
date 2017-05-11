# -*- coding:utf-8 -*-
'''
题目描述
	请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
	例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
	但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。 
'''
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
        	float(s)
        	return True
        except:
        	return False

    # 正则方法

    def isNumeric_re(self, s):
    	result = re.match(r'[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$',s)
    	
    	if result:
    		# print result
    		return True
    	return False

A = Solution()
example = ["+100","5e2","-123","3.1416","-1E-16","12e","1a3.14","1.2.3","+-5","12e+4.3"]
for i in example:
	print(A.isNumeric(i))
	print(A.isNumeric_re(i))