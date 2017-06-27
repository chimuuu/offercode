# env/bin/python
# coding:utf-8

# 希尔(Shell)排序（递减增量排序算法）（不稳定排序）
# 基本思想是：
# 先取一个小于n的整数d1作为第一个增量把文件的全部记录分成d1个组。
# 所有距离为d1的倍数的记录放在同一个组中。先在各组内进行直接插入排序；
# 然后，取得第二个增量d2<d1重复上述的分组和排序，直至所取的增量di=1，即所有记录放在同一组中进行直接插入排序为止。
# 该方法实质上是一种分组插入方法。
# 一般取d1=n/2，di+1=di/2。如果结果为偶数，则加1，保证di为奇数。
# 希尔排序是不稳定的，希尔排序的执行时间依赖于增量序列，其平均时间复杂度为O(n^(3/2)),下界为n*log2n.
#
class Solution:
	# 插入排序
	def Shell(self, alist):
		# 设定步长
		step = len(alist)/2
		while step > 0:
			for i in range(step, len(alist)):
				# 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
				while i >= step and alist[i-step] > alist[i]:
					alist[i], alist[i-step] = alist[i-step], alist[i]
					i -= step
			step = step/2
		
		return alist
			


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.Shell(alist)

