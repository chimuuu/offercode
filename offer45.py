# -*- coding:utf-8 -*-
'''
题目描述
	圆圈中最后剩下的数字
	0，1，...，n-1这n各数字排成一个圆圈，从数字0开始每次从这个圆圈中删除第m个数字
	求这个圆圈中剩下的最后一个数字
	
	另一个解释
	然后,他随机指定一个数m,让编号为0的小朋友开始报数。
	每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
	从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友
'''

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1  or m < 1:
        	return -1
        last = 0
        people = range(n)
        i = 0
        for num in range(n, 1, -1):
        	i = (i+m-1)%num
        	people.pop(i)
        return people[-1]

A = Solution()
print(A.LastRemaining_Solution(5,3))