# -*- coding:utf-8 -*-

'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。 
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):
        # write code here
        if not self.stack_min:
        	self.stack_min.append(node)
       	else:
       		if self.min() <= node:
       			self.stack_min.append(self.min())
       		else:
       			self.stack_min.append(node)
       	self.stack.append(node)

    def pop(self):
        # write code here
        if not self.stack:
        	return []
        else:
        	self.stack_min.pop()
        	return self.stack.pop()

    def top(self):
        # write code here
        if not self.stack:
        	return []
        return self.stack[-1]

    def min(self):
        # write code here
        if not self.stack_min:
        	return []
        else:
        	return self.stack_min[-1]