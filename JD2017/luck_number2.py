# coding:utf-8
'''
幸运数
状态------------------------------------AC
'''

def get_sum_x(num, x):
    '''
    :param num: 十进制数
    :param x: 需要转换的进制数
    :return: 进制转换后的各位和
    '''
    res = 0
    # 获取十进制各位和
    while num != 0:
        remainder = num % x
        res += remainder
        num = num/x
    return res


if __name__ == '__main__':

    n = input()
    luck_num = 1
    for i in range(2, n+1):
        if get_sum_x(i, 10) == get_sum_x(i, 2):
            luck_num += 1
        else:
            pass
    print luck_num
