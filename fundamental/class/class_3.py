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
    def method(): #里面无参数
        print('使用了@staticmethod')

    #类方法
    @classmethod
    def cm(cls): #自动补全self.
        print('使用了@calssmethod')

#类属性由实例对象共享
stu1 =Student('张三',20)
stu2 =Student('李四',29)
print(stu1.native_place)
print(stu2.native_place)

#类属性被修改后，实例对象也受到影响
Student.native_place ="江西"
print(stu1.native_place)
print(stu2.native_place)
