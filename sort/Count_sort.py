# env/bin/python
# coding:utf-8

# 排序算法之计数排序,稳定排序) 时间复杂度为 O(n+k)

# 假设前提：n个输入元素中的每一个都是在0到k区间内的一个整数，其中k为某个整数
# 基本思想：对每一个输入元素x，确定小于x的元素个数。利用这一信息，就可以直接把x放到它
# 输出数组中的位置上了。例如：如果有17个元素小于x，则x就应该放在第18个输出位置上。
# 当有几个元素相同时，这一方案要略作修改。


class Solution:
	# 插入排序
	def Count_sort(self, alist):
		n = len(alist)
		blist = [None] * n
		for i in range(n):
			p = 0
			q = 0
			for j in range(n):
				if alist[j] < alist[i]:
					p += 1
				elif alist[j] == alist[i]:
					q += 1
			for k in range(p, p + q):
				blist[k] = alist[i]
				
		return blist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.Count_sort(alist)

