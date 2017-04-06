# coding:utf-8

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution:
	# 初级 相对位置变化
	def reOrderArray1(self, array):
	# write code here
		if len(array) < 1:
			return
		elif len(array) == 1:
			return array

		front = 0
		rear = len(array) - 1
		while front < rear:
			# 为奇数时后移
			while array[front] & 0x1 == 1:
				front += 1
			# 为偶数时前移
			while array[rear] & 0x1 == 0:
				rear -= 1

			if front < rear:
				temp = array[front]
				array[front] = array[rear]
				array[rear] = temp
                
		return sorted(array[:front])+sorted((array[front:]))

	def reOrderArray2(self, array):
		left = [x for x in array if x & 0x1]
		right = [x for x in array if not x & 0x1]
		return left + right

s = Solution()

print s.reOrderArray1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print s.reOrderArray2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])