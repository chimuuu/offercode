# coding:utf8
'''
字符串中找出连续最长的数字串
'''

def most_long_num(L, str_array):
    '''
    找出连续最长的数字串
    :param str_array: 
    :return: num
    '''
    num = []
    res = 0
    max_index = 0
    for i in range(L):
        if 47 < ord(str_array[i]) < 58:
            res += 1
        else:
            res = 0

        num.append(res)


    max_index = str_array.index('{}'.format(max(num)))

    return ''.join([i for i in str_array[max_index-max(num)+1:max_index+1]])

if __name__ == '__main__':

    str_array = [i for i in raw_input()]
    L = len(str_array)

    print most_long_num(L, str_array)
