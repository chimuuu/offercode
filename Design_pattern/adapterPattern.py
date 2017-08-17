# coding:utf-8

'''
适配器模式

模式特点：将一个类的接口转换成为客户希望的另外一个接口。

程序实例：用户通过适配器使用一个类的方法。

代码特点：无

所谓适配器模式是指是一种接口适配技术，它可通过某个类来使用另一个接口与之不兼容的类，运用此模式，两个类的接口都无需改动。
适配器模式主要应用于希望复用一些现存的类，但是接口又与复用环境要求不一致的情况，比如在需要对早期代码复用一些功能等应用上很有实际价值。
其中Target是用户期望的标准类，而Adaptee是我们需要匹配的类，二者通过Adapter匹配起来。
'''

# 期望输出类
class Target(object):
    def request(self):
        print 'Target request'


# 被适配类
class Adaptee(object):
    def specialRequest(self):
        print 'Adaptee specialRequest'


# 适配器
class Adpater(object):
    def __init__(self, adpatee):
        self.adpatee = adpatee

    def request(self):
        self.adpatee.specialRequest()


if __name__ == '__main__':
    objects = []
    a = Target()
    b = Adaptee()

    objects.append(a)
    objects.append(Adpater(b))  # 适配接口

    for obj in objects:
        obj.request()           # 调用相同接口

'''
输出：
C:\Python27\python.exe E:/codepy/designMode/adapterMode.py
Target request
Adaptee specialRequest

调用了相同的接口，但是却实现了特殊类的输出，即被适配的类通过通用接口也可以输出
'''
