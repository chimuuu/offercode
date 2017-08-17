# coding:utf-8

'''
抽象工厂模式

模式特点：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类。

程序实例：提供对不同的数据库访问的支持。

　　　　　IUser和IDepartment是两种不同的抽象产品，它们都有mysql 和redis这两种不同的实现；
         IFactory是产生IUser和IDepartment的抽象工厂，
         根据具体实现（mysqlFactory和redisFactory）产生对应的具体的对象（mysqlUser与mysqlDepartment或者redisUser与redisDepartment）。

抽象工厂与简单工程的区别：
    简单工厂 ：用来生产同一等级结构中的任意产品。（对于增加新的产品，无能为力）
    工厂方法 ：用来生产同一等级结构中的固定产品。（支持增加任意产品）   
    抽象工厂 ：用来生产不同产品族的全部产品。（对于增加新的产品，无能为力；支持增加产品族） 
      
'''

# 抽象产品
class IUser:
    def GetUser(self):
        pass
    def InsertUser(self):
        pass

# 抽象产品
class IDepartment:
    def GetDepartment(self):
        pass
    def InsertDepartment(self):
        pass

# 实现
class mysqlUser(IUser):
    def GetUser(self):
        print "mysql GetUser"
    def InsertUser(self):
        print "mysql InsertUser"

# 实现
class mysqlDepartment(IDepartment):
    def GetDepartment(self):
        print "mysql GetDepartment"
    def InsertDepartment(self):
        print "mysql InsertDepartment"

# 实现
class redisUser(IUser):
    def GetUser(self):
        print "redis GetUser"
    def InsertUser(self):
        print "redis InsertUser"

# 实现
class redisDepartment(IDepartment):
    def GetDepartment(self):
        print "redis GetDepartment"
    def InsertDepartment(self):
        print "redis InsertDepartment"

# 抽象工厂
class IFactory:
    def CreateUser(self):
        pass
    def CreateDepartment(self):
        pass

# 具体工厂
class mysqlFactory(IFactory):
    def CreateUser(self):
        temp = mysqlUser()
        return temp
    def CreateDepartment(self):
        temp = mysqlDepartment()
        return temp

# 具体工厂
class redisFactory(IFactory):
    def CreateUser(self):
        temp = redisUser()
        return temp
    def CreateDepartment(self):
        temp = redisDepartment()
        return temp

if __name__ == "__main__":
    factory = redisFactory()
    user = factory.CreateUser()
    depart = factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()