# env/bin/python
# coding:utf-8

# 排序算法之冒泡排序
# 时间复杂度为 为（n, n^2)
# 冒泡排序将被排序的记录数组R[1..n]垂直排列，每个记录R[i]看作是重量为ki的气泡。根据轻气泡不能在重气泡之下的原则，
# 从下往上扫描数组R；凡扫描到违反本原则的轻气泡，就使其向上"漂浮"。
# 如此反复进行，直到最后任何两个气泡都是轻者在上，重者在下为止

class Solution:
	def bubble(self, alist):
		#
		L = len(alist)
		for i in range(L):
			for j in range(i+1, L):
				if alist[i] > alist[j]:
					alist[i], alist[j] = alist[j], alist[i]
		return  alist
		
		
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.bubble(alist)