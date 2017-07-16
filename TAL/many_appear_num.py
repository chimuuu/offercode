# coding:utf8
'''
n个数里出现次数大于等于n/2的数
'''

def many_appear(a_array, n):
    '''
    :param array: 
    :return: 
    '''
    for i in a_array:
        if a_array.count(i) >= n/2:
            return i
        else:
            pass
    else:
        return ''



if __name__ == '__main__':

    array = [i for i in raw_input().split()]
    n = len(array)


    print many_appear(array, n)
