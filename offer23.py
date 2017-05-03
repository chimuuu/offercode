# coding:utf-8

'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。 
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        queue = []
        if not root:
            return []

        result = []
        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result
# from collections import deque		
# class Solution:
#     # 返回从上到下每个节点值列表，例：[1,2,3]
# 	def PrintFromTopToBottom(self, root):
#         # write code here
# 		if not root:
# 			return []

#         node_queue = deque()
#         node_queue.append(root)
#         ret = []

#         while node_queue:
#         	first_node = node_queue.popleft()	# 队首出列
#         	ret.append(first_node.val)

#         	if first_node.left:
#         		node_queue.append(first_node.left)
#         	if first_node.right:
#         		node_queue.append(first_node.right)
		# return ret