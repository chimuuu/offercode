# env/bin/python
# coding:utf-8

# 排序算法之直接插入（稳定算法） 时间复杂度为 n^2

class Solution:
	# 插入排序
	def insert(self, alist):
		# 循环查找
		for index in range(1, len(alist)):
			cur = alist[index]
			position = index
			
			# 查找交换
			while position > 0 and alist[position - 1] > cur:
				alist[position] = alist[position - 1]
				position -= 1
			alist[position] = cur
		
		return alist

	
alist = [54,26,93,17,77,31,44,55,20]
a = Solution()
print a.insert(alist)
				
