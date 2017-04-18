# coding:utf-8

'''
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
      都按先录入排列在前的规则处理。

   例示：
   jack      70
   peter     96
   Tom       70
   smith     67

   从高到低  成绩            
   peter     96    
   jack      70    
   Tom       70    
   smith     67    

   从低到高

   smith     67  

   Tom       70    
   jack      70    
   peter     96      

输入描述:

输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开



输出描述:

按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开


输入例子:

3
0
fang 90
yang 50
ning 70


输出例子:

fang 90
ning 70
yang 50
'''

while True:
	try:
		n = input()
		flag = input()

		num = []
		grade_dict = {}
		for i in range(n):
			s = raw_input()
			num.append(s)
		if flag == 1:
			res = sorted(num, key = lambda x: int(x.split()[1]), reverse = False)
		else:
			res = sorted(num, key = lambda x: int(x.split()[1]), reverse = True)

		for v in res:
			print v
	except:
		break