# -*- coding:utf-8 -*-

'''
反转 单词顺序
'''

class Solution:
    def ReverseSentence(self, s):
        # write code he

        s = s.split()
        s.reverse()
        return ' '.join(s)

S = Solution()
s = 'I am a student.'
s1 = ' '
# print ''.join(s.split(' ')[::-1])
print(S.ReverseSentence(s))
print(S.ReverseSentence(s1))