# coding:utf-8

'''
输入描述::等差数列 2，5，8，11，14...

输入一个正整数。

输出描述:

输出一个相加后的整数。

输入例子:

2

输出例子:

7
'''
while  True:
	try:
		print sum(range(2, input()*3, 3))
	except:
		break