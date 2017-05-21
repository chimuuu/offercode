# -*- coding:utf-8 -*-

'''
面试57：删除链表中重复的结点
	在一个排序的链表中，
	存在重复的结点，请删除该链表中重复的结点，
	重复的结点不保留，返回链表头指针。 
	例如，链表1->2->3->3->4->4->5 处理后为 1->2->5 
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
        	return pHead

        if pHead.next.val == pHead.val:
        	pNode = pHead.next.next
        	while pNode and pNode.val == pHead.val:
        		pNode = pNode.next
        		return self.deleteDuplication(pNode)
        else:
        	pHead.next = self.deleteDuplication(pHead.next)
        	return pHead


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.deleteDuplication(node1))


