# -*- coding:utf-8 -*-


'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
	注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # 输入为空
        if pNode == None:
        	return None

        # 如果有右子树，则找右子树的最左节点
        if pNode.right:
        	curNode = pNode.right
        	while curNode.left:
        		curNode = curNode.left
        	return curNode

        # 如果当前结点有父结点且是父结点的右子结点，
        # 则把其父节点作为下一个遍历的节点，向上回溯，
        # 直到找到父节点没有父节点并且父节点是父节点的父节点的左孩子为止
        while pNode.next:
        	if pNode.next.left == pNode:
        		return pNode.next
        	pNode = pNode.next

        return None