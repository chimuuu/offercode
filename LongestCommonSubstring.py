# coding:utf-8
''''' 
求两个字符串的最长公共子串 
思想：建立一个二维数组，保存连续位相同与否的状态 
'''
def getNumofCommonSubstr(str1 , str2):
    lstr1 = len (str1)
    lstr2 = len (str2)
    record = [[0 for i in range (lstr2 + 1)] for j in range (lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range (lstr1):
        for j in range (lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - maxNum:p] , maxNum


if __name__ == '__main__':
    str1 = raw_input ()
    str2 = raw_input ()

    res = getNumofCommonSubstr (str1 , str2)
    print res




    # # coding:utf-8
# '''
# 求两个字符串的最长公共子串
# 思想：建立一个二维数组，保存连续位相同与否的状态
# '''
#
# def getNumofCommonSubstr(str1, str2):
#
#     lstr1 = len(str1)
#     lstr2 = len(str2)
#     record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)]  # 多一位
#     maxNum = 0          # 最长匹配长度
#     p = 0               # 匹配的起始位
#
#     if lstr1 < lstr2:
#         record = [[0 for i in range (lstr2 + 1)] for j in range (lstr1 + 1)]  # 多一位
#         for i in range(lstr1):
#             for j in range(lstr2):
#                 if str1[i] == str2[j]:
#                     # 相同则累加
#                     record[i+1][j+1] = record[i][j] + 1
#
#                     if record[i+1][j+1] > maxNum:
#                         # 获取最大匹配长度
#                         maxNum = record[i+1][j+1]
#                         # 记录最大匹配长度的终止位置
#                         p = i + 1
#         return str1[p - maxNum:p]
#     else:
#         record = [[0 for i in range (lstr1 + 1)] for j in range (lstr2 + 1)]  # 多一位
#         for i in range (lstr2):
#             for j in range (lstr1):
#                 if str2[i] == str1[j]:
#                     # 相同则累加
#                     record[i + 1][j + 1] = record[i][j] + 1
#
#                     if record[i + 1][j + 1] > maxNum:
#                         # 获取最大匹配长度
#                         maxNum = record[i + 1][j + 1]
#                         # 记录最大匹配长度的终止位置
#                         p = i + 1
#
#
#         return str2[p-maxNum:p]
#
#
# while True:
#     try:
#         str1 = raw_input()
#         str2 = raw_input()
#
#         print getNumofCommonSubstr(str1, str2)
#     except:
#         break