# -*- coding:utf-8 -*-
'''
面试51：正则表达式匹配
'''
import re
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == None or pattern == None:
            return False
        if s == "" and pattern == "":
            return True
        if pattern == "" and s != "":
            return False
         
        res = re.compile(str(pattern)+"$")
        result = res.match(str(s))
         
        if result is None:
            return False
        else:
            return True