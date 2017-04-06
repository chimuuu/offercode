# -*- coding:utf-8 -*-
# 二分法查找数组最小的元素

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0

        size = len(rotateArray)
        index1 = 0
        index2 = size -1
        indexMid = index1
        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            
            indexMid = (index1+index2)/2
            if rotateArray[index1] == rotateArray[index2] and rotateArray[index1] == rotateArray[indexMid]:
                return Sorder(rotateArray, index1, index2)

            elif rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid

            elif rotateArray[indexMid] <= rotateArray[index2]:
                index2 = indexMid
            
        return rotateArray[indexMid]


        # 特殊处理之顺序查找(p70)
        def Sorder(rotateArray, index1, index2):
            result = rotateArray[index1]
            for i in range(1,size):
                if result >= rotateArray[i]:
                    result = rotateArray[i]
                return result