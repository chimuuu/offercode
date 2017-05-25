# -*- coding:utf-8 -*-
'''
面试题62：序列化二叉树：最终要实现的是二叉树的序列化和反序列化。
    首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，
    再碰到左子节点或者右子节点为None的时候输出一个特殊字符"#"。对于反序列化，
    就是针对输入的一个序列构建一棵二叉树，我们可以设置一个指针先指向序列的最开始，
    然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续转化为左子树和右子树。
    当遇到当前指向的字符为特殊字符"#"或者指针超出了序列的长度，
    则返回None，指针后移，继续遍历。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 二叉树序列化
    def Serialize(self, root):
        serializeStr = ''
        if root == None:
            return '#'
        # stack 保存前序遍历结点
        stack = []
        while root or stack:
            while root:
                serializeStr += str(root.val) + ','
                stack.append(root)
                root = root.left
            serializeStr += '#,'
            root = stack.pop()
            root = root.right
        # 去掉最后的‘,#,’所以为-3
        serializeStr = serializeStr[:-3]
        return serializeStr

    # 二叉树的反序列化
    def Deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s,sp)
        node.right, sp = self.deserialize(s,sp)
        return node, sp

    # def Deserialize(self, s):
pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
result = S.Serialize(pNode1)
print(result)

result2 = S.Deserialize(result)
print(result2)
