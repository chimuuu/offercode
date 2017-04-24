# -*- coding:utf-8 -*-
'''
面试50：字符串转换成整数
'''
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    # 如果输出是0, 通过检查flag判断输入不合法还是输入直接是'0'
    def StrToInt(self, s):
        flag = False
        if s == None or len(s) < 1:
            return 0
        numStack = []
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in dict.keys():
                numStack.append(dict[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0
        print(numStack)
        ans = 0
        if len(numStack) == 1 and numStack[0] == 0:
            flag = True
            return 0
        for i in numStack:
            ans = ans*10 + i
        if s[0] == '-':
            ans = 0 - ans
        return ans

test = '+2147483647'
s = Solution()
print(s.StrToInt(test))