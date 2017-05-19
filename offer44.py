# -*- coding:utf-8 -*-
'''
面试44：扑克牌的顺子

'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        L = len(numbers)
        if numbers == None or L < 1:
        	return False

        # 将扑克牌中的特殊牌转化
        transDict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(L):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]

        # 数组排序
        numbers.sort()

        numberOfZero = 0
        numberOfGap = 0

        # 统计数组中0的个数
        # 方法一：遍历
        for i in range(L):
        	if numbers[i] == 0:
        		numberOfZero += 1

        # 统计数组中的间隔数目
        small = numberOfZero	# 数组从small开始不为0，比较相邻的数
        big = small + 1
        while big < L:
        	# 先判断有无对子出现
        	if numbers[small] == numbers[big]:
        		return False

        	numberOfGap += numbers[big] - numbers[small] - 1
        	small = big
        	big += 1
        return False if numberOfGap > numberOfZero else True

test = ['A', 3, 2, 5, 0]
test2 = [1,3,0,5,0]
s = Solution()
print(s.IsContinuous(test))
print(s.IsContinuous(test2))