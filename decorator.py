# coding:utf-8
'''
装饰器实现
闭包的应用

装饰器和被装饰函数都有参数时，
一：需要三层的嵌套
第一层传装饰器参数、第二层嵌套传函数、第三层传被装饰函数的参数

二：三层返回
最里层返回func(*args)拿到参数，外层返回最里层函数，最外层返回次外层
'''
def dec(isnot = False):
    print 'call dec'
    if isnot:
        def _dec(func):
            print 'in _dec %s', str(func)
            def in_dec(*args):
                print 'in dec args=',args
                if len(args) == 0:
                    return 0
                for val in args:
                    if not isinstance(val, int):
                        return 0
                return func(*args)
            return in_dec
    else:
        def _dec(func):
            print 'in else _dec'
            return func
    return _dec

@dec(False)
def my_sum(*args):
    print 'in my_sum'
    return sum(args)/len(args)

print my_sum(1,2,3,4,5,6,7,8,9,10)

