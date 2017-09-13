# usr/bin/env python
# _*_ coding:utf-8 _*_

'''
素数筛（Sieve of primes）：给定一个较大值n，寻找1~n中的所有素数，并把它打印出来。

判断一个数m是否是素数，需要花费O(√n)时间。
当然是遍历并判断的话，需要花费O(n√n)时间，
生产者实现也很简单:
1. 首先生成一个bool列表表示该index的数是否是素数；
2. 显然0,1不是素数；
3. 接下来判断2<=i<=n的数，
   如果为素数（True），则yield抛出，并把i的2倍，3倍,…,(n-1)/i+1倍都设为不是素数（False）。
这就是素数筛的原理，花费时间为O(n).
'''

def prime_sieve(n):
    flags = [True] * n
    flags[0] = flags[1] = False

    for i in xrange(2, n):
        if flags[i]:
            yield i

            for j in xrange(2, (n - 1) / i + 1):
                flags[i * j] = False

if __name__ == '__main__':
    n = input()
    sieves = prime_sieve(n)
    for sieve in sieves:
        print sieve
