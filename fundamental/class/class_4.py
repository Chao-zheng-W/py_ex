#创建类
class Student:  #预定”类“首字母大写，其他小写
    native_place = '福建' #直接写在类里面的变量称为类属性
    def __init__(self,name,age):
        self.name = name  # self.namec称为实例属性
        self.age = age

    #类之外定义的叫函数，之内定义的称为方法
    #实例方法
    def eat(self): #自动补全self
        print('学生在吃饭。。。')

    #静态方法
    @staticmethod
    def sm(): #里面无参数
        print('使用了@staticmethod')

    #类方法
    @classmethod
    def cm(cls): #自动补全self.
        print('使用了@calssmethod')

#使用静态方法和类方法
print(Student.sm())
print(Student.cm())
