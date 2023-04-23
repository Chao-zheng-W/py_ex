#继承父类方法，并进行方法重写
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("我是%s，今年%d岁" % (self.name,self.age))

per1 =Person('张三',20)
per1.info()

class Student(Person):
    def __init__(self,name,age,num):
        super().__init__(name,age)
        self.num =num
    def infos(self):
        super().info()  # 继承父类方法
        print('学号是{0}'.format(self.num))

stu1 = Student('李四',30,1220807)
stu1.info()  #使用父类方法
print('-------------------------')
stu1.infos()  #使用重写后的方法