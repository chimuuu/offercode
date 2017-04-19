# coding:utf-8

'''
输入描述:

输入两个字符串。第一个为短字符，第二个为长字符。

输出描述:

返回值：

输入例子:

bc
abc

输出例子:
true

'''
while True:
	try:
		s_short = raw_input()
		s_long = raw_input()
		l_short = len(s_short)

		num = 0
		for i in s_short:
			if i in s_long:
				num += 1

		if num == l_short:
			print 'true'
		else:
			print 'false'
	except:
		break