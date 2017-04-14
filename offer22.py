# -*- coding:utf-8 -*-
'''
建立一个辅助栈，把push序列的数字依次压入辅助栈，
每次压入后，比较辅助栈的栈顶元素和pop序列的首元素是否相等，
	相等的话就推出pop序列的首元素和辅助栈的栈顶元素，
	若最后辅助栈为空，则push序列可以对应于pop序列。
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
        	return False
        as_stack = []
        n = len(pushV)
        j = 0

        for i in pushV:
        	# 压入栈
        	as_stack.append(i)
        	while len(as_stack) and as_stack[-1] == popV[j]:	
        		as_stack.pop()
        		j += 1

        if as_stack:
        	return False
        return True

# 测试用例
pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popV))
print(S.IsPopOrder(pushV, popVF))