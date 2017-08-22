# -*- coding:utf-8 -*-
'''
题目描述
操作给定的二叉树，输出二叉树的三种遍历结果

前序遍历：根左右 8 6 5 7 10 9 11    第一位是根节点
中序遍历：左根右 5 6 7 8 9 10 11    中间一位是根节点
后续遍历：左右根 5 7 6 9 10 10 8    最后一位是根节点

输入描述:

二叉树
    	    8
    	   / \
    	  6   10
    	 / \  / \
    	5   7 9  11

'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 前序遍历：根左右
    def ProOrderTraverse(self, root):
        # write code here
        if not root:
            return

        print root.val
        self.ProOrderTraverse(root.left)
        self.ProOrderTraverse(root.right)

    # 中序遍历：左根右
    def inOrderTraverse(self, root):
        if not root:
            return

        self.inOrderTraverse(root.left)
        print root.val
        self.inOrderTraverse(root.right)


    # 后序遍历：左右根
    def PostOrderTraverse(self,root):
        if not root:
            return

        self.PostOrderTraverse(root.left)
        self.PostOrderTraverse(root.right)
        print root.val



pRoot1 = TreeNode(8)
pRoot2 = TreeNode(6)
pRoot3 = TreeNode(10)
pRoot4 = TreeNode(5)
pRoot5 = TreeNode(7)
pRoot6 = TreeNode(9)
pRoot7 = TreeNode(11)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot3.left = pRoot6
pRoot3.right = pRoot7

if __name__ == '__main__':
    s = Solution()

    print '<--------------前序遍历-------------->'
    s.ProOrderTraverse(pRoot1)
    print '<--------------中序遍历-------------->'
    s.inOrderTraverse(pRoot1)
    print '<--------------后序遍历-------------->'
    s.PostOrderTraverse(pRoot1)

