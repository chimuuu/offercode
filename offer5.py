# -*- coding:utf-8 -*-

'''
输入一个链表，从尾到头打印链表每个节点的值。
'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    # 递归版本
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        else:
            pnode = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pnode



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