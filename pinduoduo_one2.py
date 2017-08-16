# coding:utf-8

import heapq

def solution(n, array):

    if n < 3:
        return False

    three_max = heapq.nlargest(3, array)
    two_min = heapq.nsmallest(2, array)

    max_res = max(three_max[0]*three_max[1]*three_max[2], two_min[0]*two_min[1]*three_max[0])
    return max_res


if __name__ == '__main__':

    n = input()
    array = [int(i) for i in raw_input().split()]
    print solution(n, array)