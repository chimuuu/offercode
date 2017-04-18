# coding:utf-8

'''
找出给定字符串中大写字符(即'A'-'Z')的个数

接口说明

    原型：int CalcCapital(String str);

    返回值：int

输入描述:

输入一个String数据

输出描述:

输出string中大写字母的个数

输入例子:

add123#$%#%#O

输出例子:

1
'''
while True:
	try:
		s = raw_input()
		num = 0
		for i in s:
			if 'A' <= i <= 'Z':
				num += 1
			else:
				pass
		print num
	except:
		break

