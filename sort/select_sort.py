# env/bin/python
# coding:utf-8

# 直接选择排序（递减增量排序算法）（不稳定排序）
# 基本思想是：
# 首先在所有记录中选出序码最小的记录，把它与第1个记录交换，
# 然后在其余的记录内选出排序码最小的记录，与第2个记录交换......依次类推，直到所有记录排完为止
# 时间复杂度为O(n^(2)).
#
class Solution:
	# 直接选择排序
	def Select_Sort(self, alist):
		# 选择排序
		count = len(alist)
		for i in range(0, count):
			min = i
			for j in range(i + 1, count):
				if alist[min] > alist[j]:
					min = j
			alist[min], alist[i] = alist[i], alist[min]
		return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.Select_Sort(alist)

