# !/usr/bin/env python
# coding:utf-8

# 排序算法之快速排序 （不稳定排序）时间复杂度为 0(nlogn, n^2)
# 快速排序采用了一种分治的策略，通常称其为分治法，
# 其基本思想是：将原问题分解为若干个规模更小但结构与原问题相似的子问题。递归地解这些子问题，然后将这些子问题的解组合为原问题的解。
# 快速排序的具体过程如下：
# 第一步，在待排序的n个记录中任取一个记录，以该记录的排序码为准，将所有记录分成两组，
#        第1组各记录的排序码都小于等于该排序码，第2组各记录的排序码都大于该排序码，并把该记录排在这两组中间。
# 第二步，采用同样的方法，对左边的组和右边的组进行排序，直到所有记录都排到相应的位置为止。

class Solution:
	def quick_sort(self, alist,low, high):
		# 对序列alist[low,...high]z做快速排序
		if low < high:
			pivot = self.Partition(alist, low, high)
			
			self.quick_sort(alist, low, pivot-1)
			self.quick_sort(alist, pivot+1, high)
		return alist
	
	def Partition(self, alist, low, high):
		# 取子表第一个记录作为枢轴记录
		pivot_key = alist[low]
		# 从表的两端交替向中间扫描
		
		while low < high:
			# 将比枢轴小的元素交换到底端
			while low < high and alist[high] >= pivot_key:
				high -= 1
			alist[low], alist[high] = alist[high], alist[low]
		
			# 将比枢轴大的元素交换到顶端
			while low < high and alist[low] <= pivot_key:
				low += 1
			alist[low], alist[high] = alist[high], alist[low]
		
		return low
	
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.quick_sort(alist, 0, len(alist)-1)
