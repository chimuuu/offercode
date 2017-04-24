# -*- coding:utf-8 -*-

'''
题目描述
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个
只出现一次的字符,并返回它的位置。如果字符串为空,返回-1 
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) <= 0:
       		return -1

        string_num = {}

        for i in s:
        	if i not in string_num:
        		string_num[i] = 0

        	string_num[i] += 1 

        for i in s:
        	if string_num[i] == 1:
        		return i
        		# OJ 返回位置
        		# return s.index(i)
        		break
        return -1

s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))