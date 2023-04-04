-_#创建类，
class Student:  #预定”类“首字母大写，其他小写
    native_place = '福建' #直接写在类类里面的变量称为类属性
    def __int__(self,name,age):
        self.name = name  # self.namec称为实体属性

    #类之外定义的叫函数，之内定义的称为方法
    #实例方法
    def eat(self): #自动补全self
        print('学生在吃饭。。。')

    #静态方法
    @staticmethod
    def method(): #里面无参数
        print('使用了@staticmethod')

    #类方法
    @classmethod
    def cm(cls): #自动补全self.
        print('使用了@calssmethod')

#类本身也是对象，开辟了内存空间
print(Student,type(Student),id(Student))