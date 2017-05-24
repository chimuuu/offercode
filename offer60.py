# -*- coding:utf-8 -*-

'''
面试60：多行打印二叉树
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
        	return None

        # 初始
        nodes = [pRoot]
        ret = []

        while nodes:
        	cur, nxt = [], []
        	for node in nodes:
        		cur.append(node.val)
        		if node.left:
        			nxt.append(node.left)
        		if node.right:
        			nxt.append(node.right)
        	nodes = nxt
        	ret.append(cur)
        return ret