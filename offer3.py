# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from collections import deque	# 两端可操作的序列

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        
        TTH = deque()
       	while listNode:
            TTH.appendleft(listNode.val)
            listNode = listNode.next
        return TTH
