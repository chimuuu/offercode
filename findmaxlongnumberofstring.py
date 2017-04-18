# coding:utf-8

'''
输入描述:

输入一个字符串。

输出描述:

输出字符串中最长的数字字符串和它的长度。如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度

输入例子:

abcd12345ed125ss123058789

输出例子:

123058789,9
'''
import re
while True:
	try:
		s = raw_input()
		res = re.compile(r'\d+')
		lis = re.findall(res, s)

		length = 0
		item = []
		for i in lis:
			j = len(i)

			if j > length:
				length = j
				item = []
				item.append(i)
			elif j == length:
				item.append(i)

		st = item[0]
		for s in item[1:]:	
			st = st + s

		print st + ',' + str(length)

	except:
		break

# s = raw_input()
# res = re.compile(r'\d+')
# lis = re.findall(res, s)

# length = 0
# item = []
# for i in lis:
# 	j = len(i)

# 	if j > length:
# 		length = j
# 		item = []
# 		item.append(i)
# 	elif j == length:
# 		item.append(i)

# for s in item:	
# 	print str(s),

# print ',' + str(length)
