# env/bin/python
# coding:utf-8

# 排序算法之基数排序,又称桶排序(稳定排序) 时间复杂度为 0(nlog(r)m), 其中r为所采取的基数，而m为堆数
# 设单关键字的每个分量的取值范围均是C0<=Kj<=Crd-1(0<=j<=rd),
# 可能的取值个数rd称为基数．基数的选择和关键字的分解因关键字的类型而异．
# 　　(1).若关键字是十进制整数，则按个、十等位进行分解，基数rd=10,C0=0,C9=9,d为最长整数的位数．
# 　　(2).若关键字是小写的英文字符串，则rd=26,C0='a',C25='z',d为最长字符串的长度．
# 　　基数排序的基本思想是：从低位到高位依次对待排序的关键码进行分配和收集，经过d趟分配和收集，就可以得到一个有序序列．

import math

class Solution:
	# 插入排序
	def bulket_sort(self, alist, radix=10):
		k = int(math.ceil(math.log(max(alist), radix)))
		bucket = [[] for i in range(radix)]
		for i in range(1, k + 1):
			for j in alist:
				bucket[j / (radix ** (i - 1)) % (radix ** i)].append(j)
			del alist[:]
			for z in bucket:
				alist += z
				del z[:]
		return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = Solution()
print a.bulket_sort(alist)

