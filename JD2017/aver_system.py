# coding:utf-8
'''
进制均值
状态---------------------------------AC
'''

def SysConvert_aver(L, A):

    res_sum = 0
    # 获取各个进制下的转换结果
    for i in range(2, A):
        temp = A
        while temp != 0:
            remainder = temp % i
            res_sum += remainder
            temp = temp / i

    # 获取最大公约数
    max_gcd = gcd(res_sum, L)

    return '%d' %(res_sum/max_gcd) + '/' + '%d' %(L/max_gcd)

def gcd(a, b):
    '''
    化简分数输出：最大公约数
    :param a: 
    :param b: 
    :return: gcd(a, b)
    '''
    while b > 0:
        c = a%b
        a = b
        b = c

    return a


if __name__ == '__main__':

    A = input()
    L = A - 2
    print SysConvert_aver(L, A)
