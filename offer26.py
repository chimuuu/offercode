# -*- coding:utf-8 -*-

'''
题目描述
	输入一个复杂链表（每个节点中有节点值，以及两个指针，
	一个指向下一个节点，另一个特殊指针指向任意一个节点），
	返回结果为复制后复杂链表的head。
	（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空） 

方案：
	第一步：复制每个节点，将复制的每个节点连接到原始节点后面
	第二步：将复制后的链表中的复制点的randon指针连接到被复制节点random指针的后一个节点
	第三步：拆分链表，奇偶拆分成来两个

'''

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         # write code here

#         if pHead == None:
#         	return None

#         self.CloneNodes(pHead)
#         self.CloneRandomNodes(pHead)
#         return  self.CloneRandomNodes(pHead)

#     # 第一步：复制每个节点，将复制的每个节点连接到原始节点的后面
#     def CloneNodes(self, pHead):
#     	pNode = pHead

#     	while pNode:
#     		# 创建复制节点
#     		pClone = RandomListNode(0)
#     		pClone.label = pNode.label
#     		pClone.next = pNode.next

#     		pNode.next = pClone
#     		pNode = pClone.next

#     # 第二步：将复制后的链表的复制节点的random的指针链接到被复制的结点random指针的后一个节点
#     def CloneRandomNodes(self, pHead):
#     	pNode = pHead

#     	while pNode:
#     		pClone = pNode.next
#     		if pNode.random != None:
#     			# random 结点复制
#     			pClone.random = pNode.random.next
#     		pNode = pClone.next

#    	# 第三步：将原始链表的据结点拆分成原始链表及复制链表
#    	def ReconnectNodes(self, pHead):
#    		pNode = pHead
#    		pClonedNode = pNode.next
#    		pNode.next = pClonedNode.next
#    		pNode = pNode.next

#    		while pNode:
#    			pClonedNode.next = pNode.next
#    			pClonedNode = pClonedNode.next
#    			pNode.next = pClonedNode.next
#    			pNode = pNode.next

#    		return pClonedNode


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)
    # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            # pCloned.random = None         #不需要写这句话, 因为创建新的结点的时候,random自动指向None

            pNode.next = pCloned
            pNode = pCloned.next

    # 将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead
        
node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)