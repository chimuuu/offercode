# -*- coding:utf-8 -*-
# 
'''
面试27：二叉树搜索与双向链表

题目描述
	输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
	要求不能创建任何新的结点，只能调整树中结点指针的指向。 

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        # 
        # 做中序遍历
        if not pRootOfTree or (not pRootOfTree.left and not pRootOfTree.right):
        	return pRootOfTree

       	# 递归处理左子树
        self.Convert(pRootOfTree.left)
        lt = pRootOfTree.left
        if lt:
        	while lt.right:
        		lt = lt.right
        	pRootOfTree.left, lt.right = lt, pRootOfTree	# 修改当前根节点指针

       	# 递归处理右子树
       	self.Convert(pRootOfTree.right)
       	rt = pRootOfTree.right
       	if rt:
       		while rt.left:
       			rt = rt.left
       		pRootOfTree.right, rt.left = rt, pRootOfTree

       	# 最左的结点是双链表的第一个结点
       	while pRootOfTree.left:
       		pRootOfTree = pRootOfTree.left
       	return pRootOfTree