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

from collections import deque	
class Solution:
    # 列表
    def PrintFromTopToBottom_list(self, root):
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

    # 队列
    '''
	有误，回头调试吧

    '''
	# def PrintFromTopToBottom_deque(self, root):
	# # write code here
	# 	ret = []
	# 	if not root:
	# 		return []

	# 	node_queue = deque()
	# 	node_queue.append(root)

	# 	while node_queue:
	# 		first_node = node_queue.popleft()	# 队首出列
	# 		ret.append(first_node.val)

	# 		if first_node.left:
	# 			node_queue.append(first_node.left)
	# 		if first_node.right:
	# 			node_queue.append(first_node.right)
	# 	return ret

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.PrintFromTopToBottom_list(pNode1))
# print(S.PrintFromTopToBottom_deque(pNode1))