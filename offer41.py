# -*- coding:utf-8 -*-
'''
面试41：题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。 
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        found = False
        if len(array) <= 0 or not tsum:
        	return []

        ahead = len(array)
        behind = 0

        while ahead > behind:
        	curSum = array[ahead-1] + array[behind]

        	if curSum == tsum:
        		found = True
        		break
        	elif curSum > tsum:
        		ahead -= 1
        	else:
        		behind += 1
        if found:
        	return array[behind], array[ahead-1]
        else:
        	return []

s = Solution()
print(s.FindNumbersWithSum([1,2,4,7,11,15], 15))
print(s.FindNumbersWithSum([1,2,4,7,11,16], 10))
print(s.FindNumbersWithSum([], 0))



'''
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1) // 2
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big+1)))
            while curSum > tsum and small < middle:
                curSum -= small
                small += 1
                if curSum == tsum:
                    output.append(list(range(small, big+1)))
            big += 1
            curSum += big
        return output

    def FindContinuousSequence2(self, tsum):
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) >> 1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output
s = Solution()
print(s.FindContinuousSequence2(15))