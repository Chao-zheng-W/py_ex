#创建类
class Student:  #约定”类“首字母大写，其他小写
    native_place = '福建' #直接写在类里面的变量称为类属性
    def __init__(self,name,age):
        self.name = name  # self.namec称为实例属性
        self.age = age

    #类之外定义的叫函数，之内定义的称为方法
    #实例方法
    def eat(self): #自动补全self
        print(self.name+'学生在吃饭。。。')

    #静态方法
    @staticmethod
    def sm(): #里面无参数
        print('使用了@staticmethod')

    #类方法
    @classmethod
    def cm(cls): #自动补全self.
        print('使用了@calssmethod')

#类属性由实例对象共享
stu1 =Student('张三',20)
stu2 =Student('李四',29)

#给stu1动态绑定属性
stu1.gender = '男'
print(stu1.gender)
#print(stu2.gender)   报错

#给stu1动态绑定方法
def show():
    print("一个函数")

stu1.show= show
stu1.show()  #在36行的前提下，绑定成功
#stu2.show() 报错
