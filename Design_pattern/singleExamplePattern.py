# coding=utf-8
# 单例模式（四种方法）

#-*- encoding=utf-8 -*-
print '----------------------方法1--------------------------'
#方法1,实现__new__方法
#并在将一个类的实例绑定到类变量_instance上,
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
#如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()
two.a = 3
print one.a
print id(one)
print id(two)
print one == two
print one is two


print '----------------------方法2--------------------------'
#   方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
#   同一个类的所有实例天然拥有相同的行为(方法),
#   只需要保证同一个类的所有实例具有相同的状态(属性)即可
#   所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
#   可参看:http://code.activestate.com/recipes/66531/
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1

one = MyClass2()
two = MyClass2()

#one和two是两个不同的对象,id, ==, is对比结果可看出
two.a = 3
print one.a
print id(one)
print id(two)
print one == two
print one is two
print id(one.__dict__)
print id(two.__dict__)


print '----------------------方法3--------------------------'
#   方法3:本质上是方法1的升级（或者说高级）版
#   使用__metaclass__（元类）的高级python用法
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(object):
    __metaclass__ = Singleton2

one = MyClass3()
two = MyClass3()

two.a = 3
print one.a
print id(one)
print id(two)
print one == two
print one is two


print '----------------------方法4--------------------------'
#   方法4:也是方法1的升级（高级）版本,
#   使用装饰器(decorator),
#   这是一种更pythonic,更elegant的方法,
#   单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


one = MyClass4()
two = MyClass4()

two.a = 3
print one.a
print id(one)
print id(two)
print one == two
print one is two
one.x = 1
print one.x
print two.x
