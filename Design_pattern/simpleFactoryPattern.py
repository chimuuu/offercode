# coding:utf-8

'''
简单工厂模式

模式特点：工厂根据条件产生不同功能的类。只生产单一类别的东西,不同功能却是同一类

程序实例：四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。

'''
class Operation(object):
    def GetResult(self):
        pass


# '+'操作符
class OperationAdd(Operation):
    def GetResult(self):
        return self.op1 + self.op2


# '-'操作符
class OperationSub(Operation):
    def GetResult(self):
        return self.op1 - self.op2


# '*'操作符
class OperationMul(Operation):
    def GetResult(self):
        return self.op1 + self.op2


# '/'操作符
class OperationDiv(Operation):
    def GetResult(self):
        try:
            # 浮点除法
            result = float(self.op1)/self.op2
            return result
        except:
            print "Error: divided by 0."
            return

# 未定义运算符
class OperationUnknown(Operation):
    def GetResult(self):
        return "this is an unknown operation"


class OperationFactory(object):
    ops = {}
    ops['+'] = OperationAdd()
    ops['-'] = OperationSub()
    ops['*'] = OperationMul()
    ops['/'] = OperationDiv()

    def CreateOp(self, ch):
        if ch in self.ops:
            op = self.ops[ch]
        else:
            op = OperationUnknown()
        return op

# 测试
if __name__ == '__main__':

    op1 = input("a: ")
    op = raw_input("Operation: ")
    op2 = input("b: ")

    factory = OperationFactory()
    cal = factory.CreateOp(op)
    cal.op1 = op1
    cal.op2 = op2

    print cal.GetResult()