# -*- coding:utf-8 -*-

'''
面试7：
	用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, node):
        # write code here
		self.stack1.append(node)

	def pop(self):
        # return xx
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			return []
		elif len(self.stack2) != 0:
			return self.stack2.pop()

		elif len(self.stack2) == 0:
			while len(self.stack1) > 0:
				self.stack2.append(self.stack1.pop())
			return self.stack2.pop()

P = Solution()
P.push(1)
P.push(2)
P.push(3)
print(P.pop())
print(P.pop())
P.push(4)
print(P.pop())
P.push(5)
print(P.pop())
print(P.pop())
