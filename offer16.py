# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
from collections import deque
class Solution:
    # 返回ListNode
	def ReverseList(self, pHead):
        # write code here
		if not pHead:
			return []
        
		tmp = deque()
		while pHead:
			tmp.appendleft(pHead.val)
			pHead = pHead.next

		return tmp

node1 = ListNode(12)
node2 = ListNode(4)
node3 = ListNode(7)
node1.next = node2
node2.next = node3

S = Solution()
p = S.ReverseList(node1)
print(p)