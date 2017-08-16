# coding:utf-8
'''
大数相乘
-----------AC---------------------------->>>>>>>>>>>>
'''
def bignum_mult(stra, strb):

    a = list(stra)
    b = list(strb)
    la = len(stra)
    lb = len(strb)
    result = [0*i for i in range(la + lb)]

    for i in range(la):
        for j in range(lb):
            result[la - i - 1 + lb - j - 1] += int(a[i]) * int(b[j])

    for i in range(len(result) - 1):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10

    results = result[::-1]
    while results[0] == 0:
        del results[0]

    return ''.join([str(i) for i in results])

if __name__ == '__main__':

    array = raw_input().split(' ')
    stra = array[0]
    strb = array[1]
    res = bignum_mult(stra, strb)
    print res