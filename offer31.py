# -*- coding:utf-8 -*-
'''
连续子数组的最大和

'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # 分析数组规律
        if not array:
        	return []

        s_um = array[0]
        maxsum = array[0]

        for i in range(1, len(array)):
        	# 有贡献则加
        	if s_um > 0:
        		s_um += array[i]
        	# 无贡献则比较，判断最大值保存	 
        	else:
        		s_um = array[i]
        	if s_um > maxsum:
        		maxsum = s_um
        return maxsum

a = [1,-2,3,10,-4,7,2,-5]
b = [-2,-8,-1,-5,-9]
A = Solution()

print(A.FindGreatestSumOfSubArray(a))
print(A.FindGreatestSumOfSubArray(b))