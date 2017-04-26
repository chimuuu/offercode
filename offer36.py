# -*- coding:utf-8 -*-
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007 
'''
'''
思路：	这道题可以这么想，我们要找到数组中的逆序对，
		可以看做对数据进行排序，需要交换数组中的元素的次数，
		但是防止相同大小的元素发生交换，因此需要选择一个稳定的排序方法，
		记录发生交换的次数。那么，基于比较的稳定的排序方法中，最快的方法就是归并了，
		所以直接按照归并排序的思路，将数组分解、合并、排序即可。但是需要注意的是，
		在常规归并排序的时候，如果前一个元素大于后一个元素，直接进行交换即可，
		只进行了一次操作，但是对于这道题来讲，对于每一次的归并段，
		我们选择从后向前遍历，前面的归并段的某一个数值left[i]如果大于后面的某一个数值right[j]，
		因为在right自己独自排序的过程中，已经保证了right是有序的，
		所以j位置前面的数字全部小于right[j]，
		所以在这里逆序对的个数就会是 j-start-length，
		其中start是整个数组的起点，length是left的长度，然后再进行交换。
'''
class Solution:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0]*length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length-1)
        return count
    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start)//2
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start+length+1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count

    # 使用数据的index进行求解
    def InversePairs2(self, data):
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        i = 0
        while len(copy) > i:
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count

s = Solution()
print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))
