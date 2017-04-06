# -*- coding:utf-8 -*-

class Solution:
	def NumberOf1(self, n):
        # write code here
		count = 0
		flag = 1

		for i in range(32):
			if n & flag:
				count += 1
			flag = flag << 1
			print bin(flag)
		return count


if __name__ == '__main__':

 	a = Solution()
 	print a.NumberOf1(3)           