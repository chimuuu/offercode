# -*- coding:UTF-8 -*-
# 查找字符是否在一个二维数组中

# 思路：从左下角开始查找
#		行数：m = len(array) -1
#		列数：n = len(array[0])-1

class Solution:
	# arrary 二维数组
	def Find(self, targe, tarray):
		m = len(array)-1
		i = 0 

		while m >= 0 and i < len(array[0]):
			if array[m][i] > target:
				m -= 1
			elif array[m][i] < target:
				i += 1
			else:
				return True
		return False
