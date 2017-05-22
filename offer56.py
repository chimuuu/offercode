# -*- coding:UTF-8 -*-
'''
题目描述
一个链表中包含环，请找出该链表的环的入口结点。 
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def meeting_ndoe(self, pHead):
        # 查找相遇的点
        if not pHead:
            return None
        pslow = pHead.next
        if not pslow:
            return None
        pfast = pslow.next
        while pfast:
            if pslow == pfast:
                return pslow
            pslow = pslow.next
            pfast = pfast.next.next
        return None

    def EntryNodeOfLoop(self, pHead):
        '''
        1 找到环 meeting_node
        2 计算环中结点的个数
        3 根据环结点设置快指针初始
        4 快慢指针相遇
        '''
        meetnode = self.meeting_ndoe(pHead)
        # 计算环中结点数，遍历相等时则为结点数
        pcount = 1
        if not meetnode:
            return None
        pnode = meetnode
        while pnode.next != meetnode:
            pcount += 1
            pnode = pnode.next
        # pnode1 = pcount + x
        # pnode2 = x
        # x 为头结点到入口的距离
        pnode1 = pHead
        for i in range(pcount):
            pnode1 = pnode1.next
        pnode2 = pHead
        while pnode1 != pnode2:
            pnode2 = pnode2.next
            pnode1 = pnode1.next
        return pnode1


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
# node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3
# node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)
