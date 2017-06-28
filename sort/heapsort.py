# env/bin/python
# coding:utf-8

# 选择排序算法之堆排序（不稳定） 时间复杂度为 n^2
# 堆排序的最坏时间复杂度为O(nlog2n), 堆排序的平均性能较接近于最坏性能
# 思路
# 堆排序的关键步骤有两个：一是如何建立初始堆；
#                       二是当堆的根结点与堆的最后一个结点交换后，
#                       如何对少了一个结点后的结点序列做调整，使之重新成为堆。

class Solution:
	# 堆排序
	def adjust_heap(self, lists, i, size):
		lchild = 2 * i + 1
		rchild = 2 * i + 2
		max = i
		if i < size / 2:
			if lchild < size and lists[lchild] > lists[max]:
				max = lchild
			if rchild < size and lists[rchild] > lists[max]:
				max = rchild
			if max != i:
				lists[max], lists[i] = lists[i], lists[max]
				self.adjust_heap(lists, max, size)
	
	def build_heap(self, lists, size):
		for i in range(0, (size / 2))[::-1]:
			self.adjust_heap(lists, i, size)
	
	def heap_sort(self, lists):
		size = len(lists)
		self.build_heap(lists, size)
		for i in range(0, size)[::-1]:
			lists[0], lists[i] = lists[i], lists[0]
			self.adjust_heap(lists, 0, i)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.Heap_Sort(alist)

