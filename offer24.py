# coding:utf-8

'''

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
	如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
        	return False

        length = len(sequence)
        root = sequence[-1]

        # 在二叉搜索树中左子树的节点小于根节点
        for i in range(length):
        	if sequence[i] > root:
        		break

        # 在二叉搜索树中右子树的节点大于根节点
        for j in range(i, length):
        	if sequence[j] < root:
        		return False

        # 判断左子树是不是二叉树
        left = True
        if i > 0:
        	left = self.VerifySquenceOfBST(sequence[:i])
        

        right = True
        if j < length-1:
        	right = self.VerifySquenceOfBST(sequence[j:])
        return left and right


array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 1, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))