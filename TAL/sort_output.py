# coding:utf8
'''
输出n个整数里最小的k个数。升序输出
'''

def sort_ouput(a_array, n):
    '''
    :param array: 
    :return: 
    '''
    a_array.sort()
    return ' '.join([str(i) for i in a_array[0:n]])


if __name__ == '__main__':

    array = [int(i) for i in raw_input().split()]
    a_array  = array[:-1]
    n = array[-1]

    print sort_ouput(a_array, n)
