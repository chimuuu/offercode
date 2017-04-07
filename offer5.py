# -*- coding:utf-8 -*-

'''
输入一个链表，从尾到头打印链表每个节点的值。
'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        if pHead.val == None:
            return
        l = []

        while pHead:
            l.insert(0, pHead.val)
            pHead = pHead.next
        return l



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

S = Solution()
print S.ReverseList(node1)