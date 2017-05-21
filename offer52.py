# -*- coding:UTF-8 -*-
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。 
'''
class Solution:
    def multiply(self, A):
        # write code here
        if A == None or len(A) <= 0:
        	return

        first = [1]
        second = [1]

        for i in range(1, len(A)):
        	first.append(first[i-1]*A[i-1])
        	second.append(second[i-1]*A[-i])

        B = []
        for i in range(0, len(A)):
        	B.append(first[i]*second[-(i+1)])
        return B

test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))	