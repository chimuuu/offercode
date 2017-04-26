# -*- coding:utf-8 -*-

'''
把只包含素因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，
但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。 
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        if index == 1:
            return 1
        t2, t3, t5 = 0, 0, 0
        ans = [1]
        for i in range(1, index):
            ans.append(min(ans[t2]*2, ans[t3]*3, ans[t5]*5))
            if ans[i] == ans[t2]*2:
                t2+= 1
            if ans[i] == ans[t3]*3:
                t3+= 1
            if ans[i] == ans[t5]*5:
                t5+= 1
        return ans[index - 1]

num = Solution()
print(num.GetUglyNumber_Solution(5))