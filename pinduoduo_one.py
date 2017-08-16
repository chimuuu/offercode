# coding:utf-8

def solution(n, array):

    if n < 3:
        return False

    # 找出倒数第3大的位置
    max3 = Partition(array, 0, n-1)
    while max3 != n-3:
        if max3 < n-3:
            max3 = Partition(array, max3, n-1)
        elif max3 > n-3:
            max3 = Partition(array, 0, max3)

    max_res = array[max3]*array[max3+1]*array[max3+2]


    # 找出倒数第2小的位置
    min2 = Partition(array, 0, n - 1)
    while min2 != 1:
        if min2 < 1:
            min2 = Partition(array, 1, n-1)
        elif min2 > 1:
            min2 = Partition(array, 0, min2-1)

    min_res = array[min2-1]*array[min2]*max(array)

    return max(max_res, min_res)


def Partition(alist, low, high):
    # 取子表第一个记录作为枢轴记录
    pivot_key = alist[low]
    # 从表的两端交替向中间扫描

    while low < high:
        # 将比枢轴小的元素交换到底端
        while low < high and alist[high] >= pivot_key:
            high -= 1
        alist[low], alist[high] = alist[high], alist[low]

        # 将比枢轴大的元素交换到顶端
        while low < high and alist[low] <= pivot_key:
            low += 1
        alist[low], alist[high] = alist[high], alist[low]

    return low

if __name__ == '__main__':

    n = input()
    array = [int(i) for i in raw_input().split()]
    print solution(n, array)