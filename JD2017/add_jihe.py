# coding:utf-8
'''
求合集
状态--------------------------------------AC
'''
def add_jihe(a_array, b_array):

    pass

if __name__ == '__main__':

    n, m = [int(i) for i in raw_input().split()]
    a_array = [int(j) for j in raw_input().split()]
    b_array = [int(k) for k in raw_input().split()]

    a_array.extend(b_array)
    res_array = list(set(a_array))
    res_array.sort()

    print ' '.join([str(s) for s in res_array])