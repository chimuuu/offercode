# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        temp = []
        for num in array:
            if array.count(num) == 1:
                temp.append(num)
        return temp