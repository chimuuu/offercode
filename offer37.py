# -*- coding:utf-8 -*-

'''
面试第37题
题目描述
输入两个链表，找出它们的第一个公共结点。 
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque
def iter_node(root):
	while root:
		yield root
		root = root.next

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
        	return None

        head1_deque = deque()
        head2_deque = deque()

        head1_deque = [node for node in iter_node(pHead1)]
        head2_deque = [node for node in iter_node(pHead2)]
        ret = None

        while head1_deque and head2_deque:
        	top1 = head1_deque.pop()
        	top2 = head2_deque.pop()
        	if top1.val == top2.val:
        		ret = top1
        		continue
        	else:
        		break
        return ret

